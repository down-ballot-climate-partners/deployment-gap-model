"""Module for cleaning Ballot Ready data."""
import logging

import pandas as pd

from pudl.helpers import add_fips_ids

DATETIME_COLUMNS = ["race_created_at", "race_updated_at", "election_day"]

logger = logging.getLogger(__name__)


def _normalize_entities(ballot_ready: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Normalize ballot ready data into elections, position and race entities.

    Args:
        ballot_ready: Exploded, lightly cleaned raw data.

    Returns:
        trns_dfs: dataframes for elecitons, positions and races.
    """
    trns_dfs = {}
    # Elections
    election_pk_fields = ["election_id"]

    election_fields = [
        "election_id",
        "election_name",
        "election_day",
    ]
    assert (
        (ballot_ready.groupby(election_pk_fields)[election_fields].nunique() <= 1)
        .all()
        .all()
    ), "There is duplicate entity information in the elections dataframe."

    br_elections = ballot_ready.drop_duplicates(subset=election_pk_fields)[
        election_fields
    ].copy()
    assert br_elections.election_id.is_unique, "election_id is not unique."

    trns_dfs["br_elections"] = br_elections

    # Positions
    position_pk_fields = ["position_id"]

    position_fields = [
        "reference_year",
        "position_id",
        "position_name",
        "sub_area_name",
        "sub_area_value",
        "sub_area_name_secondary",
        "sub_area_value_secondary",
        "level",
        "tier",
        "is_judicial",
        "is_retention",
        "normalized_position_id",
        "normalized_position_name",
        "frequency",
        "partisan_type",
    ]
    # A small number of positions have multiple records where frequencies and referece_year
    # differ. This is because of edge cases where a position has changed its election year
    # or frequency due to redistricting or an election law. The old position_election_frequency
    # and the future/current one are reflected in the data.

    # check if position_id is unique
    deduplicated_positions = ballot_ready[position_fields].drop_duplicates()
    is_duplciate_position = deduplicated_positions.position_id.duplicated(keep=False)

    # If position_id is not unique, generate new position ids for the duplicates
    if is_duplciate_position.any():
        n_duplicates = is_duplciate_position.sum()
        logger.info(
            f"{n_duplicates / len(deduplicated_positions) * 100} % of positions have duplicates. Generating new position_ids for duplicates."
        )

        # Create a mapping of the old position_ids to the new position_ids
        new_index = ballot_ready.position_id.max() + 1
        duplicate_position_ids = deduplicated_positions[
            is_duplciate_position
        ].position_id.to_frame()
        duplicate_position_ids["new_position_id"] = range(
            new_index, new_index + n_duplicates
        )
        new_position_id_mapping = duplicate_position_ids.set_index(
            "position_id"
        ).to_dict()["new_position_id"]

        ballot_ready["position_id"] = ballot_ready["position_id"].replace(
            new_position_id_mapping
        )

    br_positions = ballot_ready.drop_duplicates(subset=position_pk_fields)[
        position_fields
    ].copy()
    assert (
        br_positions.position_id.is_unique
    ), "position_id is not unique. Deduplication did not work as expected."
    trns_dfs["br_positions"] = br_positions

    # Races
    race_pk_fields = ["race_id"]

    race_fields = [
        "race_id",
        "is_primary",
        "is_runoff",
        "is_unexpired",
        "number_of_seats",
        "race_created_at",
        "race_updated_at",
    ]
    assert (
        (ballot_ready.groupby(race_pk_fields)[race_fields].nunique() <= 1).all().all()
    ), "There is duplicate entity informaiton in the races table."
    # Add some one to many fields to the races table dataframe.
    race_fields += [
        "election_id",
        "position_id",
    ]
    br_races = ballot_ready.drop_duplicates(subset=race_pk_fields)[race_fields].copy()
    assert len(br_races) < len(ballot_ready)
    assert br_races.race_id.is_unique, "race_id is not unique!"

    trns_dfs["br_races"] = br_races

    # Create a county and position association table
    position_counties_fields = [
        "position_id",
        "county_id_fips",
        "raw_county",
        "state_id_fips",
        "raw_state",
    ]
    trns_dfs["br_positions_counties_assoc"] = ballot_ready.drop_duplicates(
        subset=["position_id", "county_id_fips"]
    )[position_counties_fields].copy()
    return trns_dfs


def _explode_counties(raw_ballot_ready: pd.DataFrame) -> pd.DataFrame:
    """Correct datatypes and explode counties columns.

    Args:
        raw_ballot_ready: raw ballot ready data.
    Returns:
        ballot_ready: lightly cleaned and exploded dataframe.
    """
    # Correct datatypes
    ballot_ready = raw_ballot_ready.convert_dtypes()
    for col in DATETIME_COLUMNS:
        ballot_ready[col] = pd.to_datetime(ballot_ready[col])

    # Explode counties column
    ballot_ready["counties"] = (
        ballot_ready.counties.str.replace('"', "").str[1:-1].str.split(", ")
    )

    exp_ballot_ready = ballot_ready.explode("counties").rename(
        columns={"counties": "county"}
    )

    duplicate_race = exp_ballot_ready.duplicated(
        subset=["county", "race_id"], keep=False
    )
    # Initial batch of raw data has duplicates in counties
    assert (
        duplicate_race.sum() <= 20
    ), "Found more duplicate county/race combinations that expected."

    # Drop duplicates. A later version of ballot ready data will remedy this problem.
    ballot_ready = exp_ballot_ready.drop_duplicates(subset=["county", "race_id"])
    assert ~ballot_ready.duplicated(subset=["county", "race_id"], keep=False).any()

    # Add state and county fips codes
    # Fix LaSalle Parish spelling to match addfips library
    ballot_ready.loc[
        (ballot_ready.county == "LaSalle Parish"), "county"
    ] = "La Salle Parish"
    ballot_ready = add_fips_ids(ballot_ready)

    # Valdez-Cordova Census Area was split into two areas in 2019
    # https://www.census.gov/programs-surveys/geography/technical-documentation/county-changes/2010.html
    # It is reasonable to split State and Federal elections between the two areas.
    # However, adding local elections to both counties is not appropriate. I'm going to do it
    # anyways because there aren't any great options for accurately geocoding the local elections.
    valdez = ballot_ready.query("county_id_fips == '02261'")
    if valdez.level.isin(["state", "federal"]).all():
        logger.info("Found a local election in the Valdez-Cordova Census Area!")

    ballot_ready = ballot_ready[ballot_ready.county_id_fips != "02261"].copy()

    valdez_corrections = [
        {"county": "Chugach Census Area", "county_id_fips": "02063"},
        {"county": "Copper River Census Area", "county_id_fips": "02066"},
    ]

    valdez_corrections_dfs = []
    for cor in valdez_corrections:
        corrected_df = valdez.copy()
        for field, value in cor.items():
            corrected_df[field] = value
        valdez_corrections_dfs.append(corrected_df)

    ballot_ready = pd.concat(valdez_corrections_dfs + [ballot_ready])

    # Drop unused columns
    ballot_ready = ballot_ready.drop(columns=["position_description"])
    ballot_ready = ballot_ready.rename(
        columns={"county": "raw_county", "state": "raw_state"}
    )

    # Clean up boolean columns
    bool_columns = [col for col in ballot_ready.columns if col.startswith("is_")]
    for col in bool_columns:
        ballot_ready[col] = ballot_ready[col].map({"t": True, "f": False})
    return ballot_ready


def transform(raw_dfs: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """Clean the Ballot Ready data.

    Transformations include:
    * Correct datatypes
    * Explode counties columns

    Args:
        raw_dfs: dictionary of dataframe names to raw dataframes.

    Returns
        trns_dfs: dictionary of dataframe names to cleaned dataframes.
    """
    raw_ballot_ready = raw_dfs["raw_ballot_ready"]
    ballot_ready = _explode_counties(raw_ballot_ready)
    return _normalize_entities(ballot_ready)
