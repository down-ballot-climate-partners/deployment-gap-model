"""
Extract gridstatus iso queues data from private bucket archive.

gridstatus code points directly at interconnection queue spreadsheets
on ISO queues websites. These spreadsheets can change without notice
and break the gridstatus API. We have a private archive of the gridstatus data
that allows us to pin the ETL code to a specific version of the raw
data. The version numbers are automatically generated by Google Cloud Storage
Object Versioning.
"""

import logging

import pandas as pd

import dbcp

logger = logging.getLogger(__name__)

ISO_QUEUE_VERSIONS: dict[str, str] = {
    "miso": "1728242350923420",
    "miso-pre-2017": "1709776311574737",
    "caiso": "1728242351254356",
    "pjm": "1728242351606642",
    "ercot": "1728242351929200",
    "spp": "1728242352244156",
    "nyiso": "1731568799445816",
    "isone": "1728242352913470",
}


def extract(iso_queue_versions: dict[str, str] = ISO_QUEUE_VERSIONS):
    """Extract gridstatus ISO Queue data."""
    iso_queues: dict[str, pd.DataFrame] = {}
    for iso, generation_num in iso_queue_versions.items():
        # MISO is an exception to the rule because we need multiple snapshots of the data
        filename = iso if iso != "miso-pre-2017" else "miso"
        uri = f"gs://dgm-archive/gridstatus/interconnection_queues/parquet/{filename}.parquet"
        path = dbcp.extract.helpers.cache_gcs_archive_file_locally(
            uri=uri, generation_num=generation_num
        )

        iso_queues[iso] = pd.read_parquet(path)

    return iso_queues
