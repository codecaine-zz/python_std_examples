# importlib.metadata — Accessing the import metadata

Here's an example of how you can access the metadata of an imported module using `importlib.metadata`:

```python
# Import the importlib.metadata module
from importlib.metadata import version, name, author, description

def get_module_metadata(module_name):
    """
    Returns the metadata of a given module.

    Args:
        module_name (str): The name of the module to retrieve metadata for.

    Returns:
        dict: A dictionary containing the metadata.
    """

    # Try to get the module's metadata
    try:
        # Get the module's version
        module_version = version(module_name)
        
        # Get the module's name
        module_name_str = name(module_name)
        
        # Get the author of the module
        module_author = author(module_name)
        
        # Get a brief description of the module
        module_description = description(module_name)
        
        # Return the metadata as a dictionary
        return {
            "version": module_version,
            "name": module_name_str,
            "author": module_author,
            "description": module_description,
        }
    
    # Handle any exceptions that may occur during metadata retrieval
    except Exception as e:
        print(f"Error retrieving metadata for {module_name}: {e}")
        return None

# Example usage
if __name__ == "__main__":
    module_name = "importlib.metadata"
    metadata = get_module_metadata(module_name)
    
    if metadata:
        print("Module Metadata:")
        print(f"Version: {metadata['version']}")
        print(f"Name: {metadata['name']}")
        print(f"Author: {metadata['author']}")
        print(f"Description: {metadata['description']}")
```

This example uses the `importlib.metadata` module to access metadata for a given module. The `get_module_metadata` function takes a module name as input and returns a dictionary containing the module's version, name, author, and description.

Please note that this is just an example and you may want to customize it according to your needs.

Here are some additional methods provided by `importlib.metadata`:

*   `version(module_name)`: Returns the version number of a given module.
*   `name(module_name)`: Returns the full name of a given module.
*   `author(module_name)`: Returns the author of a given module.
*   `description(module_name)`: Returns a brief description of a given module.
*   `home(module_name)`: Returns the URL of the module's homepage (available since Python 3.10).
*   `readme(filename)`: Returns the contents of a file at the specified path in the module's home directory (available since Python 3.9).

These methods can be used to access metadata for various modules, including built-in modules and packages that are installed using pip or other package managers.
