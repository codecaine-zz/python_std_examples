# plistlib — Generate and parse Apple .plist files

Here are some examples of using `plistlib`:

```python
import plistlib
from pathlib import Path
from io import StringIO

# Example 1: Create a new PLIST file
def create_plist(plist_data):
    """
    Creates a new PLIST file with the given data.

    Args:
        plist_data (dict): The data to write to the PLIST file.
    """
    with open("example.plist", "wb") as f:
        plistlib.dump(plist_data, f)

# Example 2: Parse an existing PLIST file
def parse_plist(plist_path):
    """
    Parses an existing PLIST file.

    Args:
        plist_path (Path): The path to the PLIST file.
    """
    with open(plist_path, "rb") as f:
        plist_data = plistlib.load(f)
        print(plist_data)

# Example 3: Parse a string representation of a PLIST
def parse_plist_string(plist_str):
    """
    Parses a string representation of a PLIST.

    Args:
        plist_str (str): The string representation of the PLIST.
    """
    plist_data = plistlib.loads(StringIO(plist_str))
    print(plist_data)

# Example 4: Update an existing PLIST file
def update_plist(plist_path, updated_data):
    """
    Updates an existing PLIST file with the given data.

    Args:
        plist_path (Path): The path to the PLIST file.
        updated_data (dict): The updated data to write to the PLIST file.
    """
    with open(plist_path, "rb") as f:
        old_plist_data = plistlib.load(f)
    updated_plist_data = {**old_plist_data, **updated_data}
    with open(plist_path, "wb") as f:
        plistlib.dump(updated_plist_data, f)

# Example 5: Create a PLIST dictionary from scratch
def create_plist_dict():
    """
    Creates an empty PLIST dictionary.
    """
    return {}

# Example 6: Add data to the created PLIST dictionary
def add_to_plist(plist_dict):
    """
    Adds new data to the created PLIST dictionary.

    Args:
        plist_dict (dict): The PLIST dictionary.
    """
    plist_dict["key"] = "value"
    return plist_dict

# Example 7: Write the updated PLIST dictionary to a file
def write_plist(plist_path, plist_data):
    """
    Writes the given PLIST data to a file.

    Args:
        plist_path (Path): The path to the output file.
        plist_data (dict): The PLIST data to write.
    """
    with open(plist_path, "wb") as f:
        plistlib.dump(plist_data, f)
```

Here is an example of how you can use these functions:

```python
plist_data = {
    "CFBundleIdentifier": "com.example.plist",
    "CFBundleName": "Example App",
    "CFBundleVersion": "1.0"
}

create_plist(plist_data)

parse_plist(Path("example.plist"))

updated_data = {"CFBundleShortVersionString": "2.0"}
update_plist(Path("example.plist"), updated_data)

created_plist_dict = create_plist_dict()
added_data = add_to_plist(created_plist_dict)
write_plist("new_example.plist", added_data)
```

This will create a new PLIST file with the given data, parse an existing PLIST file, update an existing PLIST file with new data, create a new empty PLIST dictionary, add data to the dictionary, and write the updated dictionary to a new file.
