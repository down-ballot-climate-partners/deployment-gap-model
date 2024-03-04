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

# These are the earliest version we have for ISOs
# except for spp and ISONE because the recent versions
# have columns the old versions don't.
ISO_QUEUE_VERSIONS: dict[str, str] = {
    "miso": "1681775160487863",
    "caiso": "1681775162586588",
    "pjm": "1681775160979859",
    "ercot": "1681775161342766",
    "spp": "1704654954488739",
    "nyiso": "1681775159356063",
    "isone": "1704654954804863",
}


def extract(iso_queue_versions: dict[str, str] = ISO_QUEUE_VERSIONS):
    """Extract gridstatus ISO Queue data."""
    iso_queues: dict[str, pd.DataFrame] = {}
    for iso, revision_num in iso_queue_versions.items():
        uri = f"gs://gridstatus-archive/interconnection_queues/{iso}.parquet"
        path = dbcp.extract.helpers.cache_gcs_archive_file_locally(
            uri=uri, revision_num=revision_num
        )

        iso_queues[iso] = pd.read_parquet(path)

    return iso_queues
