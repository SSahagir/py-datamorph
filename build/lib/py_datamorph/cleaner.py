import csv
import os

class DataMorphCleaner:
    """Professional data cleaning and analysis utility."""

    @staticmethod
    def deep_clean(input_path, output_path=None):
        """
        Removes empty rows, strips whitespace from all fields, 
        and handles encoding inconsistencies.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"File not found: {input_path}")
            
        # FIXED: Changed input_csv to input_path
        output_path = output_path or input_path.replace('.csv', '_pro_cleaned.csv')
        cleaned_data = []

        with open(input_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                headers = [h.strip() for h in next(reader)]
                cleaned_data.append(headers)
            except StopIteration:
                return "Error: File is empty."
            
            for row in reader:
                # Clean every cell in the row
                clean_row = [cell.strip() for cell in row]
                # Keep row only if it contains at least one non-empty value
                if any(clean_row):
                    cleaned_data.append(clean_row)

        with open(output_path, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(cleaned_data)
        
        return output_path

    @staticmethod
    def get_stats(csv_path):
        """Generates a technical summary of the dataset for the user."""
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"File not found: {csv_path}")

        with open(csv_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            try:
                headers = next(reader)
                rows = list(reader)
            except StopIteration:
                return {"Status": "Empty File"}
            
        return {
            "Filename": os.path.basename(csv_path),
            "Total Records": len(rows),
            "Column Count": len(headers),
            "Fields": ", ".join(headers),
            "File Size": f"{os.path.getsize(csv_path) / 1024:.2f} KB"
        }