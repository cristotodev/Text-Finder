"""
Class for exporting search results in different formats
"""

import json
import csv

class Exporter:
    @staticmethod
    def export_to_json(results: list, output_file: str):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

    @staticmethod
    def export_to_csv(results: list, output_file: str):
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Folder path", "File", "Found words"])
            writer.writerows(results)
