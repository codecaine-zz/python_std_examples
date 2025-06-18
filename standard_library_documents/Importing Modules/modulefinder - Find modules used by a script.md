# modulefinder - Find modules used by a script
## Table of Contents

1. [1. Basic Usage](#1-basic-usage)
2. [Example: Finding Modules Used by a Script](#example-finding-modules-used-by-a-script)
3. [Explanation:](#explanation)
4. [2. Analyzing Modules with ModuleFinder](#2-analyzing-modules-with-modulefinder)
5. [Example: Using ModuleFinder for Detailed Analysis](#example-using-modulefinder-for-detailed-analysis)
6. [Explanation:](#explanation)
7. [3. Customizing ModuleFinder](#3-customizing-modulefinder)
8. [Example: Filtering Modules by Type](#example-filtering-modules-by-type)
9. [Explanation:](#explanation)
10. [4. Handling Large Scripts](#4-handling-large-scripts)



The `modulefinder` module is part of Python's standard library, which provides tools to analyze and manage Python package installations. It allows you to find and analyze the imports in a Python script or module. Below are comprehensive code examples for various functionalities provided by the `modulefinder` module.

### 1. Basic Usage

#### Example: Finding Modules Used by a Script
```python
import sys
from importlib.util import find_spec

# List of scripts to analyze
scripts = [
    "example_script.py",
]

for script in scripts:
    print(f"Analyzing {script}:")
    
    # Find the spec for the script module
    spec = find_spec(script)
    if spec is None:
        print(f"No module found for: {script}")
    else:
        print("Modules used by", script, "are:")
        
        # Walk through all imports in the spec
        for submodule in spec.submodules:
            if submodule.loader is not None:
                print(submodule.name)
```

#### Explanation:
- **Importing `sys` and `find_spec`:** These are essential modules for interacting with the Python runtime.
- **Finding Script Modules:** The `find_spec()` function is used to locate the import spec of a module. This returns an object that provides information about the module, including its name, path, and loader.
- **Iterating Through Submodules:** The `submodules` attribute contains all submodules imported by the script.

### 2. Analyzing Modules with ModuleFinder

#### Example: Using ModuleFinder for Detailed Analysis
```python
import sys
from importlib.util import find_spec
from modulefinder import ModuleFinder

# List of scripts to analyze
scripts = [
    "example_script.py",
]

for script in scripts:
    print(f"Analyzing {script}:")
    
    # Create a ModuleFinder instance
    finder = ModuleFinder()

    # Run the finder on the script
    finder.run_script(script)

    # Print found modules
    for mod in finder.modules.values():
        if mod.name not in sys.builtin_module_names:
            print(f"Module: {mod.name}, File: {mod.file}")

    # Print missing imports
    for mod_name, err in finder.errors.items():
        print(f"Error importing {mod_name}: {err}")
```

#### Explanation:
- **Using `ModuleFinder`:** This class is used to perform more comprehensive analysis of modules and their dependencies.
- **Running the Finder:** The `run_script()` method processes the script and records all imported modules and any errors encountered.
- **Handling Results:** The found modules are stored in the `finder.modules` dictionary, where each module has a `name` and `file` attribute.

### 3. Customizing ModuleFinder

#### Example: Filtering Modules by Type
```python
import sys
from importlib.util import find_spec
from modulefinder import ModuleFinder

# List of scripts to analyze
scripts = [
    "example_script.py",
]

for script in scripts:
    print(f"Analyzing {script}:")
    
    # Create a ModuleFinder instance and specify include standard library modules
    finder = ModuleFinder()
    finder.add_package_path("")

    # Run the finder on the script
    finder.run_script(script)

    # Filter out built-in modules
    found_modules = [mod.name for mod in finder.modules.values() if mod.file is not None]

    print("Modules used by", script, "are:")
    for module in found_modules:
        print(module)
```

#### Explanation:
- **Including Standard Library Modules:** By adding the package path with `finder.add_package_path("")`, all standard library modules are included.
- **Filtering Built-in Modules:** The code filters out built-in modules by checking if the `file` attribute is not `None`.

### 4. Handling Large Scripts

#### Example: Analyzing a Large Script
```python
import sys
from importlib.util import find_spec
from modulefinder import ModuleFinder

# List of large scripts to analyze
large_scripts = [
    "large_script.py",
]

for script in large_scripts:
    print(f"Analyzing {script}:")
    
    # Create a ModuleFinder instance
    finder = ModuleFinder()

    # Run the finder on the script
    finder.run_script(script)

    # Print total number of modules found
    total_modules = len(finder.modules)
    print(f"Total modules found in {script}: {total_modules}")

    # Print top 10 most imported modules
    import_counts = {mod.name: mod.importer.count for mod in finder.modules.values() if mod.importer is not None}
    top_10 = sorted(import_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\nTop 10 most imported modules:")
    for module, count in top_10:
        print(f"Module: {module}, Imports: {count}")
```

#### Explanation:
- **Running the Finder on a Large Script:** The `run_script()` method is used to process large scripts efficiently.
- **Counting Module Imports:** The script counts how many times each module is imported and prints the top 10 most imported modules.

### Conclusion

These examples demonstrate various functionalities of the `modulefinder` module, including basic usage, detailed analysis with `ModuleFinder`, customizing module searching, handling large scripts, and filtering out built-in modules. Each example includes comments to help understand the code's purpose and functionality.
