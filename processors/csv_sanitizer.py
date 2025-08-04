import csv
from .base_processor import BaseProcessor

class CSVSanitizer(BaseProcessor):
    def process(self, filepath):
        sanitized_filepath = filepath.replace('.csv', '_sanitized.csv')
        with open(filepath, 'r') as infile, open(sanitized_filepath, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            headers = next(reader)
            sanitized_headers = [h.lower().replace(' ', '_') for h in headers]
            writer.writerow(sanitized_headers)
            
            for row in reader:
                writer.writerow(row)
        return sanitized_filepath
