# Task Instructions

The objective of this task is to process user data from a CSV file and convert a filtered subset into a JSON format.

## Steps

1.  **Read the Input File**:
    - Locate the file at `/app/input.csv`.
    - The file contains user data with columns including `active`.

2.  **Filter Data**:
    - Identify rows where the `active` column is `true`.
    - The check must be case-insensitive (e.g., "True", "true", "TRUE" are all valid).

3.  **transform and Save**:
    - Convert the filtered rows into a list of dictionaries.
    - Write this list to a JSON file located at `/app/output.json`.
