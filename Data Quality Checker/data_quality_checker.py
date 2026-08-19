"""Simple CSV data quality checker.

Checks a CSV file for common data-quality problems:
- Missing values
- Duplicate rows
- Empty columns

Usage:
    python data_quality_checker.py path/to/file.csv
"""

import csv
import sys
from pathlib import Path


def check_csv(file_path: str) -> None:
    """Print a concise data-quality report for a CSV file."""
    path = Path(file_path)

    if not path.is_file():
        print(f"Error: file not found: {file_path}")
        return

    try:
        with path.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames

            if not fieldnames:
                print("Error: CSV file has no header row.")
                return

            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        print(f"Error reading CSV: {exc}")
        return

    row_count = len(rows)
    duplicate_count = row_count - len({tuple(row.get(column, "") for column in fieldnames) for row in rows})

    missing_counts = {
        column: sum(not (row.get(column) or "").strip() for row in rows)
        for column in fieldnames
    }
    empty_columns = [column for column, count in missing_counts.items() if count == row_count]

    print("=" * 45)
    print("CSV DATA QUALITY REPORT")
    print("=" * 45)
    print(f"File: {path.name}")
    print(f"Rows: {row_count}")
    print(f"Columns: {len(fieldnames)}")
    print(f"Duplicate rows: {duplicate_count}")

    print("\nMissing values:")
    found_missing = False
    for column, count in missing_counts.items():
        if count:
            found_missing = True
            print(f"  - {column}: {count}")
    if not found_missing:
        print("  None")

    print("\nCompletely empty columns:")
    if empty_columns:
        for column in empty_columns:
            print(f"  - {column}")
    else:
        print("  None")

    print("\nQuality status:")
    if duplicate_count or any(missing_counts.values()):
        print("  Review recommended: data-quality issues were found.")
    else:
        print("  Good: no missing values or duplicate rows detected.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python data_quality_checker.py path/to/file.csv")
        sys.exit(1)

    check_csv(sys.argv[1])
