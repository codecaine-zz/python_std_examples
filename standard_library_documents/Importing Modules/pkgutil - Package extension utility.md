# pkgutil — Package extension utility

**Package Extension Utility (pkgutil)**
======================================

The `pkgutil` module provides a way to access and manipulate Python packages.

### Module Documentation

```markdown
Module Name: pkgutil

Description:
------------

The pkgutil module provides a way to access and manipulate Python packages.
It allows you to list the contents of a package, get the package's metadata,
and check if a package is installed.

Functions
---------
- `find_modules(module_path)`: Find all modules in the given path that are part of an installed package.
- `load_module(module_path)`: Load a module from the given path.
- `list_packages(directory)`: List the packages found in the directory.
- `get_data(filename, directory=None)`: Get the data specified by filename from the package distribution if it exists.
- `get_spec(filename, directory=None)`: Return a specification for the distribution file that matches filename.
```

### Code Examples
-----------------

#### 1. Finding all modules in a package

```python
import pkgutil

# Find all modules in the current package
for module_info in pkgutil.iter_modules():
    print(f"Module Name: {module_info.name}")
    print(f"Module Path: {module_info.module_name}")
```

This will output all the modules in the current package.

#### 2. Loading a module

```python
import pkgutil

# Load a module from a file
try:
    module = pkgutil.load_module('example', 'path/to/example.py')
except ImportError as e:
    print(f"Failed to load module: {e}")
```

This will load the `example` module from the specified file.

#### 3. Listing packages in a directory

```python
import pkgutil

# List all packages in the current directory
for package_info in pkgutil.iter_packages():
    print(f"Package Name: {package_info.name}")
    print(f"Package Path: {package_info.path}")
```

This will output all the packages in the current directory.

#### 4. Getting data from a package

```python
import pkgutil

# Get data from a file
data = pkgutil.get_data('example', 'path/to/data.txt')
if data is not None:
    print(f"Data: {data.decode('utf-8')}")
else:
    print("No data found")
```

This will get the data specified by the `data.txt` file from the package distribution.

#### 5. Checking if a package is installed

```python
import pkgutil

# Check if a package is installed
try:
    pkgutil.get_spec('example')
except ImportError:
    print("Package 'example' not found")
```

This will check if the `example` package is installed and output whether it's found or not.

### Example Use Case
--------------------

Here's an example use case where we want to create a script that lists all modules in our current package:

```python
import pkgutil

def list_modules():
    for module_info in pkgutil.iter_modules():
        print(f"Module Name: {module_info.name}")
        print(f"Module Path: {module_info.module_name}")

if __name__ == "__main__":
    list_modules()
```

This script will output all the modules in our current package when run.
