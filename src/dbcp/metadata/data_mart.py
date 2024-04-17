"""SQL Alchemy metadata for the data mart tables."""
from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    Float,
    Integer,
    MetaData,
    String,
    Table,
)

metadata = MetaData()
schema = "data_mart"

counties_wide_format = Table(
    "counties_wide_format",
    metadata,
    Column("state_id_fips", String, nullable=False),
    Column("county_id_fips", String, primary_key=True),
    Column("state", String),
    Column("county", String, nullable=False),
    Column("county_total_co2e_tonnes_per_year", Float),
    Column("fossil_existing_capacity_mw", Float),
    Column("fossil_existing_co2e_tonnes_per_year", Float),
    Column("fossil_existing_facility_count", Integer),
    Column("fossil_proposed_capacity_mw", Float),
    Column("fossil_proposed_co2e_tonnes_per_year", Float),
    Column("fossil_proposed_facility_count", Integer),
    Column("renewable_and_battery_existing_capacity_mw", Float),
    Column("renewable_and_battery_existing_co2e_tonnes_per_year", Float),
    Column("renewable_and_battery_existing_facility_count", Integer),
    Column("renewable_and_battery_proposed_capacity_mw", Float),
    Column("renewable_and_battery_proposed_facility_count", Integer),
    Column("renewable_and_battery_proposed_avoided_co2e_tonnes_per_year", Float),
    Column("renewable_and_battery_proposed_capacity_mw_actionable", Float),
    Column("renewable_and_battery_proposed_facility_count_actionable", Integer),
    Column("renewable_and_battery_proposed_avoided_co2e_actionable", Float),
    Column("renewable_and_battery_proposed_capacity_mw_nearly_certain", Float),
    Column("renewable_and_battery_proposed_facility_count_nearly_certain", Integer),
    Column("renewable_and_battery_proposed_avoided_co2e_nearly_certain", Float),
    Column("infra_total_proposed_co2e_tonnes_per_year", Float),
    Column("infra_total_proposed_facility_count", Integer),
    Column("infra_total_proposed_nox_tonnes_per_year", Float),
    Column("infra_total_proposed_pm2_5_tonnes_per_year", Float),
    Column("battery_storage_existing_capacity_mw", Float),
    Column("battery_storage_existing_facility_count", Integer),
    Column("battery_storage_proposed_capacity_mw", Float),
    Column("battery_storage_proposed_facility_count", Integer),
    Column("coal_existing_capacity_mw", Float),
    Column("coal_existing_co2e_tonnes_per_year", Float),
    Column("coal_existing_facility_count", Integer),
    Column("coal_proposed_capacity_mw", Float),
    Column("coal_proposed_co2e_tonnes_per_year", Float),
    Column("coal_proposed_facility_count", Integer),
    Column("gas_existing_capacity_mw", Float),
    Column("gas_existing_co2e_tonnes_per_year", Float),
    Column("gas_existing_facility_count", Integer),
    Column("gas_proposed_capacity_mw", Float),
    Column("gas_proposed_co2e_tonnes_per_year", Float),
    Column("gas_proposed_facility_count", Integer),
    Column("offshore_wind_existing_capacity_mw", Float),
    Column("offshore_wind_existing_facility_count", Integer),
    Column("offshore_wind_proposed_capacity_mw", Float),
    Column("offshore_wind_proposed_facility_count", Integer),
    Column("offshore_wind_proposed_avoided_co2e_tonnes_per_year", Float),
    Column("offshore_wind_capacity_mw_via_ports", Float),
    Column("offshore_wind_interest_type", String),
    Column("offshore_wind_proposed_capacity_mw_actionable", Float),
    Column("offshore_wind_proposed_facility_count_actionable", Integer),
    Column("offshore_wind_proposed_avoided_co2e_actionable", Float),
    Column("offshore_wind_proposed_capacity_mw_nearly_certain", Float),
    Column("offshore_wind_proposed_facility_count_nearly_certain", Integer),
    Column("offshore_wind_proposed_avoided_co2e_nearly_certain", Float),
    Column("oil_existing_capacity_mw", Float),
    Column("oil_existing_co2e_tonnes_per_year", Float),
    Column("oil_existing_facility_count", Integer),
    Column("oil_proposed_capacity_mw", Float),
    Column("oil_proposed_co2e_tonnes_per_year", Float),
    Column("oil_proposed_facility_count", Integer),
    Column("onshore_wind_existing_capacity_mw", Float),
    Column("onshore_wind_existing_facility_count", Integer),
    Column("onshore_wind_proposed_capacity_mw", Float),
    Column("onshore_wind_proposed_facility_count", Integer),
    Column("onshore_wind_proposed_avoided_co2e_tonnes_per_year", Float),
    Column("onshore_wind_proposed_capacity_mw_actionable", Float),
    Column("onshore_wind_proposed_facility_count_actionable", Integer),
    Column("onshore_wind_proposed_avoided_co2e_actionable", Float),
    Column("onshore_wind_proposed_capacity_mw_nearly_certain", Float),
    Column("onshore_wind_proposed_facility_count_nearly_certain", Integer),
    Column("onshore_wind_proposed_avoided_co2e_nearly_certain", Float),
    Column("solar_existing_capacity_mw", Float),
    Column("solar_existing_co2e_tonnes_per_year", Float),
    Column("solar_existing_facility_count", Integer),
    Column("solar_proposed_capacity_mw", Float),
    Column("solar_proposed_facility_count", Integer),
    Column("solar_proposed_avoided_co2e_tonnes_per_year", Float),
    Column("solar_proposed_capacity_mw_actionable", Float),
    Column("solar_proposed_facility_count_actionable", Integer),
    Column("solar_proposed_avoided_co2e_actionable", Float),
    Column("solar_proposed_capacity_mw_nearly_certain", Float),
    Column("solar_proposed_facility_count_nearly_certain", Integer),
    Column("solar_proposed_avoided_co2e_nearly_certain", Float),
    Column("infra_gas_proposed_co2e_tonnes_per_year", Float),
    Column("infra_gas_proposed_facility_count", Integer),
    Column("infra_gas_proposed_nox_tonnes_per_year", Float),
    Column("infra_gas_proposed_pm2_5_tonnes_per_year", Float),
    Column("infra_lng_proposed_co2e_tonnes_per_year", Float),
    Column("infra_lng_proposed_facility_count", Integer),
    Column("infra_lng_proposed_nox_tonnes_per_year", Float),
    Column("infra_lng_proposed_pm2_5_tonnes_per_year", Float),
    Column("infra_oil_proposed_co2e_tonnes_per_year", Float),
    Column("infra_oil_proposed_facility_count", Integer),
    Column("infra_oil_proposed_nox_tonnes_per_year", Float),
    Column("infra_oil_proposed_pm2_5_tonnes_per_year", Float),
    Column(
        "infra_petrochemicals_and_plastics_proposed_co2e_tonnes_per_year",
        Float,
        nullable=True,
    ),
    Column(
        "infra_petrochemicals_and_plastics_proposed_facility_count",
        Integer,
        nullable=True,
    ),
    Column(
        "infra_petrochemicals_and_plastics_proposed_nox_tonnes_per_year",
        Float,
        nullable=True,
    ),
    Column(
        "infra_petrochemicals_and_plastics_proposed_pm2_5_tonnes_per_yea",
        Float,
        nullable=True,
    ),
    Column(
        "infra_synthetic_fertilizers_proposed_co2e_tonnes_per_year",
        Float,
        nullable=True,
    ),
    Column("infra_synthetic_fertilizers_proposed_facility_count", Integer),
    Column("infra_synthetic_fertilizers_proposed_nox_tonnes_per_year", Float),
    Column(
        "infra_synthetic_fertilizers_proposed_pm2_5_tonnes_per_year",
        Float,
        nullable=True,
    ),
    Column("ordinance_text", String),
    Column("ordinance_earliest_year_mentioned", Float),
    Column("ordinance_jurisdiction_name", String),
    Column("ordinance_jurisdiction_type", String),
    Column("ordinance_is_restrictive", Boolean),
    Column("ordinance_via_reldi", Boolean, nullable=False),
    Column("ordinance_via_solar_nrel", Boolean),
    Column("ordinance_via_wind_nrel", Boolean),
    Column("ordinance_via_nrel_is_de_facto", Boolean),
    Column("ordinance_via_self_maintained", Boolean),
    Column("state_permitting_type", String),
    Column("state_permitting_text", String),
    Column("total_tracts", Integer),
    Column("justice40_dbcp_index", Float),
    Column("n_distinct_qualifying_tracts", Integer),
    Column("n_tracts_agriculture_loss_low_income", Integer),
    Column("n_tracts_asthma_low_income", Integer),
    Column("n_tracts_below_poverty_and_low_high_school", Integer),
    Column("n_tracts_below_poverty_line_less_than_high_school_islands", Integer),
    Column("n_tracts_building_loss_low_income", Integer),
    Column("n_tracts_diabetes_low_income", Integer),
    Column("n_tracts_diesel_particulates_low_income", Integer),
    Column("n_tracts_energy_burden_low_income", Integer),
    Column("n_tracts_hazardous_waste_proximity_low_income", Integer),
    Column("n_tracts_heart_disease_low_income", Integer),
    Column("n_tracts_housing_burden_low_income", Integer),
    Column("n_tracts_lead_paint_and_median_home_price_low_income", Integer),
    Column("n_tracts_life_expectancy_low_income", Integer),
    Column("n_tracts_linguistic_isolation_and_low_high_school", Integer),
    Column("n_tracts_local_to_area_income_ratio_and_low_high_school", Integer),
    Column("n_tracts_local_to_area_income_ratio_less_than_high_school_islan", Integer),
    Column("n_tracts_pm2_5_low_income", Integer),
    Column("n_tracts_population_loss_low_income", Integer),
    Column("n_tracts_risk_management_plan_proximity_low_income", Integer),
    Column("n_tracts_superfund_proximity_low_income", Integer),
    Column("n_tracts_traffic_low_income", Integer),
    Column("n_tracts_unemployment_and_low_high_school", Integer),
    Column("n_tracts_unemployment_less_than_high_school_islands", Integer),
    Column("n_tracts_wastewater_low_income", Integer),
    Column("unprotected_land_area_km2", Float),
    Column("federal_fraction_unprotected_land", Float),
    Column("county_land_area_km2", Float),
    Column(
        "tribal_land_frac",
        Float,
        CheckConstraint("tribal_land_frac >= 0.0 AND tribal_land_frac <= 1.0"),
        nullable=False,
    ),
    Column("energy_community_coal_closures_area_fraction", Float),
    Column("energy_community_qualifies_via_employment", Boolean),
    Column("energy_community_qualifies", Boolean),
    schema=schema,
)

existing_plants = Table(
    "existing_plants",
    metadata,
    Column("plant_id_eia", Integer, primary_key=True),
    Column("resource", String, nullable=False),
    Column("max_operating_date", DateTime),
    Column("capacity_mw", Float, nullable=False),
    Column("co2e_tonnes_per_year", Float),
    Column("state_id_fips", String),
    Column("county_id_fips", String),
    Column("state", String),
    Column("county", String),
    schema=schema,
)

fossil_infrastructure_projects = Table(
    "fossil_infrastructure_projects",
    metadata,
    Column("project_id", Integer, primary_key=True),
    Column("project_name", String, nullable=False),
    Column("state", String),
    Column("county", String),
    Column("county_id_fips", String),
    Column("state_id_fips", String),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("raw_street_address", String),
    Column("air_construction_id", Float),
    Column("facility_id", Integer),
    Column("facility_name", String),
    Column("project_classification", String),
    Column("operating_status", String),
    Column("industry_sector", String, nullable=False),
    Column("raw_project_type", String),
    Column("project_description", String),
    Column("facility_description", String),
    Column("permit_description", String),
    Column("cost_millions", Float),
    Column("raw_number_of_jobs_promised", String),
    Column("date_modified", DateTime),
    Column("co2e_tonnes_per_year", Float),
    Column("voc_tonnes_per_year", Float),
    Column("so2_tonnes_per_year", Float),
    Column("nox_tonnes_per_year", Float),
    Column("co_tonnes_per_year", Float),
    Column("pm2_5_tonnes_per_year", Float),
    Column("total_wetlands_affected_permanently_acres", Float),
    Column("total_wetlands_affected_temporarily_acres", Float),
    Column("raw_estimated_population_within_3_miles", Float),
    Column("raw_percent_low_income_within_3_miles", Float),
    Column("raw_percent_people_of_color_within_3_miles", Float),
    Column("raw_respiratory_hazard_index_within_3_miles", Float),
    Column("raw_relative_cancer_risk_per_million_within_3_miles", Float),
    Column("raw_wastewater_discharge_indicator", Float),
    Column("is_ally_target", String, nullable=False),
    schema=schema,
)

iso_projects_wide_format = Table(
    "iso_projects_wide_format",
    metadata,
    Column("source", String, primary_key=True),
    Column("project_id", Integer, primary_key=True),
    Column("project_name", String),
    Column("iso_region", String),
    Column("entity", String),
    Column("utility", String),
    Column("developer", String),
    Column("state_1", String),
    Column("state_id_fips_1", String),
    Column("county_1", String),
    Column("county_id_fips_1", String),
    Column("county_2", String),
    Column("county_id_fips_2", String),
    Column("resource_class", String),
    Column("is_hybrid", Boolean, nullable=False),
    Column("is_actionable", Boolean),
    Column("is_nearly_certain", Boolean),
    Column("generation_type_1", String),
    Column("generation_capacity_mw_1", Float),
    Column("generation_type_2", String),
    Column("generation_capacity_mw_2", Float),
    Column("storage_type", String),
    Column("storage_capacity_mw", Float),
    Column("co2e_tonnes_per_year", Float, nullable=False),
    Column("date_entered_queue", DateTime),
    Column("date_proposed_online", DateTime),
    Column("interconnection_status", String),
    Column("point_of_interconnection", String),
    Column("queue_status", String, nullable=False),
    Column("ordinance_via_reldi", Boolean, nullable=False),
    Column("ordinance_jurisdiction_name", String),
    Column("ordinance_jurisdiction_type", String),
    Column("ordinance_earliest_year_mentioned", Integer),
    Column("ordinance_text", String),
    Column("ordinance_via_solar_nrel", Boolean),
    Column("ordinance_via_wind_nrel", Boolean),
    Column("ordinance_via_nrel_is_de_facto", Boolean),
    Column("ordinance_via_self_maintained", Boolean),
    Column("ordinance_is_restrictive", Boolean),
    Column("state_permitting_type", String),
    schema=schema,
)
iso_projects_long_format = Table(
    "iso_projects_long_format",
    metadata,
    # PK should be (source, project_id, resource_clean, county_id_fips)
    # but null county_id_fips values force the use of a surrogate key.
    Column("state", String),
    Column("county", String),
    Column("county_id_fips", String),
    Column("queue_id", String),
    Column("resource_clean", String, nullable=False),
    Column("project_id", Integer, nullable=False),
    Column("date_proposed_online", DateTime),
    Column("developer", String),
    Column("entity", String),
    Column("interconnection_status", String),
    Column("point_of_interconnection", String),
    Column("project_name", String),
    Column("date_entered_queue", DateTime),
    Column("queue_status", String, nullable=False),
    Column("iso_region", String),
    Column("utility", String),
    Column("capacity_mw", Float),
    Column("state_id_fips", String),
    Column("state_permitting_type", String),
    Column("co2e_tonnes_per_year", Float),
    Column("ordinance_earliest_year_mentioned", Float),
    Column("ordinance_jurisdiction_name", String),
    Column("ordinance_jurisdiction_type", String),
    Column("ordinance_text", String),
    Column("ordinance_via_reldi", Boolean, nullable=False),
    Column("ordinance_via_solar_nrel", Boolean),
    Column("ordinance_via_wind_nrel", Boolean),
    Column("ordinance_via_nrel_is_de_facto", Boolean),
    Column("ordinance_via_self_maintained", Boolean),
    Column("ordinance_is_restrictive", Boolean),
    Column("is_hybrid", Boolean, nullable=False),
    Column("is_actionable", Boolean),
    Column("is_nearly_certain", Boolean),
    Column("resource_class", String),
    Column("frac_locations_in_county", Float, nullable=False),
    Column("source", String, nullable=False),
    Column("surrogate_id", Integer, primary_key=True),
    schema=schema,
)

iso_projects_change_log = Table(
    "iso_projects_change_log",
    metadata,
    # PK should be (source, project_id, resource_clean, county_id_fips)
    # but null county_id_fips values force the use of a surrogate key.
    Column("state", String),
    Column("county", String),
    Column("county_id_fips", String),
    Column("queue_id", String),
    Column("resource_clean", String, nullable=False),
    Column("project_id", Integer, nullable=False),
    Column("date_proposed_online", DateTime),
    Column("developer", String),
    Column("entity", String),
    Column("interconnection_status", String),
    Column("point_of_interconnection", String),
    Column("project_name", String),
    Column("date_entered_queue", DateTime),
    Column("queue_status", String, nullable=False),
    Column("iso_region", String),
    Column("utility", String),
    Column("capacity_mw", Float),
    Column("state_id_fips", String),
    Column("state_permitting_type", String),
    Column("co2e_tonnes_per_year", Float),
    Column("ordinance_earliest_year_mentioned", Float),
    Column("ordinance_jurisdiction_name", String),
    Column("ordinance_jurisdiction_type", String),
    Column("ordinance_text", String),
    Column("ordinance_via_reldi", Boolean, nullable=False),
    Column("ordinance_via_solar_nrel", Boolean),
    Column("ordinance_via_wind_nrel", Boolean),
    Column("ordinance_via_nrel_is_de_facto", Boolean),
    Column("ordinance_via_self_maintained", Boolean),
    Column("ordinance_is_restrictive", Boolean),
    Column("is_hybrid", Boolean, nullable=False),
    Column("is_actionable", Boolean),
    Column("is_nearly_certain", Boolean),
    Column("resource_class", String),
    Column("frac_locations_in_county", Float, nullable=False),
    Column("source", String, nullable=False),
    Column("surrogate_id", Integer),
    Column("effective_date", DateTime),
    Column("end_date", DateTime, nullable=True),
    schema=schema,
)

counties_long_format = Table(
    "counties_long_format",
    metadata,
    Column("state_id_fips", String, nullable=False),
    Column("county_id_fips", String, primary_key=True),
    Column("state", String, nullable=False),
    Column("county", String, nullable=False),
    Column("facility_type", String, primary_key=True),
    Column("resource_or_sector", String, primary_key=True),
    Column("status", String, primary_key=True),
    Column("facility_count", Integer, nullable=False),
    Column("capacity_mw", Float),
    Column("actionable_mw_fraction", Float),
    Column("co2e_tonnes_per_year", Float),
    Column("pm2_5_tonnes_per_year", Float),
    Column("nox_tonnes_per_year", Float),
    Column("state_permitting_type", String),
    Column("state_permitting_text", String, nullable=False),
    Column("total_tracts", Integer),
    Column("justice40_dbcp_index", Float),
    Column("n_distinct_qualifying_tracts", Integer),
    Column("n_tracts_agriculture_loss_low_income", Integer),
    Column("n_tracts_asthma_low_income", Integer),
    Column("n_tracts_below_poverty_and_low_high_school", Integer),
    Column("n_tracts_below_poverty_line_less_than_high_school_islands", Integer),
    Column("n_tracts_building_loss_low_income", Integer),
    Column("n_tracts_diabetes_low_income", Integer),
    Column("n_tracts_diesel_particulates_low_income", Integer),
    Column("n_tracts_energy_burden_low_income", Integer),
    Column("n_tracts_hazardous_waste_proximity_low_income", Integer),
    Column("n_tracts_heart_disease_low_income", Integer),
    Column("n_tracts_housing_burden_low_income", Integer),
    Column("n_tracts_lead_paint_and_median_home_price_low_income", Integer),
    Column("n_tracts_life_expectancy_low_income", Integer),
    Column("n_tracts_linguistic_isolation_and_low_high_school", Integer),
    Column("n_tracts_local_to_area_income_ratio_and_low_high_school", Integer),
    Column("n_tracts_local_to_area_income_ratio_less_than_high_school_islan", Integer),
    Column("n_tracts_pm2_5_low_income", Integer),
    Column("n_tracts_population_loss_low_income", Integer),
    Column("n_tracts_risk_management_plan_proximity_low_income", Integer),
    Column("n_tracts_superfund_proximity_low_income", Integer),
    Column("n_tracts_traffic_low_income", Integer),
    Column("n_tracts_unemployment_and_low_high_school", Integer),
    Column("n_tracts_unemployment_less_than_high_school_islands", Integer),
    Column("n_tracts_wastewater_low_income", Integer),
    Column("ordinance_is_restrictive", Boolean),
    Column("ordinance_via_solar_nrel", Boolean),
    Column("ordinance_via_wind_nrel", Boolean),
    Column("ordinance_via_nrel_is_de_facto", Boolean),
    Column("ordinance_via_self_maintained", Boolean),
    Column("ordinance_via_reldi", Boolean, nullable=False),
    Column("ordinance_jurisdiction_name", String),
    Column("ordinance_jurisdiction_type", String),
    Column("ordinance_text", String),
    Column("ordinance_earliest_year_mentioned", Integer),
    Column("unprotected_land_area_km2", Float),
    Column("federal_fraction_unprotected_land", Float),
    Column("county_land_area_km2", Float),
    Column(
        "tribal_land_frac",
        Float,
        CheckConstraint("tribal_land_frac >= 0.0 AND tribal_land_frac <= 1.0"),
        nullable=False,
    ),
    Column("energy_community_coal_closures_area_fraction", Float),
    Column("energy_community_qualifies_via_employment", Boolean),
    Column("energy_community_qualifies", Boolean),
    schema=schema,
)

iso_counties_change_log = Table(
    "iso_counties_change_log",
    metadata,
    Column("county_id_fips", String, primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("county", String),
    Column("state_id_fips", String),
    Column("state", String),
    Column("withdrawn_clean_n_projects", Integer),
    Column("suspended_clean_n_projects", Integer),
    Column("new_clean_n_projects", Integer),
    Column("operational_clean_n_projects", Integer),
    Column("withdrawn_fossil_n_projects", Integer),
    Column("suspended_fossil_n_projects", Integer),
    Column("operational_fossil_n_projects", Integer),
    Column("new_fossil_n_projects", Integer),
    Column("new_other_n_projects", Integer),
    Column("withdrawn_other_n_projects", Integer),
    Column("suspended_other_n_projects", Integer),
    Column("operational_other_n_projects", Integer),
    Column("withdrawn_clean_capacity_mw", Float),
    Column("suspended_clean_capacity_mw", Float),
    Column("new_clean_capacity_mw", Float),
    Column("operational_clean_capacity_mw", Float),
    Column("withdrawn_fossil_capacity_mw", Float),
    Column("suspended_fossil_capacity_mw", Float),
    Column("operational_fossil_capacity_mw", Float),
    Column("new_fossil_capacity_mw", Float),
    Column("new_other_capacity_mw", Float),
    Column("withdrawn_other_capacity_mw", Float),
    Column("suspended_other_capacity_mw", Float),
    Column("operational_other_capacity_mw", Float),
    schema=schema,
)
iso_regions_change_log = Table(
    "iso_regions_change_log",
    metadata,
    Column("iso_region", String, primary_key=True),
    Column("date", DateTime, primary_key=True),
    Column("withdrawn_clean_n_projects", Integer),
    Column("suspended_clean_n_projects", Integer),
    Column("new_clean_n_projects", Integer),
    Column("operational_clean_n_projects", Integer),
    Column("withdrawn_fossil_n_projects", Integer),
    Column("suspended_fossil_n_projects", Integer),
    Column("operational_fossil_n_projects", Integer),
    Column("new_fossil_n_projects", Integer),
    Column("new_other_n_projects", Integer),
    Column("withdrawn_other_n_projects", Integer),
    Column("suspended_other_n_projects", Integer),
    Column("operational_other_n_projects", Integer),
    Column("withdrawn_clean_capacity_mw", Float),
    Column("suspended_clean_capacity_mw", Float),
    Column("new_clean_capacity_mw", Float),
    Column("operational_clean_capacity_mw", Float),
    Column("withdrawn_fossil_capacity_mw", Float),
    Column("suspended_fossil_capacity_mw", Float),
    Column("operational_fossil_capacity_mw", Float),
    Column("new_fossil_capacity_mw", Float),
    Column("new_other_capacity_mw", Float),
    Column("withdrawn_other_capacity_mw", Float),
    Column("suspended_other_capacity_mw", Float),
    Column("operational_other_capacity_mw", Float),
    schema=schema,
)

br_election_data = Table(
    "br_election_data",
    metadata,
    Column("race_id", Integer, nullable=False, primary_key=True),
    Column("raw_county", String, nullable=False, primary_key=True),
    Column("state_name", String, nullable=False),
    Column("county_name", String),
    Column("election_id", Integer, nullable=False),
    Column("election_name", String, nullable=False),
    Column("election_day", DateTime, nullable=False),
    Column("is_primary", Boolean, nullable=False),
    Column("is_runoff", Boolean, nullable=False),
    Column("is_unexpired", Boolean, nullable=False),
    Column("position_id", Integer, nullable=False),
    Column("position_name", String, nullable=False),
    Column("sub_area_name", String),
    Column("sub_area_value", String),
    Column("sub_area_name_secondary", String),
    Column("sub_area_value_secondary", String),
    Column("raw_state", String, nullable=False),
    Column("level", String, nullable=False),
    Column("tier", Integer, nullable=False),
    Column("is_judicial", Boolean, nullable=False),
    Column("is_retention", Boolean, nullable=False),
    Column("number_of_seats", Integer, nullable=False),
    Column("normalized_position_id", Integer, nullable=False),
    Column("normalized_position_name", String, nullable=False),
    Column(
        "frequency", String, nullable=True
    ),  # Starting 2023-10-03 update there were a couple hundred nulls
    Column(
        "reference_year", String, nullable=True
    ),  # Starting 2023-10-03 update there were a couple hundred nulls
    Column("partisan_type", String),
    Column("race_created_at", DateTime, nullable=False),
    Column("race_updated_at", DateTime, nullable=False),
    Column("state_id_fips", String, nullable=False),
    Column("county_id_fips", String),  # Should not be nullable in future updates
    schema=schema,
)

county_commission_election_info = Table(
    "county_commission_election_info",
    metadata,
    Column("county_id_fips", String, nullable=False, primary_key=True),
    Column("county_name", String, nullable=False),
    Column("next_general_election_id", Integer),
    Column("next_general_election_name", String),
    Column("next_general_election_day", DateTime),
    Column("next_general_total_n_seats", Integer),
    Column("next_general_total_n_races", Integer),
    Column("next_general_all_race_names", String),
    Column("next_general_frequency", String),
    Column("next_general_reference_year", Integer),
    Column("next_primary_election_id", Integer),
    Column("next_primary_election_name", String),
    Column("next_primary_election_day", DateTime),
    Column("next_primary_total_n_seats", Integer),
    Column("next_primary_total_n_races", Integer),
    Column("next_primary_all_race_names", String),
    Column("next_primary_frequency", String),
    Column("next_primary_reference_year", Integer),
    Column("next_run_off_election_id", Integer),
    Column("next_run_off_election_name", String),
    Column("next_run_off_election_day", DateTime),
    Column("next_run_off_total_n_seats", Integer),
    Column("next_run_off_total_n_races", Integer),
    Column("next_run_off_all_race_names", String),
    Column("next_run_off_frequency", String),
    Column("next_run_off_reference_year", Integer),
    schema=schema,
)

pudl_eia860m_changelog = Table(
    "pudl_eia860m_changelog",
    metadata,
    Column("report_date", DateTime, primary_key=True),
    Column("generator_id", String, primary_key=True),
    Column("plant_id_eia", Integer, primary_key=True),
    Column("valid_until_date", DateTime),
    Column("plant_name_eia", String),
    Column("utility_id_eia", Integer),
    Column("utility_name_eia", String),
    Column("capacity_mw", Float),
    Column("county", String),
    Column("current_planned_generator_operating_date", DateTime),
    Column("data_maturity", String),
    Column("energy_source_code_1", String),
    Column("energy_storage_capacity_mwh", Float),
    Column("fuel_type_code_pudl", String),
    Column("generator_retirement_date", DateTime),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("net_capacity_mwdc", Float),
    Column("operational_status", String),
    Column("raw_operational_status_code", String),
    Column("operational_status_code", Integer, nullable=True),
    Column("planned_derate_date", DateTime),
    Column("planned_generator_retirement_date", DateTime),
    Column("planned_net_summer_capacity_derate_mw", Float),
    Column("planned_net_summer_capacity_uprate_mw", Float),
    Column("planned_uprate_date", DateTime),
    Column("prime_mover_code", String),
    Column("state", String),
    Column("summer_capacity_mw", Float),
    Column("technology_description", String),
    Column("winter_capacity_mw", Float),
    Column(
        "state_id_fips",
        String,
        nullable=True,
    ),
    Column(
        "county_id_fips",
        String,
        nullable=True,
    ),  # Should not be nullable in future updates
    schema=schema,
)
