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
    Column("cost_millions", Integer),
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
