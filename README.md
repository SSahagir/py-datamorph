
# 🚀 py-datamorph

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Beta-brightgreen.svg)

**py-datamorph** is a high-performance, zero-dependency Python toolkit engineered for data developers and analysts. It provides a robust suite of tools for seamless data conversion (CSV, JSON, XML), deep data cleaning, and instant statistical analysis—all accessible via a powerful Command Line Interface (CLI) or as an importable module.

Developed as a professional utility, it eliminates the overhead of heavy libraries like `pandas` for essential data transformation tasks.

---

## 🌟 Key Features

* **Multi-Format Conversion:** Effortlessly transform datasets between CSV, JSON, and XML formats.
* **Deep Data Cleaning:** Automatically purge empty rows, strip invisible whitespace from cells, and gracefully handle real-world encoding issues like Excel's BOM (`utf-8-sig`).
* **Instant Data Statistics:** Generate comprehensive analytical reports (row counts, column definitions, file size) for any CSV file directly in your terminal.
* **Zero Dependencies:** Built 100% on Python's Standard Library. It’s lightweight, secure, and incredibly fast.
* **Interactive CLI:** A polished, mutually-exclusive command-line tool for immediate terminal usage without writing any code.

---

## 🛠️ Installation

You can install `py-datamorph` directly into your local Python environment.

### Local Installation
Navigate to the root directory of the project (where `setup.py` is located) and run:

```bash
pip install .
```

---

## 💻 Usage: Command Line Interface (CLI)

After installation, the `datamorph` command becomes available globally in your terminal.

### 1. Data Conversion
Easily switch between data formats. The output file is automatically generated in the same directory.

```bash
# Convert CSV to JSON
datamorph --csv2json dataset.csv

# Convert JSON to CSV
datamorph --json2csv data.json

# Convert XML to JSON
datamorph --xml2json config.xml
```

### 2. Deep Data Cleaning
Sanitize messy CSV files before feeding them into databases or machine learning models.

```bash
datamorph --clean raw_data.csv
```
*(Outputs a sanitized file named `raw_data_pro_cleaned.csv`)*

### 3. Dataset Analysis
Get a quick technical overview of your CSV dataset without writing a single line of code.

```bash
datamorph --stats sales_data.csv
```

---

## 🐍 Usage: As a Python Module

You can easily integrate `py-datamorph` into your own custom Python scripts.

```python
from py_datamorph.converter import DataMorphConverter
from py_datamorph.cleaner import DataMorphCleaner

# Initialize the toolkit
conv = DataMorphConverter()
cleaner = DataMorphCleaner()

# 1. Convert files programmatically
json_file_path = conv.csv_to_json("employees.csv")

# 2. Get dataset statistics as a dictionary
stats = cleaner.get_stats("employees.csv")
print(f"Dataset contains {stats['Total Records']} rows.")
```

---

## 🏗️ Project Architecture

```text
py-datamorph/
├── py_datamorph/
│   ├── __init__.py        # Package initialization
│   ├── converter.py       # Core conversion logic (CSV/JSON/XML)
│   ├── cleaner.py         # Advanced data cleaning & statistics logic
│   └── cli.py             # Command-line argument parsing and routing
├── setup.py               # Package build and distribution configuration
└── README.md              # Project documentation
```

---

## 📝 License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software for both educational and commercial purposes.

---

## 👨‍💻 Developed By

**Sk Sahagir** * **Academic Details:** * **Course:** Bachelor of Technology in Information Technology (IT)  
  * **Institute:** Government College of Engineering & Textile Technology, Serampore  
  * **Roll No:** 11000224051  
  * **Registration No:** 241100110219 (2024-25)  
* **Connect with me:** * 📧 [Email](mailto:sksahagira@gmail.com)  
  * 🔗 [LinkedIn](https://www.linkedin.com/in/your-profile-handle)  


```