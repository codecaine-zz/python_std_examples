# os.path - Common pathname manipulations
## Table of Contents

1. [Explanation:](#explanation)



The `os.path` module in Python provides a portable way of using operating system dependent functionality related to files and directories. Below are comprehensive examples demonstrating various functionalities of the `os.path` module, along with explanations for each example:

```python
import os

# Example 1: Joining paths
# Joining multiple parts into a single path
path_parts = ['home', 'user', 'documents', 'report.docx']
full_path = os.path.join(*path_parts)
print(f"Full Path: {full_path}")

# Example 2: Splitting paths
# Splitting the full path into directory and file components
dir_name, file_name = os.path.split(full_path)
print(f"Directory Name: {dir_name}")
print(f"File Name: {file_name}")

# Example 3: Checking if a file or directory exists
# Using os.path.exists() to check for existence of a file or directory
file_path = 'path/to/my_file.txt'
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")

# Example 4: Getting the last modification time of a file
# Using os.path.getmtime() to get the modification time of a file
import datetime
if os.path.exists(file_path):
    modification_time = os.path.getmtime(file_path)
    print(f"Last Modification Time: {datetime.datetime.fromtimestamp(modification_time)}")
else:
    print("File does not exist.")

# Example 5: Checking if a path is absolute
# Using os.path.isabs() to check if a path is absolute
absolute_path = os.path.abspath(full_path)
print(f"Is Absolute Path: {os.path.isabs(absolute_path)}")

# Example 6: Getting the current working directory
# Using os.getcwd() to get the current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

# Example 7: Changing the current working directory
# Using os.chdir() to change the current working directory
try:
    new_directory = 'path/to/new/directory'
    os.chdir(new_directory)
    print("Changed Current Directory.")
except FileNotFoundError:
    print("Directory does not exist.")

# Example 8: Listing all files in a directory
# Using os.listdir() to list all files and directories in a directory
if os.path.isdir(current_directory):
    for item in os.listdir(current_directory):
        print(item)
else:
    print("Path is not a directory.")

# Example 9: Checking if a path is a directory
# Using os.path.isdir() to check if a path is a directory
directory_path = 'path/to/my_directory'
if os.path.isdir(directory_path):
    print("This is a directory.")
else:
    print("This is not a directory.")

# Example 10: Getting the size of a file in bytes
# Using os.path.getsize() to get the size of a file
file_size = os.path.getsize(file_path)
print(f"File Size (bytes): {file_size}")

# Example 11: Creating a new directory
# Using os.makedirs() to create multiple directories
try:
    new_dir_path = 'path/to/new/directory'
    os.makedirs(new_dir_path, exist_ok=True)
    print("Directory created.")
except FileExistsError:
    print("Directory already exists.")

# Example 12: Removing an empty directory
# Using os.rmdir() to remove a non-empty directory if it is empty
try:
    dir_to_remove = 'path/to/directory'
    os.rmdir(dir_to_remove)
    print("Directory removed.")
except FileNotFoundError:
    print("Directory does not exist.")

# Example 13: Removing a file
# Using os.remove() to delete a file
try:
    file_to_remove = 'path/to/my_file.txt'
    os.remove(file_to_remove)
    print("File deleted.")
except FileNotFoundError:
    print("File does not exist.")

# Example 14: Renaming a directory or file
# Using os.rename() to rename a file or directory
new_name = 'new_name_for_my_file.docx'
os.rename(file_path, new_name)
print(f"Renamed file from {file_path} to {new_name}")

# Example 15: Getting the absolute path of a symbolic link
# Using os.path.realpath() for resolving symbolic links
real_path = os.path.realpath('path/to/symbolic_link')
print(f"Real Path: {real_path}")

# Example 16: Checking if two paths point to the same file or directory
# Using os.path.samefile() to compare paths
other_file_path = 'path/to/another_file.txt'
if os.path.samefile(file_path, other_file_path):
    print("Both paths point to the same file.")
else:
    print("Paths do not point to the same file.")

# Example 17: Getting the extension of a path
# Using os.path.splitext() to get the extension of a file
base_name, extension = os.path.splitext(file_path)
print(f"Base Name: {base_name}")
print(f"Extension: {extension}")

# Example 18: Removing an empty directory recursively (for directories with contents)
# Note: This will only remove empty directories. For non-empty directories, use shutil.rmtree()
dir_to_remove_recursive = 'path/to/directory_with_contents'
os.rmdir(dir_to_remove_recursive)  # This will raise an error as it's not empty

# Example 19: Creating a symbolic link
# Using os.symlink() to create a symbolic link
try:
    symlink_path = 'path/to/symlink'
    source_file = 'path/to/source/file.txt'
    os.symlink(source_file, symlink_path)
    print("Symbolic Link created.")
except FileExistsError:
    print("Symlink already exists.")

# Example 20: Checking if a path is a symbolic link
# Using os.path.islink() to check if a path is a symbolic link
if os.path.islink(symlink_path):
    print("This is a symbolic link.")
else:
    print("This is not a symbolic link.")

```

### Explanation:

- **Path Joining and Splitting**: Demonstrates how to join multiple paths into one using `os.path.join()` and split them back into directory and file components with `os.path.split()`.
  
- **File Existence Check**: Shows how to check if a file or directory exists using `os.path.exists()`.

- **Last Modification Time**: Uses `os.path.getmtime()` to get the last modification time of a file, which is then converted to a human-readable format using `datetime.datetime.fromtimestamp()`.

- **Path Absoluteity and Current Directory Manipulation**: Demonstrates how to check if a path is absolute with `os.path.isabs()`, change the current directory with `os.chdir()`, get the current working directory with `os.getcwd()`, and more.

- **File and Directory Management**: Includes operations like listing files in a directory, checking if a path is a directory or file, getting the size of a file, creating/removing directories, and managing symbolic links.

Each example includes error handling for cases where the paths might not exist, providing clear output to verify the results.
