# csv — CSV File Reading and Writing

**CSV Module Documentation**
=====================================

The `csv` module provides classes for reading and writing tabular data in CSV (Comma Separated Values) format.

### Importing the csv Module
```python
import csv
```

### Reading a CSV File
------------------------

You can use the `reader` function to read a CSV file:
```python
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in reader:
        print(row)
```

This will output:
```
['Name,Age,Country']
['John,25,USA']
['Alice,30,UK']
```

### Writing a CSV File
-----------------------

You can use the `writer` function to write data to a CSV file:
```python
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write data to the CSV file
    writer.writerow(['Name', 'Age', 'Country'])
    writer.writerow(['John', 25, 'USA'])
    writer.writerow(['Alice', 30, 'UK'])
```

This will create a new CSV file `data.csv` with the following content:
```
Name,Age,Country
John,25,USA
Alice,30,UK
```

### Specifying Field Names
---------------------------

You can specify field names when writing data to a CSV file using the `fieldnames` parameter:
```python
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, fieldnames=['Name', 'Age', 'Country'])
    
    # Write data to the CSV file
    writer.writerow(['John', 25, 'USA'])
    writer.writerow(['Alice', 30, 'UK'])
```

This will create a new CSV file `data.csv` with the following content:
```
Name,Age,Country
John,25,USA
Alice,30,UK
```

### Error Handling
------------------

You can use try-except blocks to handle errors when reading or writing CSV files:
```python
try:
    with open('non_existent_file.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found.")
```

This will output "File not found." instead of raising an error.

### CSV Reader Options
-----------------------

You can use the `reader` function with various options to customize its behavior:

*   ` delimiter`: specifies the delimiter character (default: `,`)
*   ` quotechar`: specifies the character used for quoting (default: `'`)
*   `escapechar`: specifies the character used for escaping (default: `\`)
*   `lineterminator`: specifies the line terminator character (default: `\n`)

```python
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"', escapechar='\\', lineterminator='\r\n')
    
    # Iterate over each row in the CSV file
    for row in reader:
        print(row)
```

This will output rows with semicolon (`;`) delimiters and double quotes (`"`) for quoting.

### CSV Writer Options
-----------------------

You can use the `writer` function with various options to customize its behavior:

*   `delimiter`: specifies the delimiter character (default: `,`)
*   `quotechar`: specifies the character used for quoting (default: `'`)
*   `escapechar`: specifies the character used for escaping (default: `\`)
*   `lineterminator`: specifies the line terminator character (default: `\n`)

```python
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', escapechar='\\', lineterminator='\r\n')
    
    # Write data to the CSV file
    writer.writerow(['Name', 'Age', 'Country'])
    writer.writerow(['John', 25, 'USA'])
    writer.writerow(['Alice', 30, 'UK'])
```

This will create a new CSV file `data.csv` with semicolon (`;`) delimiters and double quotes (`"`) for quoting.
