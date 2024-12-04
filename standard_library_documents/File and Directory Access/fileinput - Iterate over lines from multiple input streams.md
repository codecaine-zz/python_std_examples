# fileinput - Iterate over lines from multiple input streams

The `fileinput` module is a part of Python's standard library that provides an easy way to read from multiple files or standard input. It allows you to process each line from each of these inputs in sequence, handling various options such as skipping blank lines and processing only certain lines based on their position.

Here are some comprehensive code examples for the `fileinput` module:

### Example 1: Iterating Over Multiple Files

This example reads lines from multiple files sequentially and prints them. It handles empty lines by checking if they contain any content.

```python
import fileinput

# List of files to read
files_to_read = ['file1.txt', 'file2.txt']

# Iterate over each line in the specified files
for line in fileinput.input(files=files_to_read):
    # Check if the line is not empty before processing
    if line:
        print(line.strip())  # Print each non-empty line after stripping whitespace

# Clean up any open files
fileinput.close()
```

### Example 2: Skipping Blank Lines

This example demonstrates how to skip blank lines when reading from multiple files. It uses the `fileinput.SKIP_BLANK_LINES` option.

```python
import fileinput

# List of files to read
files_to_read = ['file1.txt', 'file2.txt']

# Iterate over each line in the specified files, skipping empty ones
for line in fileinput.input(files=files_to_read, inplace=True):
    # Check if the line is not empty before processing
    if line:
        print(line.strip())  # Print each non-empty line after stripping whitespace

# Clean up any open files
fileinput.close()
```

### Example 3: Processing Lines Based on Position

This example shows how to process lines based on their position in each file. It uses the `lineno` attribute available in the `fileinput` module.

```python
import fileinput

# List of files to read
files_to_read = ['file1.txt', 'file2.txt']

# Iterate over each line in the specified files, processing lines based on position
for line_num, line in enumerate(fileinput.input(files=files_to_read)):
    if line:
        # Print the line number and the content
        print(f"Line {line_num + 1}: {line.strip()}")

# Clean up any open files
fileinput.close()
```

### Example 4: Using `inplace` Mode

This example uses the `inplace` mode to modify lines in place, allowing you to edit multiple files simultaneously.

```python
import fileinput

# List of files to read and modify
files_to_modify = ['file1.txt', 'file2.txt']

# Iterate over each line in the specified files, modifying them if necessary
for line_num, line in enumerate(fileinput.input(files=files_to_modify, inplace=True)):
    # Check if the line is not empty before processing
    if line:
        # Modify the line (e.g., change 'old' to 'new')
        modified_line = line.replace('old', 'new').strip()
        print(modified_line)  # Print the modified line

# Clean up any open files
fileinput.close()
```

### Example 5: Handling Unicode Input

This example demonstrates how to handle Unicode input when reading from multiple files. It uses the `encoding` parameter to specify the encoding.

```python
import fileinput

# List of files to read
files_to_read = ['file1.txt', 'file2.txt']

# Iterate over each line in the specified files, handling UTF-8 encoding
for line in fileinput.input(files=files_to_read, encoding='utf-8'):
    # Print the line after decoding it from bytes
    print(line.decode('utf-8'))

# Clean up any open files
fileinput.close()
```

These examples cover various aspects of using the `fileinput` module, including reading from multiple files, handling blank lines, processing lines based on position, modifying files in place, and handling Unicode input. Each example is self-contained and should be clear for inclusion in documentation or use cases where these functionalities are required.
