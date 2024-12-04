# tomllib — Parse TOML files

**Tomlib Module: Parsing TOML Files**
=====================================

The `tomllib` module is part of the Python Standard Library, which provides support for parsing and encoding Tom's Obvious, Minimal Language (TOML) files.

### Module Overview

Here's an overview of the main functions provided by the `tomllib` module:

*   **Loading a TOML file**: The `tomllib.load()` function loads a TOML file into a Python dictionary.
*   **Encoding a dictionary to TOML**: The `tomllib.dumps()` function encodes a Python dictionary to a TOML string.

### Code Examples

#### Loading a TOML File

Here's an example of how to load a TOML file using the `tomllib.load()` function:

```python
import tomllib

def load_toml_file(file_path):
    """
    Load a TOML file into a Python dictionary.
    
    Args:
        file_path (str): Path to the TOML file.

    Returns:
        dict: The loaded TOML data as a Python dictionary.
    """
    try:
        with open(file_path, 'rb') as file:
            # Use the `tomllib.load()` function to load the TOML file
            data = tomllib.load(file)
            return data
    except tomllib.TomlibParserError as e:
        print(f"Error parsing TOML file: {e}")
        return None

# Example usage:
file_path = 'example.toml'
data = load_toml_file(file_path)
if data is not None:
    print(data)
```

#### Encoding a Dictionary to TOML

Here's an example of how to encode a Python dictionary to a TOML string using the `tomllib.dumps()` function:

```python
import tomllib

def dump_toml_dict(data):
    """
    Encode a Python dictionary to a TOML string.
    
    Args:
        data (dict): The Python dictionary to be encoded.

    Returns:
        str: The encoded TOML string.
    """
    try:
        # Use the `tomllib.dumps()` function to encode the dictionary
        tomldata = tomllib.dumps(data, sort_keys=True)
        return tomldata
    except Exception as e:
        print(f"Error encoding dictionary: {e}")
        return None

# Example usage:
data = {'name': 'John', 'age': 30}
toml_string = dump_toml_dict(data)
if toml_string is not None:
    print(toml_string)
```

### Best Practices

Here are some best practices for working with the `tomllib` module:

*   Always use the `try-except` block when loading or encoding TOML data to handle potential errors.
*   Use the `tomllib.load()` function to load TOML files, and the `tomllib.dumps()` function to encode Python dictionaries.
*   Consider using the `sort_keys=True` argument when encoding dictionaries to ensure consistent ordering of keys in the generated TOML string.
