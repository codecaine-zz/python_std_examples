# linecache - Random access to text lines

The `linecache` module provides a way to access lines of files, even if the file is not open or has been changed since it was last accessed. This can be particularly useful when you need to process large files without reading them entirely into memory.

Here are some comprehensive code examples for using the `linecache` module:

### Example 1: Retrieve a line from a file

```python
import linecache

# Specify the path to the file and the line number
file_path = '/path/to/your/file.txt'
line_number = 5

try:
    # Get the specified line from the file
    line_content = linecache.getline(file_path, line_number)
    
    print(f"Line {line_number} in '{file_path}':")
    print(line_content.strip())  # Remove any trailing newline character
except FileNotFoundError:
    print("The file does not exist.")
```

### Example 2: Retrieve all lines from a file and store them in a list

```python
import linecache

# Specify the path to the file
file_path = '/path/to/your/file.txt'

try:
    # Get all lines from the file into a list
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    print("All lines in '{file_path}':")
    for line in lines:
        print(line.strip())
except FileNotFoundError:
    print("The file does not exist.")
```

### Example 3: Store the contents of a file in memory and retrieve a specific line

```python
import linecache

# Specify the path to the file
file_path = '/path/to/your/file.txt'

try:
    # Load all lines into memory
    lines = linecache.getlines(file_path)
    
    # Specify the line number
    line_number = 3
    
    print(f"Line {line_number} in '{file_path}':")
    print(lines[line_number - 1].strip())  # Adjust for zero-based indexing
except FileNotFoundError:
    print("The file does not exist.")
```

### Example 4: Clear the cache to free up memory

```python
import linecache

# Specify the path to the file
file_path = '/path/to/your/file.txt'

try:
    # Get a line from the file
    line_content = linecache.getline(file_path, 1)
    
    print(f"Line 1 in '{file_path}':")
    print(line_content.strip())
except FileNotFoundError:
    print("The file does not exist.")

# Clear the cache to free up memory
linecache.clearcache()
```

### Example 5: Retrieve lines from multiple files and process them

```python
import linecache

# List of file paths
file_paths = ['/path/to/file1.txt', '/path/to/file2.txt']

try:
    # Retrieve all lines from each file
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        print(f"Lines in '{file_path}':")
        for line in lines:
            print(line.strip())
except FileNotFoundError:
    print("One or more files do not exist.")
```

### Example 6: Handle errors gracefully using try-except blocks

```python
import linecache

# Specify the path to a file that might not exist
file_path = '/path/to/nonexistent_file.txt'

try:
    # Attempt to retrieve a line from the non-existent file
    line_content = linecache.getline(file_path, 1)
    
    print(f"Line 1 in '{file_path}':")
    print(line_content.strip())
except FileNotFoundError as e:
    print(f"An error occurred: {e}")
```

### Example 7: Store and retrieve lines in a context manager

```python
import linecache

class LineCacheManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lines = None

    def load_lines(self):
        with open(self.file_path, 'r') as file:
            self.lines = file.readlines()

    def get_line(self, line_number):
        if self.lines is None:
            self.load_lines()
        
        return self.lines[line_number - 1].strip()

# Usage
manager = LineCacheManager('/path/to/your/file.txt')
try:
    line_content = manager.get_line(5)
    print(f"Line 5 in '{file_path}':")
    print(line_content.strip())
except IndexError:
    print("The specified line number is out of range.")
```

### Example 8: Use `linecache` with a list to store lines and process them

```python
import linecache

# List of file paths
file_paths = ['/path/to/file1.txt', '/path/to/file2.txt']

lines_data = []

try:
    # Retrieve all lines from each file and store in a list
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        lines_data.extend(lines)
    
    print("All lines processed:")
    for line in lines_data:
        print(line.strip())
except FileNotFoundError:
    print("One or more files do not exist.")
```

These examples cover various use cases of the `linecache` module, from basic retrieval to handling errors and storing results. Each example includes comments for clarity and best practices are followed throughout the code.
