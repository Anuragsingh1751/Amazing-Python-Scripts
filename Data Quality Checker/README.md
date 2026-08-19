# CSV Data Quality Checker

A beginner-friendly Python script that checks a CSV file for common data-quality problems.

## Features

- Counts rows and columns
- Detects duplicate rows
- Counts missing values by column
- Finds completely empty columns
- Prints a simple quality status

## Requirements

Python 3.8 or newer. No external packages are required.

## Usage

```bash
python data_quality_checker.py path/to/file.csv
```

Example:

```bash
python data_quality_checker.py sales.csv
```

The script prints a concise report that can be used as a first step before cleaning or analyzing a dataset.
