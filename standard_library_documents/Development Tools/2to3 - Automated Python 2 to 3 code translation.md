# 2to3 - Automated Python 2 to 3 code translation
## Table of Contents

1. [Example 1: Basic Conversion with a Script](#example-1-basic-conversion-with-a-script)
2. [Description:](#description)
3. [Explanation:](#explanation)
4. [Example 2: Using Fixers Manually](#example-2-using-fixers-manually)
5. [Description:](#description)
6. [Explanation:](#explanation)
7. [Example 3: Running 2to3 on Multiple Files](#example-3-running-2to3-on-multiple-files)
8. [Description:](#description)
9. [Explanation:](#explanation)
10. [Example 4: Using 2to3 as a Command-line Tool](#example-4-using-2to3-as-a-command-line-tool)



The `2to3` module is used for automatically converting Python 2 code to Python 3 code. It provides tools and utilities to help developers transition their codebases from Python 2 to Python 3, ensuring compatibility and reducing the need for manual modifications. Below are comprehensive examples demonstrating various functionalities of the `2to3` module.

### Example 1: Basic Conversion with a Script

#### Description:
This example demonstrates how to use the `2to3` tool as a script in your application to convert Python 2 code to Python 3.

```python
import sys
from lib2to3.main import main

# Define the directory containing the Python 2 files to be converted
input_dir = 'path/to/your/python2/code'

# Define the directory where the converted Python 3 files will be saved
output_dir = 'path/to/your/python3/code'

# Run the conversion process
main("lib2to3.fixes", [input_dir, output_dir])
```

#### Explanation:
- **`import sys`**: Imports the `sys` module to access command-line arguments.
- **`from lib2to3.main import main`**: Imports the `main` function from the `lib2to3` module.
- **`input_dir` and `output_dir`**: Define the directories where the Python 2 files are located and where the converted files will be saved, respectively.
- **`main("lib2to3.fixes", [input_dir, output_dir])`**: Calls the `main` function to perform the conversion. The first argument is a list of fixers (modules) to apply during the conversion, and the second argument is a list of directories containing the Python 2 files.

### Example 2: Using Fixers Manually

#### Description:
This example shows how to manually use the `fixer` classes provided by the `lib2to3` module to convert specific parts of your code.

```python
import lib2to3
from lib2to3 import fix_all, pytree, refactor

# Define the file path containing Python 2 code
file_path = 'path/to/your/python2/file.py'

# Create a parser object for the input file
with open(file_path, 'rb') as f:
    tree = pytree.parse(f.read())

# Define the fixers to apply
fixers_to_apply = [lib2to3.fixes.fix_print, lib2to3.fixes.fix_raw_input]

# Create a refactoring context
context = refactor.RefactorContext()

# Apply the fixers to the input tree
refactor.apply_fixes(tree, fixers_to_apply, context)

# Output the modified code to a new file
with open('path/to/your/python3/file.py', 'w') as f:
    f.write(str(tree))
```

#### Explanation:
- **`import lib2to3`**: Imports the `lib2to3` module.
- **`from lib2to3 import fix_all, pytree, refactor`**: Imports the necessary classes and functions from `lib2to3`.
- **`file_path`**: Specifies the path to the Python 2 file that needs to be converted.
- **`with open(file_path, 'rb') as f:`**: Opens the file in binary read mode to parse it using `pytree.parse()`.
- **`fixers_to_apply`**: A list of fixers that will be applied to the parsed tree. In this example, `fix_print` and `fix_raw_input` are used.
- **`refactor.RefactorContext()`**: Creates a refactoring context.
- **`refactor.apply_fixes(tree, fixers_to_apply, context)`**: Applies the specified fixers to the parse tree.
- **`with open('path/to/your/python3/file.py', 'w') as f:`**: Opens a new file in write mode and writes the modified tree back to it.

### Example 3: Running 2to3 on Multiple Files

#### Description:
This example demonstrates how to run `2to3` on multiple files at once using the `fix_all` function.

```python
import lib2to3

# Define a list of file paths containing Python 2 code
file_paths = ['path/to/your/python2/file1.py', 'path/to/your/python2/file2.py']

# Run the conversion process on all specified files
fix_all(file_paths, fixers_to_apply=["lib2to3.fixes.fix_print"])
```

#### Explanation:
- **`import lib2to3`**: Imports the `lib2to3` module.
- **`file_paths`**: A list of paths to the Python 2 files that need to be converted.
- **`fix_all(file_paths, fixers_to_apply=["lib2to3.fixes.fix_print"])`**: Applies all fixers specified in the `fixers_to_apply` list to each file in the `file_paths` list.

### Example 4: Using 2to3 as a Command-line Tool

#### Description:
This example shows how to use the `2to3` tool as a command-line utility, which is often more convenient for large codebases.

```bash
# Run the conversion process from the command line
python -m lib2to3.fixes.fix_print path/to/your/python2/code path/to/your/python3/code
```

#### Explanation:
- **`python -m lib2to3.fixes.fix_print path/to/your/python2/code path/to/your/python3/code`**: Invokes the `fix_print` fixer on all files in `path/to/your/python2/code` and saves the converted files to `path/to/your/python3/code`.

These examples cover various aspects of using the `2to3` module, from basic script usage to manual application of fixers and running conversions on multiple files.
