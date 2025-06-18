# shutil - High-level file operations
## Table of Contents

1. [1. Copying Files and Directories](#1-copying-files-and-directories)
2. [2. Moving Files and Directories](#2-moving-files-and-directories)
3. [3. Deleting Files and Directories](#3-deleting-files-and-directories)
4. [4. Copying Files with Permissions](#4-copying-files-with-permissions)
5. [5. Archiving Files](#5-archiving-files)
6. [6. Compressing Files](#6-compressing-files)
7. [7. Listing Files in a Directory](#7-listing-files-in-a-directory)
8. [8. Getting File Information](#8-getting-file-information)
9. [9. Reading and Writing Files](#9-reading-and-writing-files)
10. [10. Making and Removing Directories](#10-making-and-removing-directories)



Certainly! Below are comprehensive code examples for various functionalities in the `shutil` module, which provides a high-level interface for common file operations in Python.

### 1. Copying Files and Directories

```python
import shutil
import os

# Example 1: Copy a single file to a new location
source_file = 'example.txt'
destination_file = 'example_copied.txt'

if os.path.exists(source_file):
    shutil.copy(source_file, destination_file)
    print(f"Copied {source_file} to {destination_file}")
else:
    print(f"Source file {source_file} does not exist.")

# Example 2: Copy all contents of a directory to another directory (not the directory itself)
source_dir = 'source_directory'
destination_dir = 'destination_directory'

if os.path.exists(source_dir):
    shutil.copytree(source_dir, destination_dir)
    print(f"Copied contents of {source_dir} to {destination_dir}")
else:
    print(f"Source directory {source_dir} does not exist.")
```

### 2. Moving Files and Directories

```python
import shutil
import os

# Example 1: Move a file to a new location
source_file = 'example.txt'
destination_file = 'example_moved.txt'

if os.path.exists(source_file):
    shutil.move(source_file, destination_file)
    print(f"Moved {source_file} to {destination_file}")
else:
    print(f"Source file {source_file} does not exist.")

# Example 2: Rename or move a directory (not the contents of the directory)
source_dir = 'source_directory'
new_name = 'moved_directory'

if os.path.exists(source_dir):
    shutil.move(source_dir, new_name)
    print(f"Renamed/Moved {source_dir} to {new_name}")
else:
    print(f"Source directory {source_dir} does not exist.")
```

### 3. Deleting Files and Directories

```python
import shutil
import os

# Example 1: Move a file to a new location
source_file = 'example.txt'
destination_file = 'example_moved.txt'

if os.path.exists(source_file):
    shutil.move(source_file, destination_file)
    print(f"Moved {source_file} to {destination_file}")
else:
    print(f"Error: {source_file} does not exist")

# Example 2: Rename or move a directory (not the contents of the directory)
source_dir = 'source_directory'
new_name = 'moved_directory'

if os.path.exists(source_dir):
    shutil.move(source_dir, new_name)
    print(f"Renamed/Moved {source_dir} to {new_name}")
else:
    print(f"Error: {source_dir} does not exist")
```

### 4. Copying Files with Permissions

```python
import shutil

# Example 1: Copy a file while preserving permissions
import shutil
import os

# Example 1: Copy a file while preserving permissions
source_file = 'example.txt'
destination_file = 'example_copied_with_permissions.txt'

if os.path.exists(source_file):
    shutil.copy2(source_file, destination_file)
    print(f"Copied {source_file} to {destination_file} with permissions")
else:
    print(f"Error: {source_file} does not exist")
```

### 5. Archiving Files

```python
import shutil
import tarfile

# Example 1: Create a .tar archive from a directory
import shutil
import tarfile
import os

# Example 1: Create a .tar archive from a directory
source_dir = 'source_directory'
archive_name = 'example.tar'

if os.path.exists(source_dir):
    with tarfile.open(archive_name, mode='w') as tar:
        tar.add(source_dir)
    print(f"Created {archive_name} from {source_dir}")
else:
    print(f"Error: {source_dir} does not exist")

# Example 2: Extract a .tar archive to a directory
archive_to_extract = 'example.tar'
extract_path = 'extracted_directory'

if os.path.exists(archive_to_extract) and os.path.getsize(archive_to_extract) > 0:
    with tarfile.open(archive_to_extract, mode='r') as tar:
        tar.extractall(path=extract_path)
    print(f"Extracted {archive_name} to {extract_path}")
else:
    print(f"Error: {archive_to_extract} does not exist or is empty")
```

### 6. Compressing Files

```python
import shutil
import gzip
import os

# Example 1: Create a .gz compressed file from a text file
file_to_compress = 'example.txt'
compressed_file = 'example.txt.gz'

if os.path.exists(file_to_compress):
    with open(file_to_compress, 'rb') as f_in:
        with gzip.open(compressed_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Compressed {file_to_compress} to {compressed_file}")
else:
    print(f"File {file_to_compress} does not exist")

# Example 2: Extract a .gz compressed file
file_to_extract = 'example.txt.gz'
extracted_file = 'extracted_example.txt'

if os.path.exists(file_to_extract):
    with gzip.open(file_to_extract, mode='rb') as f_in:
        with open(extracted_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Extracted {compressed_file} to {extracted_file}")
else:
    print(f"File {file_to_extract} does not exist")
```

### 7. Listing Files in a Directory

```python
import shutil
import os

# Example 1: List all files and directories in the current directory
current_dir = '.'
files_and_dirs = os.listdir(current_dir)
print(f"Files and Directories in {current_dir}: {files_and_dirs}")

# Example 2: Recursively list all files in a directory (including subdirectories)
directory_to_list = 'example_directory'

for root, dirs, files in os.walk(directory_to_list):
    for file in files:
        print(os.path.join(root, file))
```

### 8. Getting File Information

```python
import shutil
import os

# Example 1: Get the size of a file
file_path = 'example.txt'
try:
    size = os.path.getsize(file_path)
    print(f"Size of {file_path}: {size} bytes")
except FileNotFoundError:
    print(f"File {file_path} not found.")

# Example 2: Get information about the file like creation time, modification time, etc.
try:
    stat_info = os.stat(file_path)
    print(stat_info)
except FileNotFoundError:
    print(f"File {file_path} not found.")
```

### 9. Reading and Writing Files

```python
import shutil
import os

# Example 1: Read a file into memory as a string
file_to_read = 'example.txt'
if os.path.exists(file_to_read):
    with open(file_to_read, 'r') as f:
        content = f.read()
    print(f"Content of {file_to_read}: {content}")
else:
    print(f"File {file_to_read} does not exist.")

# Example 2: Write text to a file
file_to_write = 'example_written.txt'
text_to_write = "Hello, World!"
with open(file_to_write, 'w') as f:
    f.write(text_to_write)
print(f"Wrote '{text_to_write}' to {file_to_write}")
```

### 10. Making and Removing Directories

```python
import os
import shutil

# Example 1: Create a new directory
directory_name = 'new_directory'
os.makedirs(directory_name, exist_ok=True)
print(f"Created {directory_name}")

# Example 2: Remove an empty directory
empty_dir_to_remove = 'empty_directory'
shutil.rmtree(empty_dir_to_remove, ignore_errors=True)
print(f"Removed {empty_dir_to_remove}")
```

### Notes:

- **Permissions:** When copying or moving files, ensure that the user has the necessary permissions to perform these actions.
- **Error Handling:** Consider adding error handling to manage exceptions such as file not found errors or permission denied errors.
- **Security:** Be cautious with `shutil.move` and `shutil.rmtree` when dealing with user inputs or paths from untrusted sources.
- **Symbolic Links:** When copying directories, use the `symlinks` parameter in `shutil.copytree` to control whether to copy symbolic links as links or as the actual files they point to.
- **Path Validation:** Always validate and sanitize paths to avoid directory traversal vulnerabilities and other security issues.

These examples should provide a good starting point for using the `shutil` module in Python.
