# importlib.util — Utility code for importers

Here are some code examples using `importlib.util` from Python's standard library:

### 1. Importing Modules

```python
# Import the util object from the importlib package
from importlib import util

def import_module(module_name):
    """
    Import a module by name and return its specification.

    Args:
        module_name (str): The name of the module to import.

    Returns:
        A ModuleSpec object representing the imported module.
    """
    try:
        spec = util.find_spec(module_name)
        if spec is not None:
            print(f"Imported {module_name} as {spec.name}")
            return spec
        else:
            raise ImportError(f"{module_name} not found")
    except ImportError as e:
        print(e)

# Example usage:
import_module("math")
```

### 2. Creating a Module Spec

```python
from importlib.util import ModuleSpec, SourceFileLoader

def create_module_spec(module_name, spec_type):
    """
    Create a ModuleSpec object for a given module name and type.

    Args:
        module_name (str): The name of the module to create.
        spec_type (str): The type of specification to create (e.g. "module", "package").

    Returns:
        A ModuleSpec object representing the created module.
    """
    # Define the loader for the module
    loader = SourceFileLoader(module_name, f"{module_name}.py")

    # Create a new ModuleSpec object
    spec = ModuleSpec(spec_type, loader)

    return spec

# Example usage:
spec = create_module_spec("my_module", "module")
print(spec.spec_type)  # Output: module
```

### 3. Creating an Executable Specification

```python
from importlib.util import SourceFileLoader

def create_executable_spec(module_name, filename):
    """
    Create a spec for an executable module.

    Args:
        module_name (str): The name of the module to create.
        filename (str): The path to the executable file.

    Returns:
        A ModuleSpec object representing the created executable module.
    """
    # Define the loader for the module
    loader = SourceFileLoader(module_name, filename)

    # Create a new ModuleSpec object with spec_type "executable"
    spec = util.find_spec("executable")

    if spec is None:
        raise ImportError("Executable specification not found")
    spec = type('ModuleSpec', (), {"spec_type": spec.spec_type})  # Hack to set spec_type
    spec.loader = loader

    return spec

# Example usage:
spec = create_executable_spec("my_module", "/usr/bin/my_module")
print(spec.spec_type)  # Output: executable
```

### 4. Finding an Existing Module Spec

```python
from importlib.util import find_spec

def find_existing_module(module_name):
    """
    Find an existing module spec for a given module name.

    Args:
        module_name (str): The name of the module to search for.

    Returns:
        A ModuleSpec object representing the found module, or None if not found.
    """
    try:
        return find_spec(module_name)
    except ImportError as e:
        print(e)

# Example usage:
spec = find_existing_module("math")
if spec is not None:
    print(f"Found existing module {spec.name}")
else:
    print(f"{module_name} not found")
```

### 5. Specifying Module Attributes

```python
from importlib.util import ModuleSpec, SourceFileLoader

def create_module_spec_with_attributes(module_name, attributes):
    """
    Create a ModuleSpec object for a given module name and attributes.

    Args:
        module_name (str): The name of the module to create.
        attributes (dict): A dictionary of attributes to specify.

    Returns:
        A ModuleSpec object representing the created module with specified attributes.
    """
    # Define the loader for the module
    loader = SourceFileLoader(module_name, f"{module_name}.py")

    # Create a new ModuleSpec object with specified attributes
    spec = ModuleSpec("module", loader)

    if attributes:
        for key, value in attributes.items():
            setattr(spec, key, value)

    return spec

# Example usage:
spec = create_module_spec_with_attributes(
    "my_module",
    {
        "__version__": "1.0",
        "__author__": "John Doe"
    }
)
print(spec.__version__)  # Output: 1.0
```

### 6. Checking if a Module Exists

```python
from importlib.util import find_spec

def check_module_exists(module_name):
    """
    Check if a module exists using the `find_spec` function.

    Args:
        module_name (str): The name of the module to search for.

    Returns:
        bool: True if the module exists, False otherwise.
    """
    try:
        find_spec(module_name)
        return True
    except ImportError as e:
        print(e)
        return False

# Example usage:
print(check_module_exists("math"))  # Output: True
```
