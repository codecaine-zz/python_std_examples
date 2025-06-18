# winreg - Windows registry access
## Table of Contents

1. [Example 1: Create a New Key in the Current User's Local Machine](#example-1-create-a-new-key-in-the-current-users-local-machine)
2. [Example 2: Read a Value from a Key](#example-2-read-a-value-from-a-key)
3. [Example 3: Delete a Value from a Key](#example-3-delete-a-value-from-a-key)
4. [Example 4: Modify an Existing Value in a Key](#example-4-modify-an-existing-value-in-a-key)
5. [Example 5: Create a New Subkey and Set Multiple Values](#example-5-create-a-new-subkey-and-set-multiple-values)
6. [Example 6: Read Values from a Subkey](#example-6-read-values-from-a-subkey)
7. [Example 7: Delete a Subkey and All Its Values](#example-7-delete-a-subkey-and-all-its-values)
8. [Example 8: Enumerate All Subkeys](#example-8-enumerate-all-subkeys)



The `winreg` module is part of the Python Standard Library and provides a convenient way to interact with the Windows Registry. This module allows you to read, write, modify, and delete registry keys and values. Below are some comprehensive code examples for various functionalities of the `winreg` module:

### Example 1: Create a New Key in the Current User's Local Machine
```python
import winreg

# Define the path to the new key
key_path = r"SOFTWARE\Example\MyKey"

# Open or create the key with write access
key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)

# Set a value in the newly created key
winreg.SetValueEx(key, "ValueName", 0, winreg.REG_SZ, "Hello World")

# Close the registry key
winreg.CloseKey(key)
```

### Example 2: Read a Value from a Key
```python
import winreg

# Define the path to the key and the value name
key_path = r"SOFTWARE\Example\MyKey"
value_name = "ValueName"

try:
    # Open the key with read access
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    
    # Retrieve a value from the key
    value_type, value_data = winreg.QueryValueEx(key, value_name)
    
    print(f"Value Type: {value_type}")
    print(f"Value Data: {value_data}")
    
    # Close the registry key
    winreg.CloseKey(key)
except FileNotFoundError:
    print("The specified key or value does not exist.")
```

### Example 3: Delete a Value from a Key
```python
import winreg

# Define the path to the key and the value name
key_path = r"SOFTWARE\Example\MyKey"
value_name = "ValueName"

try:
    # Open the key with write access
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)
    
    # Delete a value from the key
    winreg.DeleteValue(key, value_name)
    
    print("Value deleted successfully.")
    
    # Close the registry key
    winreg.CloseKey(key)
except FileNotFoundError:
    print("The specified key or value does not exist.")
```

### Example 4: Modify an Existing Value in a Key
```python
import winreg

# Define the path to the key and the value name
key_path = r"SOFTWARE\Example\MyKey"
value_name = "ValueName"

try:
    # Open the key with write access
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE)
    
    # Modify an existing value in the key
    new_value_data = "Updated Value"
    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, new_value_data)
    
    print("Value updated successfully.")
    
    # Close the registry key
    winreg.CloseKey(key)
except FileNotFoundError:
    print("The specified key or value does not exist.")
```

### Example 5: Create a New Subkey and Set Multiple Values
```python
import winreg

# Define the path to the root key where the subkey will be created
root_key = winreg.HKEY_LOCAL_MACHINE

# Define the full path for the new subkey and its values
subkey_path = r"SOFTWARE\Example\MySubKey"
values_to_set = {
    "StringValue": "Hello, Subkey!",
    "IntegerValue": 123,
    "BinaryValue": b"\x01\x02\x03"
}

# Open or create the subkey with write access
subkey = winreg.CreateKey(root_key, subkey_path)

try:
    # Set multiple values in the newly created subkey
    for value_name, value_data in values_to_set.items():
        if isinstance(value_data, str):
            reg_type = winreg.REG_SZ
        elif isinstance(value_data, int):
            reg_type = winreg.REG_DWORD
        elif isinstance(value_data, bytes):
            reg_type = winreg.REG_BINARY
        
        winreg.SetValueEx(subkey, value_name, 0, reg_type, value_data)
    
    print("Values set successfully.")
finally:
    # Close the registry subkey
    winreg.CloseKey(subkey)
```

### Example 6: Read Values from a Subkey
```python
import winreg

# Define the full path to the subkey
subkey_path = r"SOFTWARE\Example\MySubKey"

try:
    # Open the subkey with read access
    subkey = winreg.OpenKey(root_key, subkey_path)
    
    # Retrieve all values from the subkey
    for value_name in winreg.QueryValueNames(subkey):
        reg_type, value_data = winreg.QueryValueEx(subkey, value_name)
        
        print(f"Value Name: {value_name}")
        print(f"Value Type: {reg_type}")
        if reg_type == winreg.REG_SZ:
            print(f"Value Data: '{value_data}'")
        elif reg_type == winreg.REG_DWORD:
            print(f"Value Data: {value_data} (Decimal)")
        elif reg_type == winreg.REG_BINARY:
            print(f"Value Data: {value_data.hex()}")
    
    # Close the registry subkey
    winreg.CloseKey(subkey)
except FileNotFoundError:
    print("The specified key does not exist.")
```

### Example 7: Delete a Subkey and All Its Values
```python
import winreg

# Define the full path to the subkey
subkey_path = r"SOFTWARE\Example\MySubKey"

try:
    # Open the subkey with write access
    subkey = winreg.OpenKey(root_key, subkey_path, 0, winreg.KEY_ALL_ACCESS)
    
    # Delete all values in the subkey first
    value_names = winreg.QueryValueNames(subkey)
    for value_name in value_names:
        winreg.DeleteValue(subkey, value_name)
    
    # Delete the subkey
    winreg.DeleteKey(root_key, subkey_path)
    
    print("Subkey and all its values deleted successfully.")
finally:
    # Close the registry key (not strictly necessary here but good practice)
    if subkey:
        winreg.CloseKey(subkey)
```

### Example 8: Enumerate All Subkeys
```python
import winreg

# Define the path to the root key
root_key = winreg.HKEY_LOCAL_MACHINE

try:
    # Open the root key with read access
    key = winreg.OpenKey(root_key, "")
    
    # Enumerate all subkeys
    for subkey_name in winreg.EnumKey(key):
        print(subkey_name)
    
    # Close the registry key
    winreg.CloseKey(key)
except FileNotFoundError:
    print("The specified root key does not exist.")
```

These examples demonstrate various operations you can perform with the `winreg` module, including creating and deleting keys, setting and reading values, modifying existing values, handling different value types (string, integer, binary), and enumerating subkeys. Always ensure that you have administrative privileges when making changes to the Windows Registry to avoid errors or system instability.
