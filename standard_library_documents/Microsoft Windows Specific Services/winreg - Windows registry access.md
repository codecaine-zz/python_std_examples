# winreg — Windows registry access

Here's an example of how you can use the `winreg` module in Python:

**Accessing and Modifying Registry Values**
```python
import winreg

# Open the registry key
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_READ | winreg.KEY_WRITE)

try:
    # Read the value of the 'Python' key
    value, regtype = winreg.QueryValueEx(key, "Python")
    print(f"Current Python executable: {value}")

    # Modify the value of the 'Python' key
    new_value = r"C:\path\to\python.exe"
    winreg.SetValueEx(key, "Python", 0, winreg.REG_SZ, new_value)
except Exception as e:
    print(f"Error accessing registry key: {e}")
finally:
    # Close the registry key
    winreg.CloseKey(key)
```

**Creating a New Registry Key**
```python
import winreg

# Create a new registry key
key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\MyCompany\\Settings")

try:
    # Set a value in the new key
    regvalue = winreg.CreateValueEx(winreg.KEY_VALUE, b"MySetting", 0, winreg.REG_SZ, b"Hello World")
    winreg.SetValue(key, regvalue)
except Exception as e:
    print(f"Error creating registry key: {e}")
finally:
    # Close the registry key
    winreg.CloseKey(key)
```

**Deleting a Registry Key**
```python
import winreg

# Open the registry key
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\MyCompany\\Settings", 0, winreg.KEY_READ | winreg.KEY_WRITE)

try:
    # Delete the value in the key
    winreg.DeleteValue(key, b"MySetting")
except Exception as e:
    print(f"Error deleting registry key: {e}")
finally:
    # Close the registry key
    winreg.CloseKey(key)
```

**Querying Registry Keys**
```python
import winreg

# Open a specific registry key
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_READ)

try:
    # Iterate over the values in the key
    while True:
        value, regtype = winreg.QueryValueEx(key, None)
        if not value:
            break
        print(f"Key: {value}")
except Exception as e:
    print(f"Error querying registry key: {e}")
finally:
    # Close the registry key
    winreg.CloseKey(key)
```

Note that you'll need to run your Python script with administrator privileges to access and modify the Windows registry.
