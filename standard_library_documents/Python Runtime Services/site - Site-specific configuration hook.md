# site - Site-specific configuration hook
## Table of Contents

1. [1. `site.addsitedir(path)`](#1-siteaddsitedirpath)
2. [2. `site.getsitepackages()`](#2-sitegetsitepackages)
3. [3. `site.getusersitepackages()`](#3-sitegetusersitepackages)
4. [4. `site.getsitecustomize()`](#4-sitegetsitecustomize)
5. [5. `site.removesitedir(path)`](#5-siteremovesitedirpath)
6. [6. `site.setusersitepackages(True | False)`](#6-sitesetusersitepackagestrue-false)
7. [7. `site.clearsitepackages()`](#7-siteclearsitepackages)
8. [8. `site.addsitedir(path, setpath=True)`](#8-siteaddsitedirpath-setpathtrue)
9. [9. `site.removesitedir(path, unsetsitepackages=False)`](#9-siteremovesitedirpath-unsetsitepackagesfalse)
10. [10. `site.addsitedir(path, setpath=True)`](#10-siteaddsitedirpath-setpathtrue)



The `site` module in Python is used to customize the behavior of Python's import system, especially when it comes to loading modules from a directory outside the standard installation path. This can be useful for various purposes, such as extending the Python environment with additional libraries or modules.

Here are comprehensive code examples for each functionality provided by the `site` module:

### 1. `site.addsitedir(path)`
- **Purpose**: Adds a directory to the list of directories that Python searches for site-specific modules.
- **Description**: This function is used to add an additional directory to the Python path, allowing you to import modules from that directory without changing the system-wide PYTHONPATH.

```python
import site

# Add a custom site directory to the Python path
site.addsitedir('/path/to/custom/site-packages')

# Now, you can import modules from this directory
try:
    import my_custom_module
except ImportError as e:
    print(f"Module not found: {e}")
```

### 2. `site.getsitepackages()`
- **Purpose**: Returns a list of directories where Python will look for site-specific packages.
- **Description**: This function is useful for determining where additional libraries are installed and can be used to dynamically adjust paths in scripts or IDEs.

```python
import site

# Get the list of site-packages directories
site_packages_directories = site.getsitepackages()

print("Site-packages directories:", site_packages_directories)
```

### 3. `site.getusersitepackages()`
- **Purpose**: Returns a directory where Python will look for site-specific packages installed by the user.
- **Description**: This function is useful for accessing the directory where user-installed packages are stored, which can be used to dynamically find or manage user-specific modules.

```python
import site

# Get the path to the user's site-packages directory
user_site_packages = site.getusersitepackages()

print("User site-packages directory:", user_site_packages)
```

### 4. `site.getsitecustomize()`
- **Purpose**: Returns the filename of the file that contains customization functions for the import system.
- **Description**: This function is useful for implementing custom behavior in module loading, such as adding hooks for specific types of modules or modifying the order in which modules are imported.

```python
import site

# Get the path to the sitecustomize.py file
site_customize_path = site.getsitecustomize()

print("Sitecustomize file:", site_customize_path)
```

### 5. `site.removesitedir(path)`
- **Purpose**: Removes a directory from the list of directories that Python searches for site-specific modules.
- **Description**: This function is used to remove an additional directory from the Python path, allowing you to revert the change made by `addsitedir`.

```python
import site

# Add a custom site directory
site.addsitedir('/path/to/custom/site-packages')

# Remove the custom site directory
site.removesitedir('/path/to/custom/site-packages')
```

### 6. `site.setusersitepackages(True | False)`
- **Purpose**: Controls whether Python will look for user-specific packages.
- **Description**: This function is used to enable or disable the search for user-specific packages, which can be useful in environments where user-installed packages are managed differently.

```python
import site

# Enable searching for user-site-packages
site.setusersitepackages(True)

# Now Python will look in the user's site-packages directory if available
try:
    import my_user_module
except ImportError as e:
    print(f"Module not found: {e}")
```

### 7. `site.clearsitepackages()`
- **Purpose**: Clears the list of directories that Python searches for site-specific modules.
- **Description**: This function is used to reset the Python path, removing all custom additions made by `addsitedir`.

```python
import site

# Add a custom site directory
site.addsitedir('/path/to/custom/site-packages')

# Clear the list of site-packages directories
site.clearsitepackages()

# Now Python will only search in the standard library path
try:
    import my_standard_module
except ImportError as e:
    print(f"Module not found: {e}")
```

### 8. `site.addsitedir(path, setpath=True)`
- **Purpose**: Adds a directory to the list of directories that Python searches for site-specific modules and optionally updates the system PYTHONPATH.
- **Description**: This function is useful for adding a custom directory to the Python path and updating the system environment variable in one step.

```python
import site

# Add a custom site directory to the Python path and update PYTHONPATH
site.addsitedir('/path/to/custom/site-packages', setpath=True)

# Now you can import modules from this directory and PYTHONPATH is updated
try:
    import my_custom_module
except ImportError as e:
    print(f"Module not found: {e}")
```

### 9. `site.removesitedir(path, unsetsitepackages=False)`
- **Purpose**: Removes a directory from the list of directories that Python searches for site-specific modules and optionally updates the system PYTHONPATH.
- **Description**: This function is useful for removing a custom directory from the Python path and updating the system environment variable in one step.

```python
import site

# Add a custom site directory to the Python path
site.addsitedir('/path/to/custom/site-packages')

# Remove the custom site directory and update PYTHONPATH
site.removesitedir('/path/to/custom/site-packages', unsetsitepackages=True)

# Now Python will only search in the standard library path and PYTHONPATH is updated
try:
    import my_standard_module
except ImportError as e:
    print(f"Module not found: {e}")
```

### 10. `site.addsitedir(path, setpath=True)`
- **Purpose**: Adds a directory to the list of directories that Python searches for site-specific modules and optionally updates the system PYTHONPATH.
- **Description**: This function is useful for adding a custom directory to the Python path and updating the system environment variable in one step.

```python
import site

# Add a custom site directory to the Python path and update PYTHONPATH
site.addsitedir('/path/to/custom/site-packages', setpath=True)

# Now you can import modules from this directory and PYTHONPATH is updated
try:
    import my_custom_module
except ImportError as e:
    print(f"Module not found: {e}")
```

These code examples demonstrate various functionalities of the `site` module, including adding custom directories to the Python path, accessing specific directories where Python looks for site-specific packages, and managing the PYTHONPATH environment variable.
