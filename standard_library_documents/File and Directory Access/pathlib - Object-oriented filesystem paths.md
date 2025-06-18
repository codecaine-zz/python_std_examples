# pathlib - Object-oriented filesystem paths
## Table of Contents

1. [Explanation:](#explanation)



Below are comprehensive examples of how to use each functionality provided by the `pathlib` module in Python 3.12. Each example is well-documented with comments explaining each step.

```python
from pathlib import Path

# Example 1: Create a new Path object for a file or directory
file_path = Path("example.txt")
directory_path = Path("documents")

print(file_path)    # Output: PosixPath('example.txt')
print(directory_path)  # Output: PosixPath('documents')

# Example 2: Check if the path exists and is a file or directory
if file_path.exists():
    print("File exists:", file_path)
else:
    print("File does not exist")

if directory_path.exists() and directory_path.is_dir():
    print("Directory exists:", directory_path)
else:
    print("Directory does not exist")

# Example 3: Create a new directory if it doesn't exist
new_directory = Path("new_directory")
if not new_directory.exists():
    new_directory.mkdir(parents=True, exist_ok=True)

print("New directory created:", new_directory)

# Example 4: Move or rename a file or directory
original_file_path = Path("example.txt")
target_file_path = Path("backup/example_backup.txt")

if original_file_path.exists():
    target_file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure target directory exists
    original_file_path.rename(target_file_path)
    print("File moved to:", target_file_path)
else:
    print("File does not exist")

# Example 5: List all files and directories in a directory
if directory_path.exists():
    for item in directory_path.iterdir():
        if item.is_file():
            print(f"File: {item}")
        elif item.is_dir():
            print(f"Directory: {item}")

# Example 6: Get the absolute path of a relative path
relative_path = Path("example.txt")
absolute_path = relative_path.resolve()
print("Absolute path:", absolute_path)

# Example 7: Check if a path is an absolute path
if absolute_path.is_absolute():
    print("Path is absolute.")
else:
    print("Path is not absolute.")

# Example 8: Get the name of the file or directory without extension
file_name_without_extension = file_path.stem
print("File name without extension:", file_name_without_extension)

# Example 9: Get the extension of a file
file_extension = file_path.suffix
print("File extension:", file_extension)

# Example 10: Walk through directories and files recursively
if directory_path.exists():
    for item in directory_path.rglob("*"):
        if item.is_file():
            print(f"File found: {item}")

# Example 11: Normalize a path by resolving all symbolic links and redundant references
normalized_path = Path("example.txt")
real_path = normalized_path.resolve()
print("Normalized and resolved path:", real_path)

# Example 12: Join paths to create a new path object
combined_path = file_path.parent / "backup" / "example_backup.txt"
print("Combined path:", combined_path)
```

### Explanation:

- **Path Objects**: `Path` objects are used to represent filesystem paths in an abstract way.
- **Existence Check**: Methods like `exists()` and `is_dir()` check if a path exists and its type.
- **Directory Creation**: The `mkdir()` method creates a new directory. The `parents=True` parameter ensures parent directories are created, and `exist_ok=True` prevents raising an error if the directory already exists.
- **File Movement**: The `rename()` method moves or renames a file or directory.
- **Directory Contents**: The `iterdir()` method lists all items in a directory, including files and subdirectories.
- **Absolute Path Resolution**: The `resolve()` method returns the absolute path by resolving symbolic links and redundant references.
- **Path Normalization**: The `normpath()` method normalizes a path by removing redundant components.
- **Path Joining**: The `/` operator is used to join paths, creating a new `Path` object.

These examples cover a wide range of functionalities provided by the `pathlib` module, demonstrating how to work with file and directory paths in Python.
