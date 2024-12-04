# shutil - High-level file operations

Certainly! Below are comprehensive code examples for various functionalities in the `shutil` module, which provides a high-level interface for common file operations in Python.

### 1. Copying Files and Directories

```python
import shutil

# Example 1: Copy a single file to a new location
source_file = 'example.txt'
destination_file = 'example_copied.txt'

shutil.copy(source_file, destination_file)
print(f"Copied {source_file} to {destination_file}")

# Example 2: Copy all contents of a directory to another directory (not the directory itself)
source_dir = 'source_directory'
destination_dir = 'destination_directory'

shutil.copytree(source_dir, destination_dir)
print(f"Copied contents of {source_dir} to {destination_dir}")
```

### 2. Moving Files and Directories

```python
import shutil

# Example 1: Move a file to a new location
source_file = 'example.txt'
destination_file = 'example_moved.txt'

shutil.move(source_file, destination_file)
print(f"Moved {source_file} to {destination_file}")

# Example 2: Rename or move a directory (not the contents of the directory)
source_dir = 'source_directory'
new_name = 'moved_directory'

shutil.move(source_dir, new_name)
print(f"Renamed/Moved {source_dir} to {new_name}")
```

### 3. Deleting Files and Directories

```python
import shutil

# Example 1: Delete a single file
file_to_delete = 'example.txt'
shutil.os.remove(file_to_delete)
print(f"Deleted {file_to_delete}")

# Example 2: Recursively delete an entire directory (including all contents)
directory_to_delete = 'destination_directory'

shutil.rmtree(directory_to_delete)
print(f"Recursively deleted {directory_to_delete}")
```

### 4. Copying Files with Permissions

```python
import shutil

# Example 1: Copy a file while preserving permissions
source_file = 'example.txt'
destination_file = 'example_copied_with_permissions.txt'

shutil.copy2(source_file, destination_file)
print(f"Copied {source_file} to {destination_file} with permissions")
```

### 5. Archiving Files

```python
import shutil
import tarfile

# Example 1: Create a .tar archive from a directory
source_dir = 'source_directory'
archive_name = 'example.tar'

with tarfile.open(archive_name, mode='w') as tar:
    tar.add(source_dir)
print(f"Created {archive_name} from {source_dir}")

# Example 2: Extract a .tar archive to a directory
archive_to_extract = 'example.tar'
extract_path = 'extracted_directory'

with tarfile.open(archive_to_extract, mode='r') as tar:
    tar.extractall(path=extract_path)
print(f"Extracted {archive_name} to {extract_path}")
```

### 6. Compressing Files

```python
import shutil
import gzip

# Example 1: Create a .gz compressed file from a text file
file_to_compress = 'example.txt'
compressed_file = 'example.txt.gz'

with open(file_to_compress, 'rb') as f_in:
    with gzip.open(compressed_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
print(f"Compressed {file_to_compress} to {compressed_file}")

# Example 2: Extract a .gz compressed file
file_to_extract = 'example.txt.gz'
extracted_file = 'extracted_example.txt'

with gzip.open(file_to_extract, mode='rb') as f_in:
    with open(extracted_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
print(f"Extracted {compressed_file} to {extracted_file}")
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
size = os.path.getsize(file_path)
print(f"Size of {file_path}: {size} bytes")

# Example 2: Get information about the file like creation time, modification time, etc.
stat_info = os.stat(file_path)
print(stat_info)
```

### 9. Reading and Writing Files

```python
import shutil

# Example 1: Read a file into memory as a string
file_to_read = 'example.txt'
with open(file_to_read, 'r') as f:
    content = f.read()
print(f"Content of {file_to_read}: {content}")

# Example 2: Write text to a file
file_to_write = 'example_written.txt'
text_to_write = "Hello, World!"
with open(file_to_write, 'w') as f:
    f.write(text_to_write)
print(f"Wrote '{text_to_write}' to {file_to_write}")
```

### 10. Making and Removing Directories

```python
import shutil

# Example 1: Create a new directory
directory_name = 'new_directory'
shutil.os.makedirs(directory_name)
print(f"Created {directory_name}")

# Example 2: Remove an empty directory
empty_dir_to_remove = 'empty_directory'
shutil.os.rmdir(empty_dir_to_remove)
print(f"Removed {empty_dir_to_remove}")
```

### Notes:

- **Permissions:** When copying or moving files, ensure that the user has the necessary permissions to perform these actions.
- **Error Handling:** Consider adding error handling to manage exceptions such as file not found errors or permission denied errors.
- **Security:** Be cautious with `shutil.move` and `shutil.rmtree` when dealing with user inputs or paths from untrusted sources.

These examples should provide a good starting point for using the `shutil` module in Python.
