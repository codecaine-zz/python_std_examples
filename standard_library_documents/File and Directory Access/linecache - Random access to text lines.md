# linecache — Random access to text lines

**LineCache Module**
=====================

The `linecache` module provides an interface to access text files line by line, allowing for random access and efficient memory usage.

**Installation**
---------------

You can install the `linecache` module using pip:
```bash
pip install linecache
```
**Code Examples**
-----------------

### 1. Reading a Text File Line by Line

```python
import linecache

# Read the first 10 lines from the file 'example.txt'
lines = linecache.getlines('example.txt', count=10)

for line in lines:
    print(line)
```

### 2. Accessing a Specific Line by Number

```python
import linecache

# Get the 5th line from the file 'example.txt'
line = linecache.getline('example.txt', 5)

print(line)
```

### 3. Checking if a File Exists and Returns an Empty List on Failure

```python
import linecache

try:
    lines = linecache.getlines('non_existent_file.txt')
except FileNotFoundError:
    print("File does not exist")
else:
    # File exists, process the contents
    for line in lines:
        print(line)
```

### 4. Reading a Text File and Returning Only Unique Lines

```python
import linecache

def get_unique_lines(file_name):
    unique_lines = set()
    with open(file_name, 'r') as f:
        for line in f:
            if line.strip() not in unique_lines:
                unique_lines.add(line.strip())
    return list(unique_lines)

unique_lines = get_unique_lines('example.txt')
for line in unique_lines:
    print(line)
```

### 5. Reading a Text File and Returning Only Lines Containing a Specific Word

```python
import linecache

def get_lines_with_word(file_name, word):
    matching_lines = []
    with open(file_name, 'r') as f:
        for line in f:
            if word.lower() in line.lower():
                matching_lines.append(line.strip())
    return matching_lines

matching_lines = get_lines_with_word('example.txt', 'hello')
for line in matching_lines:
    print(line)
```

### 6. Using `getlines` with a Custom Line Separator

```python
import linecache

# Specify a custom line separator (e.g., newline followed by tab)
custom_separator = "\n\t"

lines = linecache.getlines('example.txt', sep=custom_separator)

for i, line in enumerate(lines):
    print(f"Line {i+1}: {line}")
```

Note: The `getlines` function returns an iterator yielding lines from the file. If you need to use a different separator or have more complex requirements, consider using `open` and `split` methods instead.

**Error Handling**
-----------------

When working with files that may not exist or have issues reading them, it's essential to handle potential errors. The `linecache` module provides no explicit error handling; you must implement it yourself based on your specific needs and requirements.
