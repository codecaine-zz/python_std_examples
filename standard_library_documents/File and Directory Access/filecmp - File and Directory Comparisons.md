# filecmp - File and Directory Comparisons
## Table of Contents

1. [1. `cmp`](#1-cmp)
2. [2. `cmpfiles`](#2-cmpfiles)
3. [3. `dircmp`](#3-dircmp)
4. [4. `filecmp.dircmpobj`](#4-filecmpdircmpobj)
5. [5. `subprocess.run`](#5-subprocessrun)
6. [6. `filecmp.cmpfiles() with patterns`](#6-filecmpcmpfiles-with-patterns)
7. [7. `filecmp.cmp() with custom comparison logic`](#7-filecmpcmp-with-custom-comparison-logic)
8. [8. `filecmp.cmp() with binary comparison`](#8-filecmpcmp-with-binary-comparison)
9. [9. `filecmp.dircmp()` with ignore patterns](#9-filecmpdircmp-with-ignore-patterns)
10. [10. `filecmp.cmp() with shallow comparison`](#10-filecmpcmp-with-shallow-comparison)



The `filecmp` module in Python provides utilities to compare files or directories for equality, modification times, and more. Below are comprehensive examples of how to use each function and class in the `filecmp` module.

### 1. `cmp`
The `cmp()` function compares two files and returns:
- `0` if both files are identical.
- A negative integer if the first file is older than the second file.
- A positive integer otherwise.

```python
import filecmp

# Example usage
filecmp.cmp('source.txt', 'destination.txt')
```

### 2. `cmpfiles`
The `cmpfiles()` function compares two sets of files and returns:
- Three lists: `[same_files, different_files, missing_files]`.

```python
import filecmp

# Example usage
common, diff, miss = filecmp.cmpfiles('source_dir', 'destination_dir', ['file1.txt', 'file2.txt'])
print("Same Files:", common)
print("Different Files:", diff)
print("Missing Files:", miss)
```

### 3. `dircmp`
The `dircmp()` function compares two directories and provides a comprehensive comparison of their contents.

```python
import filecmp

# Example usage
dir_cmp = filecmp.dircmp('source_dir', 'destination_dir')
print("Common files:", dir_cmp.common)
print("Different files:", dir_cmp.diff_files)
print("Common subdirectories:", dir_cmp.common_dirs)
print("Subdirectory of source but not destination:", dir_cmp.left_only)
print("Subdirectory of destination but not source:", dir_cmp.right_only)

# Optionally, walk through directories
for root, dirs, files in os.walk(dir_cmp.left):
    for file in files:
        rel_path = os.path.join(root, file)
        print("File from source:", rel_path)

for root, dirs, files in os.walk(dir_cmp.right):
    for file in files:
        rel_path = os.path.join(root, file)
        print("File from destination:", rel_path)
```

### 4. `filecmp.dircmpobj`
The `dircmp()` function returns an instance of `dircmpobj` which can be used to compare directories and their contents.

```python
import filecmp

# Example usage
dir_cmp = filecmp.dircmp('source_dir', 'destination_dir')

# Print detailed information about the comparison
print(dir_cmp.left, "and", dir_cmp.right)
print("Common files:", dir_cmp.common)
print("Different files:", dir_cmp.diff_files)
print("Common subdirectories:", dir_cmp.common_dirs)

# Walk through directories using the dircmpobj
for root, dirs, files in dir_cmp.walk():
    for file in files:
        print(f"File found at: {os.path.join(root, file)}")
```

### 5. `subprocess.run`
The `subprocess.run()` function can be used to compare directories using the external command `diff`.

```python
import subprocess

# Example usage
result = subprocess.run(['diff', 'source_dir', 'destination_dir'], capture_output=True)
print("Diff Output:")
print(result.stdout.decode('utf-8'))
```

### 6. `filecmp.cmpfiles() with patterns`
You can specify file patterns to include or exclude during comparison.

```python
import filecmp

# Example usage
common, diff, miss = filecmp.cmpfiles('source_dir', 'destination_dir',
                                        ['*.txt'], ['.gitignore'])
print("Common files:", common)
print("Different files:", diff)
print("Missing files:", miss)
```

### 7. `filecmp.cmp() with custom comparison logic`
You can define a custom function for comparison using the `use_cse` parameter.

```python
import filecmp

def custom_cmp(file1, file2):
    # Custom comparison logic here
    return True  # Return False if files are different, otherwise True

# Example usage
filecmp.cmp('source.txt', 'destination.txt', use_cse=custom_cmp)
```

### 8. `filecmp.cmp() with binary comparison`
If you need to compare files for content equality without considering file attributes like size and modification time, set `shallow` to `False`.

```python
import filecmp

# Example usage
result = filecmp.cmp('source.txt', 'destination.txt', use_cse=False)
print("Files are", "equal" if result else "different")
```

### 9. `filecmp.dircmp()` with ignore patterns
You can specify patterns to be ignored during the comparison.

```python
import filecmp

# Example usage
dir_cmp = filecmp.dircmp('source_dir', 'destination_dir',
                           ['*.txt'], ['.gitignore'])
print("Common files:", dir_cmp.common)
print("Different files:", dir_cmp.diff_files)
print("Common subdirectories:", dir_cmp.common_dirs)
```

### 10. `filecmp.cmp() with shallow comparison`
If you only want to compare the file sizes and modification times without opening the files, set `shallow` to `True`.

```python
import filecmp

# Example usage
result = filecmp.cmp('source.txt', 'destination.txt', use_cse=False, shallow=True)
print("Files are", "equal" if result else "different")
```

These examples demonstrate various ways to use the `filecmp` module in Python for comparing files and directories. Each example is well-documented and includes comments explaining the functionality.
