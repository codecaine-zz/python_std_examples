# shutil — High-level file operations

**Shutil Module Documentation**
=====================================

The `shutil` module provides high-level file operations, including copying, removing, and archiving files.

### Importing Modules
```python
import shutil
```

### Copying Files
-------------------

#### Using `shutil.copy()`
```python
# Copy a file from source to destination
source_file = 'source.txt'
destination_file = 'destination.txt'

try:
    # Attempt to copy the file
    shutil.copy(source_file, destination_file)
    print(f"File '{source_file}' copied to '{destination_file}'")
except FileNotFoundError as e:
    print(e)
```

#### Using `shutil.copy2()`
```python
# Copy a file from source to destination, preserving metadata
source_file = 'source.txt'
destination_file = 'destination.txt'

try:
    # Attempt to copy the file with metadata preservation
    shutil.copy2(source_file, destination_file)
    print(f"File '{source_file}' copied to '{destination_file}'")
except FileNotFoundError as e:
    print(e)
```

#### Using `shutil.copyfile()`
```python
# Copy a file from source to destination, preserving content and metadata
source_file = 'source.txt'
destination_file = 'destination.txt'

try:
    # Attempt to copy the file with preservation of content and metadata
    shutil.copyfile(source_file, destination_file)
    print(f"File '{source_file}' copied to '{destination_file}'")
except FileNotFoundError as e:
    print(e)
```

### Removing Files
-----------------

#### Using `shutil.rmtree()`
```python
# Remove a directory and all its contents
directory_path = '/path/to/directory'

try:
    # Attempt to remove the directory
    shutil.rmtree(directory_path)
    print(f"Directory '{directory_path}' removed")
except FileNotFoundError as e:
    print(e)
```

#### Using `shutil.remove()`
```python
# Remove a file
file_path = 'file.txt'

try:
    # Attempt to remove the file
    shutil.remove(file_path)
    print(f"File '{file_path}' removed")
except FileNotFoundError as e:
    print(e)
```

### Archiving Files
-----------------

#### Using `shutil.make_archive()`
```python
# Create an archive of a directory
directory_path = '/path/to/directory'
archive_name = 'archive.zip'

try:
    # Attempt to create the archive
    shutil.make_archive(archive_name, 'zip', directory_path)
    print(f"Archive '{archive_name}' created")
except FileNotFoundError as e:
    print(e)
```

#### Using `shutil.unpack_archive()`
```python
# Unpack an archive file
archive_file = '/path/to/archive.zip'
unpack_directory = '/path/to/unpack/directory'

try:
    # Attempt to unpack the archive
    shutil.unpack_archive(archive_file, unpack_directory)
    print(f"Archive '{archive_file}' unpacked in '{unpack_directory}'")
except FileNotFoundError as e:
    print(e)
```

### Miscellaneous Functions
---------------------------

#### Using `shutil.which()`
```python
# Get the path of an executable file or command
executable_name = 'python'

try:
    # Attempt to get the path of the executable
    executable_path = shutil.which(executable_name)
    if executable_path:
        print(f"Executable '{executable_name}' found at '{executable_path}'")
    else:
        print(f"Executable '{executable_name}' not found")
except FileNotFoundError as e:
    print(e)
```

#### Using `shutil.get_terminal_size()`
```python
# Get the terminal size
try:
    # Attempt to get the terminal size
    terminal_width, terminal_height = shutil.get_terminal_size()
    print(f"Terminal width: {terminal_width}, Terminal height: {terminal_height}")
except IOError as e:
    print(e)
```

### Example Usage
```python
if __name__ == '__main__':
    # Copy a file
    shutil.copy('source.txt', 'destination.txt')

    # Remove a file
    shutil.remove('file.txt')

    # Create an archive of a directory
    shutil.make_archive('archive', 'zip', '/path/to/directory')

    # Unpack an archive file
    shutil.unpack_archive('/path/to/archive.zip', '/path/to/unpack/directory')
```

Note: The `shutil` module provides a comprehensive set of high-level file operations, making it easier to work with files in Python. This documentation showcases the various functions and methods available in the `shutil` module, along with example usage and code snippets.
