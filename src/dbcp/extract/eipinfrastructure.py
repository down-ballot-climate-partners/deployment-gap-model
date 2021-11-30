"""
Retrieve data from EIP Infrastructure spreadsheets for analysis.
"""
import logging

import pandas as pd

from dbcp.extract import excel
from pudl.helpers import fix_leading_zero_gen_ids

logger = logging.getLogger(__name__)


class Extractor(excel.GenericExtractor):
    """Extractor for the excel dataset EIA860."""

    def __init__(self, *args, **kwargs):
        """
        Initialize the module.

        Args:
            ds (:class:datastore.Datastore): Initialized datastore.
        """
        self.METADATA = excel.Metadata('eipinfrastructure')
        self.cols_added = []
        super().__init__(*args, **kwargs)

    def process_raw(self, df, page, **partition):
        """
        Apply necessary pre-processing to the dataframe.

        """
        df = df.rename(
            columns=self._metadata.get_column_map(page, **partition))
        return df
