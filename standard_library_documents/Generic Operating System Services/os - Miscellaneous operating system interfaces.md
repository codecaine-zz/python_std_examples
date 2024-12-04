# os — Miscellaneous operating system interfaces

**os Module Examples**
=====================

The `os` module provides a way of using operating system dependent functionality.

### 1. Checking if a file exists
```python
import os

# Check if a file exists
def check_file_exists(file_path):
    """
    Checks if a file exists at the specified path.
    
    Args:
        file_path (str): The path to the file to check.
    
    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(file_path)

# Example usage
file_path = "/path/to/your/file.txt"
if check_file_exists(file_path):
    print(f"The file {file_path} exists.")
else:
    print(f"The file {file_path} does not exist.")
```

### 2. Getting the current working directory
```python
import os

# Get the current working directory
def get_current_directory():
    """
    Gets the path of the current working directory.
    
    Returns:
        str: The path of the current working directory.
    """
    return os.getcwd()

# Example usage
print(get_current_directory())
```

### 3. Changing the current working directory
```python
import os

# Change the current working directory
def change_directory(directory_path):
    """
    Changes the current working directory to the specified path.
    
    Args:
        directory_path (str): The path of the new working directory.
    """
    os.chdir(directory_path)

# Example usage
new_dir = "/path/to/new/directory"
change_directory(new_dir)
print(os.getcwd())  # prints the new directory
```

### 4. Listing files and directories in a given directory
```python
import os

# List files and directories in a given directory
def list_files_and_directories(directory_path):
    """
    Lists all files and directories in the specified path.
    
    Args:
        directory_path (str): The path of the directory to list.
    
    Returns:
        list: A list of files and directories in the specified path.
    """
    return os.listdir(directory_path)

# Example usage
dir_path = "/path/to/your/directory"
files_and_dirs = list_files_and_directories(dir_path)
print(files_and_dirs)  # prints a list of files and directories
```

### 5. Creating a new directory
```python
import os

# Create a new directory
def create_directory(directory_name):
    """
    Creates a new directory with the specified name.
    
    Args:
        directory_name (str): The name of the new directory.
    
    Returns:
        bool: True if the directory was created, False otherwise.
    """
    try:
        os.mkdir(directory_name)
        return True
    except FileExistsError:
        print(f"The directory {directory_name} already exists.")
        return False

# Example usage
dir_name = "new_directory"
if create_directory(dir_name):
    print(f"Directory {dir_name} created successfully.")
else:
    print(f"Failed to create directory {dir_name}.")
```

### 6. Deleting a file or directory
```python
import os

# Delete a file or directory
def delete_file_or_directory(file_or_dir_path):
    """
    Deletes the specified file or directory.
    
    Args:
        file_or_dir_path (str): The path of the file or directory to delete.
    
    Returns:
        bool: True if the file or directory was deleted, False otherwise.
    """
    try:
        os.remove(file_or_dir_path)
        return True
    except FileNotFoundError:
        print(f"The file {file_or_dir_path} does not exist.")
        return False

# Example usage
file_path = "/path/to/your/file.txt"
if delete_file_or_directory(file_path):
    print(f"File {file_path} deleted successfully.")
else:
    print(f"Failed to delete file {file_path}.")
```

### 7. Getting the absolute path of a given path
```python
import os

# Get the absolute path of a given path
def get_absolute_path(path):
    """
    Gets the absolute path of the specified path.
    
    Args:
        path (str): The path to get the absolute path for.
    
    Returns:
        str: The absolute path of the specified path.
    """
    return os.path.abspath(path)

# Example usage
file_path = "/path/to/your/file.txt"
absolute_path = get_absolute_path(file_path)
print(absolute_path)  # prints the absolute path
```

### 8. Getting the relative path of a given path
```python
import os

# Get the relative path of a given path
def get_relative_path(path, base_dir):
    """
    Gets the relative path of the specified path from the given base directory.
    
    Args:
        path (str): The path to get the relative path for.
        base_dir (str): The base directory to compare with.
    
    Returns:
        str: The relative path of the specified path from the given base directory.
    """
    return os.path.relpath(path, base_dir)

# Example usage
base_dir = "/path/to/base/directory"
file_path = "/path/to/your/file.txt"
relative_path = get_relative_path(file_path, base_dir)
print(relative_path)  # prints the relative path
```

### 9. Getting the directory name of a given path
```python
import os

# Get the directory name of a given path
def get_directory_name(path):
    """
    Gets the directory name of the specified path.
    
    Args:
        path (str): The path to get the directory name for.
    
    Returns:
        str: The directory name of the specified path.
    """
    return os.path.dirname(path)

# Example usage
file_path = "/path/to/your/file.txt"
dir_name = get_directory_name(file_path)
print(dir_name)  # prints the directory name
```

### 10. Getting the file name of a given path
```python
import os

# Get the file name of a given path
def get_file_name(path):
    """
    Gets the file name of the specified path.
    
    Args:
        path (str): The path to get the file name for.
    
    Returns:
        str: The file name of the specified path.
    """
    return os.path.basename(path)

# Example usage
file_path = "/path/to/your/file.txt"
file_name = get_file_name(file_path)
print(file_name)  # prints the file name
```
