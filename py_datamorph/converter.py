import csv
import json
import os
import xml.etree.ElementTree as ET

class DataMorphConverter:
    """Advanced class to handle multi-format data conversions."""
    
    @staticmethod
    def csv_to_json(csv_path, json_path=None, indent=4):
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Source CSV not found: {csv_path}")
        
        json_path = json_path or csv_path.replace('.csv', '.json')
        data = []
        
        # Using utf-8-sig to handle Excel-generated CSV BOM markers
        with open(csv_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        with open(json_path, mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent)
        return json_path

    @staticmethod
    def json_to_csv(json_path, csv_path=None):
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Source JSON not found: {json_path}")
        
        csv_path = csv_path or json_path.replace('.json', '.csv')
        
        with open(json_path, mode='r', encoding='utf-8') as f:
            data = json.load(f)

        if not data or not isinstance(data, list):
            raise ValueError("JSON content must be a list of objects for CSV conversion.")

        # Extract headers from the first dictionary in the list
        headers = data[0].keys()
        with open(csv_path, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        return csv_path

    @staticmethod
    def xml_to_json(xml_path, json_path=None):
        """Converts flat XML structures to JSON datasets."""
        if not os.path.exists(xml_path):
            raise FileNotFoundError(f"Source XML not found: {xml_path}")
            
        tree = ET.parse(xml_path)
        root = tree.getroot()
        json_path = json_path or xml_path.replace('.xml', '.json')
        
        data = []
        for child in root:
            # Captures child tags and their text content as key-value pairs
            entry = {subchild.tag: subchild.text for subchild in child}
            if entry: data.append(entry)
            
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return json_path