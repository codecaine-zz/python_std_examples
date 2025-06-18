# glob - Unix style pathname pattern expansion
## Table of Contents

1. [Explanation of Examples:](#explanation-of-examples)



The `glob` module in Python provides a function called `glob()` that is used to expand Unix-style pathname patterns into a list of matching file names. This can be very useful for finding files based on specific naming conventions or patterns.

Below are comprehensive examples demonstrating various functionalities and use cases of the `glob` module:

```python
import glob
import os

# Example 1: Basic usage
# Find all .txt files in the current directory
print(glob.glob("*.txt"))

# Example 2: Search for files in a specific directory
# Find all .pdf files in the '/home/user/documents' directory
print(glob.glob("/home/user/documents/*.pdf"))

# Example 3: Use wildcards to match multiple file extensions
# Find all files with any of the following extensions: txt, pdf, docx
print(glob.glob("*.txt *.pdf *.docx"))

# Example 4: Find files with a specific prefix and suffix
# Find all files starting with 'report' and ending with '.doc'
print(glob.glob("report*.doc"))

# Example 5: Find files in multiple directories
# Use an absolute path to find all .py files in the home directory and its subdirectories
print(glob.glob("/home/user/**/*.py", recursive=True))

# Example 6: Find files with a specific pattern in their names
# Find all files containing 'summary' in their name
print(glob.glob("*summary*"))

# Example 7: Using shell-style wildcards
# Use ! to exclude specific patterns
print(glob.glob("*.txt !(*.log)"))  # Exclude .log files

# Example 8: Finding hidden files (files starting with a dot)
# Find all hidden files in the current directory
print(glob.glob(".?*"))

# Example 9: Using glob() with a function to filter results
def is_text_file(file_path):
    return file_path.endswith(".txt")

# Use list comprehension to find .txt files
for txt_file in [f for f in glob.iglob("*.txt") if is_text_file(f)]:
    print(txt_file)

# Example 10: Using glob() with a generator to handle large directories efficiently
def find_large_files(directory, size_threshold):
    for file_path in glob.iglob(f"{directory}/**/*", recursive=True):
        if os.path.getsize(file_path) > size_threshold:
            yield file_path

# Find all files larger than 10MB in the '/home/user/documents' directory
for large_file in find_large_files("/home/user/documents", 10 * 1024 * 1024):
    print(large_file)

```

### Explanation of Examples:

1. **Basic Usage**: This example demonstrates the simplest use case where you want to list all files with a specific extension in the current directory.

2. **Search in Specific Directory**: Shows how to search for files in a particular directory using an absolute path.

3. **Multiple File Extensions**: Demonstrates finding files with multiple extensions at once.

4. **Prefix and Suffix Patterns**: Searches for files that match both a prefix and a suffix.

5. **Recursive Search**: Uses `recursive=True` to find files in all subdirectories of a specified directory.

6. **Pattern Matching**: Uses wildcards like `*` and `?` to match filenames based on patterns.

7. **Excluding Files with Specific Patterns**: Demonstrates how to exclude certain files using the `!` wildcard.

8. **Hidden Files**: Finds files that start with a dot, which are typically hidden in Unix-like systems.

9. **Filtering Results**: Uses a filter function to apply custom logic for selecting matching files.

10. **Generator for Large Datasets**: Utilizes generators and `os.path.getsize()` to efficiently handle large datasets without loading everything into memory at once.

These examples cover a wide range of use cases for the `glob` module, demonstrating its flexibility and power in file path expansion.
