
import csv
from .base_processor import BaseProcessor

class CSVStatsCalculator(BaseProcessor):
    def process(self, filepath):
        with open(filepath, 'r') as infile:
            reader = csv.reader(infile)
            headers = next(reader)
            num_cols = len(headers)
            num_rows = sum(1 for row in reader)
        return {'num_rows': num_rows, 'num_cols': num_cols}
