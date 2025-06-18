# os - Miscellaneous operating system interfaces
## Table of Contents

1. [1. Accessing Environment Variables](#1-accessing-environment-variables)
2. [2. Changing the Current Working Directory](#2-changing-the-current-working-directory)
3. [3. Listing Directory Contents](#3-listing-directory-contents)
4. [4. Creating a New Directory](#4-creating-a-new-directory)
5. [5. Removing a Directory](#5-removing-a-directory)
6. [6. Executing a Command](#6-executing-a-command)
7. [7. Getting Current Working Directory](#7-getting-current-working-directory)
8. [8. Checking if a File or Directory Exists](#8-checking-if-a-file-or-directory-exists)
9. [9. Getting File or Directory Information](#9-getting-file-or-directory-information)
10. [10. Making a Directory with Permissions](#10-making-a-directory-with-permissions)



The `os` module in Python provides a portable way of using operating system dependent functionality, such as reading or writing to the filesystem, executing programs, and accessing environment variables. Below are comprehensive examples demonstrating various functionalities of the `os` module.

### 1. Accessing Environment Variables

```python
import os

def print_environment_variables():
    """
    This function prints all environment variables.
    """
    for name, value in os.environ.items():
        print(f"{name}: {value}")

print_environment_variables()
```

### 2. Changing the Current Working Directory

```python
import os

def change_directory(path):
    """
    This function changes the current working directory to the specified path.
    
    Args:
    path (str): The directory path to which the current working directory should be changed.
    """
    try:
        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print("Directory not found.")

change_directory('/path/to/directory')
```

### 3. Listing Directory Contents

```python
import os

def list_directory_contents(directory):
    """
    This function lists all contents of the specified directory, including files and subdirectories.
    
    Args:
    directory (str): The path to the directory whose contents should be listed.
    """
    try:
        contents = os.listdir(directory)
        print(f"Contents of {directory}:")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Directory not found.")

list_directory_contents('/path/to/directory')
```

### 4. Creating a New Directory

```python
import os

def create_directory(path):
    """
    This function creates a new directory at the specified path.
    
    Args:
    path (str): The path where the new directory should be created.
    """
    try:
        os.makedirs(path)
        print(f"Directory {path} created successfully.")
    except FileExistsError:
        print("Directory already exists.")

create_directory('/path/to/new/directory')
```

### 5. Removing a Directory

```python
import os

def remove_directory(directory):
    """
    This function removes the specified directory.
    
    Args:
    directory (str): The path to the directory that should be removed.
    """
    try:
        os.rmdir(directory)
        print(f"Directory {directory} removed successfully.")
    except FileNotFoundError:
        print("Directory not found.")
    except OSError as e:
        if e.errno == 30:  # Directory is not empty
            print("Directory is not empty. Please remove all contents first.")
        else:
            print(f"An error occurred: {e}")

remove_directory('/path/to/directory')
```

### 6. Executing a Command

```python
import os

def execute_command(command):
    """
    This function executes the specified command in a shell.
    
    Args:
    command (str): The command to be executed.
    """
    try:
        result = os.system(command)
        print(f"Command executed with result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

execute_command('ls -l')
```

### 7. Getting Current Working Directory

```python
import os

def get_current_working_directory():
    """
    This function returns the current working directory.
    """
    return os.getcwd()

current_dir = get_current_working_directory()
print(f"Current working directory: {current_dir}")
```

### 8. Checking if a File or Directory Exists

```python
import os

def check_file_or_directory_exists(path):
    """
    This function checks if a file or directory exists at the specified path.
    
    Args:
    path (str): The path to the file or directory.
    
    Returns:
    bool: True if it exists, False otherwise.
    """
    return os.path.exists(path)

exists = check_file_or_directory_exists('/path/to/file')
print(f"File/Directory exists: {exists}")
```

### 9. Getting File or Directory Information

```python
import os

def get_file_info(file_path):
    """
    This function retrieves information about a file or directory.
    
    Args:
    file_path (str): The path to the file or directory.
    
    Returns:
    dict: A dictionary containing various attributes of the file or directory.
    """
    try:
        info = os.stat(file_path)
        return {
            'mode': oct(info.st_mode)[2:],  # Convert mode to octal
            'size': info.st_size,          # File size in bytes
            'last_modified': info.st_mtime   # Last modification time
        }
    except FileNotFoundError:
        print("File not found.")
        return {}

file_info = get_file_info('/path/to/file')
print(file_info)
```

### 10. Making a Directory with Permissions

```python
import os

def create_directory_with_permissions(path, mode):
    """
    This function creates a new directory at the specified path with the given permissions.
    
    Args:
    path (str): The path where the new directory should be created.
    mode (int): The permission bits for the directory (e.g., 0o755).
    """
    try:
        os.makedirs(path, mode=mode)
        print(f"Directory {path} created successfully with permissions {oct(mode)[2:]}")
    except FileExistsError:
        print("Directory already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

create_directory_with_permissions('/path/to/new/directory', 0o755)
```

These examples demonstrate various functionalities of the `os` module, covering common tasks such as environment variable manipulation, directory operations, file system navigation, and command execution. Each function is documented with a docstring that explains its purpose, arguments, and return values.
