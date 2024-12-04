# pkgutil - Package extension utility

**pkgutil Module Examples**

The `pkgutil` module provides a set of functions to explore and load Python packages, including finding modules, entry points, and other related resources.

### Example 1: Find All Modules in a Package

```python
import pkgutil

# Define the package name
package_name = 'example_package'

try:
    # Use pkgutil.iter_modules() to find all modules in the specified package
    for module_loader, module_name, ispkg in pkgutil.iter_modules([package_name]):
        if not ispkg:  # Skip packages
            print(f"Module found: {module_name}")

except ImportError as e:
    print(f"Error: {e}")
```

**Explanation:**
- **`pkgutil.iter_modules()`**: This function returns an iterator yielding a tuple of three values for each module in the package. The first value is the `importer`, which may be `None`; the second is the module name; and the third indicates if it's a package.
- **Filtering Non-Packages**: The example checks if `ispkg` is `False` to filter out non-package modules.

### Example 2: Access a Module Dynamically

```python
import pkgutil

# Define the package and module names
package_name = 'example_package'
module_name = 'example_module'

try:
    # Use importlib.import_module() to dynamically load the specified module
    module = pkgutil.import_module(f"{package_name}.{module_name}")
    
    # Access a function or variable from the module
    result = module.some_function()
    print(result)

except ImportError as e:
    print(f"Error: {e}")
```

**Explanation:**
- **`pkgutil.import_module()`**: This function dynamically imports a module by name.
- **Example Use Case**: The example accesses a function named `some_function` from the specified module.

### Example 3: List Entry Points

```python
import pkgutil
from importlib_metadata import entry_points

# Define the distribution name and group (e.g., 'console_scripts')
distribution_name = 'example_distribution'
group = 'console_scripts'

try:
    # Use entry_points() to list all entry points for a specified distribution and group
    entry_points_list = entry_points(distribution_name=distribution_name, group=group)
    
    for ep in entry_points_list:
        print(f"Entry point: {ep.name}, command: {ep.command}")

except ValueError as e:
    print(f"Error: {e}")
```

**Explanation:**
- **`entry_points()`**: This function returns a list of `EntryPoint` objects from the distribution's metadata.
- **Example Use Case**: The example lists all console script entry points for a given distribution.

### Example 4: Find All Subpackages

```python
import pkgutil

# Define the package name
package_name = 'example_package'

try:
    # Use pkgutil.iter_submodules() to find all submodules in the specified package
    for submodule_loader, submodule_name, ispkg in pkgutil.iter_modules([package_name]):
        if ispkg:  # Only include packages
            print(f"Subpackage found: {submodule_name}")

except ImportError as e:
    print(f"Error: {e}")
```

**Explanation:**
- **`pkgutil.iter_submodules()`**: Similar to `iter_modules()`, but specifically returns submodules (i.e., packages).
- **Filtering Packages**: The example filters for submodules by checking if `ispkg` is `True`.

### Example 5: Find a Resource in a Package

```python
import pkgutil

# Define the package and resource name
package_name = 'example_package'
resource_name = 'path/to/resource'

try:
    # Use pkgutil.get_data() to load a resource from the specified package
    data = pkgutil.get_data(package_name, resource_name)
    
    # Decode the bytes data into a string (assuming UTF-8 encoding)
    decoded_data = data.decode('utf-8')
    print(decoded_data)

except FileNotFoundError as e:
    print(f"Error: {e}")
```

**Explanation:**
- **`pkgutil.get_data()`**: This function loads binary data from a package.
- **Example Use Case**: The example loads and decodes a resource file (e.g., a configuration file) from the specified package.

These examples demonstrate various functionalities of the `pkgutil` module, including finding modules, accessing them dynamically, listing entry points, discovering subpackages, and retrieving resources. Each example is designed to be self-contained and clear, with comments explaining key steps.
