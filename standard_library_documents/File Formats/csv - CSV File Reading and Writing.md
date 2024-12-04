# csv - CSV File Reading and Writing

Below are comprehensive examples of how to read from and write to CSV files using the `csv` module in Python 3.12. Each example includes detailed comments explaining each step.

### Example 1: Writing a CSV file

```python
import csv

# Data to be written into a CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Define the filename for the CSV file
filename = 'output.csv'

# Open a file in write mode and create a CSV writer object
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(data[0])

    # Write the data rows starting from the second element of the list
    for row in data[1:]:
        writer.writerow(row)

# Print a confirmation message
print(f'Data has been written to {filename}')
```

### Explanation:

- **Importing `csv` module**: We import the `csv` module, which provides functionality for reading and writing CSV files.
- **Data Preparation**: We define a list of lists (`data`) where each inner list represents a row in the CSV file. The first inner list contains column headers.
- **File Handling**: We open the specified file in write mode (`'w'`). The `newline=''` argument is used to ensure consistent line endings on different operating systems.
- **CSV Writer**: We create a `csv.writer` object, which allows us to write rows of data to the CSV file.
- **Writing Headers**: We use `writer.writerow()` to write the header row.
- **Writing Data Rows**: We loop through the data starting from the second element and write each row using `writer.writerow()`.
- **Confirmation Message**: Finally, we print a confirmation message indicating that the data has been written.

### Example 2: Reading a CSV file

```python
import csv

# Define the filename for the CSV file
filename = 'input.csv'

# Open the file in read mode and create a CSV reader object
with open(filename, mode='r') as file:
    reader = csv.reader(file)

    # Read all rows from the CSV file
    rows = list(reader)

    # Print each row
    for row in rows:
        print(row)

# Print the total number of rows read
print(f'Total number of rows: {len(rows)}')
```

### Explanation:

- **Importing `csv` module**: We import the `csv` module, which provides functionality for reading and writing CSV files.
- **File Handling**: We open the specified file in read mode (`'r'`).
- **CSV Reader**: We create a `csv.reader` object, which allows us to read rows of data from the CSV file.
- **Reading Rows**: We use `reader.readlines()` to read all rows into a list. Note that this method reads the entire file into memory.
- **Printing Rows**: We loop through the list and print each row.
- **Total Row Count**: Finally, we print the total number of rows read.

### Example 3: Writing a CSV file with DictWriter

```python
import csv

# Data to be written into a CSV file using DictWriter
data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]

# Define the filename for the CSV file
filename = 'output_dict.csv'

# Open a file in write mode and create a DictWriter object
with open(filename, mode='w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']  # Column names
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for row in data:
        writer.writerow(row)

# Print a confirmation message
print(f'Data has been written to {filename}')
```

### Explanation:

- **Importing `csv` module**: We import the `csv` module, which provides functionality for reading and writing CSV files.
- **Data Preparation**: We define a list of dictionaries (`data`) where each dictionary represents a row in the CSV file with keys corresponding to column headers.
- **File Handling**: We open the specified file in write mode (`'w'`). The `newline=''` argument is used to ensure consistent line endings on different operating systems.
- **CSV Writer**: We create a `csv.DictWriter` object, which allows us to write rows of data using dictionary keys. We specify `fieldnames` as the list of column headers.
- **Writing Headers**: We use `writer.writeheader()` to write the header row.
- **Writing Data Rows**: We loop through the data and write each row using `writer.writerow()`.
- **Confirmation Message**: Finally, we print a confirmation message indicating that the data has been written.

### Example 4: Reading a CSV file with DictReader

```python
import csv

# Define the filename for the CSV file
filename = 'input_dict.csv'

# Open the file in read mode and create a DictReader object
with open(filename, mode='r') as file:
    reader = csv.DictReader(file)

    # Read all rows from the CSV file
    rows = list(reader)

    # Print each row
    for row in rows:
        print(row)

# Print the total number of rows read
print(f'Total number of rows: {len(rows)}')
```

### Explanation:

- **Importing `csv` module**: We import the `csv` module, which provides functionality for reading and writing CSV files.
- **File Handling**: We open the specified file in read mode (`'r'`).
- **CSV Reader**: We create a `csv.DictReader` object, which allows us to read rows of data as dictionaries with keys corresponding to column headers.
- **Reading Rows**: We use `reader.readlines()` to read all rows into a list. Note that this method reads the entire file into memory.
- **Printing Rows**: We loop through the list and print each row.
- **Total Row Count**: Finally, we print the total number of rows read.

These examples cover basic operations for reading from and writing to CSV files using Python's `csv` module. You can expand upon these examples by handling different types of data, such as complex numbers or custom objects, by implementing appropriate serialization and deserialization logic.
