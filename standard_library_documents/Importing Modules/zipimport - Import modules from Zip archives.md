# zipimport — Import modules from Zip archives

**ZipImport Example**
```python
# Importing modules from a zip archive using ZipImport

import importlib.util
from importlib.machinery import SourceFileLoader
from io import BytesIO

def load_module_from_zip(zip_path, module_name):
    """
    Load a Python module from a zip archive.

    Args:
        zip_path (str): Path to the zip archive containing the module.
        module_name (str): Name of the module to be loaded.

    Returns:
        Module: The loaded module.
    """
    # Create a BytesIO object to simulate a file
    with open(zip_path, 'rb') as f:
        zip_data = f.read()

    # Load the zip archive using the BytesIO object
    spec = importlib.util.spec_from_file_location(module_name, BytesIO(zip_data))
    
    if spec is None:
        raise ValueError(f"Failed to load module from zip: {module_path}")

    # Create a SourceFileLoader object to load the module
    loader = SourceFileLoader(module_name, BytesIO(zip_data))

    # Load the module using the loader
    try:
        module = loader.load_module()
    except Exception as e:
        raise ValueError(f"Failed to load module from zip: {e}")

    return module

# Example usage
if __name__ == "__main__":
    # Create a sample zip archive containing a Python module
    import zipfile
    with zipfile.ZipFile("example.zip", "w") as zip_file:
        # Add the module to the zip archive
        zip_file.write("./module.py")

    # Load the module from the zip archive
    module_name = "example.module"
    loaded_module = load_module_from_zip("example.zip", module_name)

    # Print the loaded module's name and attributes
    print(f"Loaded Module: {loaded_module.__name__}")
    for attr in dir(loaded_module):
        if not attr.startswith("_"):
            print(f"{attr}: {getattr(loaded_module, attr)}")
```

**Explanation**

This code defines a function `load_module_from_zip` that loads a Python module from a zip archive. It uses the `importlib.util.spec_from_file_location` function to create a module specification for the zip archive, and then creates a `SourceFileLoader` object to load the module.

The example usage demonstrates how to create a sample zip archive containing a Python module, load the module using the `load_module_from_zip` function, and print the loaded module's name and attributes.

**Note**

This code assumes that the zip archive contains a single Python module file. If your use case involves loading multiple modules from different parts of the same zip archive, you will need to modify the code accordingly.

Also note that this is just one way to load a Python module from a zip archive. Depending on your specific requirements, you may need to use other methods or libraries.
