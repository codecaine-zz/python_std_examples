# imp — Access the import internals

Here's an example of how you can access and manipulate the `import` module in Python:

```python
# Import the import module directly
import importlib

# Get a list of all registered modules
registered_modules = [m[0] for m in importlib.machinery.module_specifiers()]
print("Registered Modules:")
for module in registered_modules:
    print(module)

# Get a list of all loaded modules
loaded_modules = [m.name for m in importlib.util.find_spec "__import__").names]
print("\nLoaded Modules:")
for module in loaded_modules:
    print(module)

# Import a specific module using the `alias` function
from importlib.machinery import ModuleSpec

# Create a new module spec with a custom name and location
module_spec = ModuleSpec("custom_module", "path/to/custom_module.py")

# Use the `alias` function to register the module
importlib.util.module_from_spec(module_spec)
importlib.util.setup_module(module_spec)

# Get the imported module using the `__name__` attribute
imported_module = __import__("custom_module")
print("\nImported Module:")
print(imported_module.__name__)
```

**Accessing Import Errors**

To access import errors, you can use the following code:

```python
try:
    # Attempt to import a module with an error
    __import__("non_existent_module")
except ImportError as e:
    # Print the error message
    print(f"Import Error: {e}")

# Get all import errors using the `errors` attribute of the `module_specifier`
errors = [m[1].__name__ for m in importlib.machinery.module_specifiers() if m[1].errors]
print("\nImport Errors:")
for error in errors:
    print(error)
```

**Manipulating Import Settings**

To manipulate import settings, you can use the following code:

```python
import sys

# Get the current import path
sys.path.append("path/to/new/directory")

try:
    # Attempt to import a module again after modifying the import path
    __import__("module")
except ImportError as e:
    print(f"Import Error: {e}")

# Reset the import path to its original value
sys.path.pop()

# Get all import paths using the `sys.modules` dictionary
import_paths = sys.modules.keys()
print("\nImport Paths:")
for path in import_paths:
    print(path)

# Create a new import path and add it to the list of paths
new_path = "path/to/new/directory"
sys.path.append(new_path)
del sys.modules[new_path]
```

**Accessing Import Hooks**

To access import hooks, you can use the following code:

```python
import importlib.util

# Get a list of all installed hooks using the `hooks` attribute of the `module_specifier`
hooks = [m[1].__name__ for m in importlib.machinery.module_specifiers()]
print("\nImport Hooks:")
for hook in hooks:
    print(hook)

# Define a new import hook function
def custom_hook(module):
    print(f"Custom Hook: {module.__name__}")

import importlib.util

# Register the custom hook using the `setup_hook` function
importlib.util.setup_hook("custom_module", custom_hook)

# Get the imported module using the `__name__` attribute
imported_module = __import__("custom_module")
print("\nImported Module:")
print(imported_module.__name__)

# Define a new import error hook function
def custom_error_hook(error):
    print(f"Custom Error Hook: {error}")

import importlib.util

# Register the custom error hook using the `setup_error_hook` function
importlib.util.setup_error_hook("custom_module", custom_error_hook)
```
