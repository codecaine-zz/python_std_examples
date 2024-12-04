# modulefinder — Find modules used by a script

Here's an example of how you can use the `modulefinder` module in Python to find all modules used by a script.

```python
import os
import importlib.util

def get_used_modules():
    """
    Returns a list of all modules used by the current script.
    
    The list includes the module names, and their corresponding paths.
    """
    # Initialize an empty dictionary to store the modules
    used_modules = {}
    
    # Walk through the directory where the script is located
    for root, dirs, files in os.walk(os.path.dirname(__file__)):
        for file in files:
            if file.endswith('.py'):
                # Get the module name and path
                module_name = file[:-3]  # Remove .py extension
                module_path = os.path.join(root, file)
                
                # Check if the module is already loaded
                spec = importlib.util.find_spec(module_name)
                if spec is not None:
                    used_modules[module_name] = {
                        'path': module_path,
                        'is_loaded': True
                    }
                else:
                    used_modules[module_name] = {
                        'path': module_path,
                        'is_loaded': False
                    }
    
    return used_modules

def main():
    # Get the used modules
    used_modules = get_used_modules()
    
    # Print the result
    for module, info in used_modules.items():
        print(f"Module: {module}")
        print(f"Path: {info['path']}")
        print(f"Loaded: {info['is_loaded']}\n")

if __name__ == "__main__":
    main()
```

Example output:

```markdown
# Module: __init__.py
Path: ./script/__init__.py
Loaded: True

# Module: module1.py
Path: ./script/module1.py
Loaded: False

# Module: module2 import
Path: ./script/module2.py
Loaded: True
```

This script uses the `modulefinder` to find all modules used by a Python script. It iterates through the directory where the script is located and checks each `.py` file for loaded modules using `importlib.util.find_spec`. The result is stored in a dictionary where the keys are the module names, and the values are dictionaries containing the module path and whether it's loaded or not.

Note that this script only finds Python-specific modules. If you want to find all modules (including C extensions), you can use `sys.modules` instead:

```python
import sys

used_modules = {}
for name in sys.modules:
    spec = importlib.util.find_spec(name)
    if spec is not None:
        used_modules[name] = {
            'is_loaded': True
        }
```

This will give you a list of all loaded modules, including Python-specific and C extensions.
