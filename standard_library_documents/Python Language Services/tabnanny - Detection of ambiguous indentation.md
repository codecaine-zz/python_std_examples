# tabnanny - Detection of ambiguous indentation
## Table of Contents

1. [1. Basic Usage](#1-basic-usage)
2. [2. Custom Indentation Check](#2-custom-indentation-check)
3. [3. Checking Multiple Files](#3-checking-multiple-files)
4. [4. Skipping Lines](#4-skipping-lines)
5. [5. Handling Output](#5-handling-output)
6. [6. Using `tabnanny` as a Command-Line Tool](#6-using-tabnanny-as-a-command-line-tool)
7. [7. Customizing the Output Format](#7-customizing-the-output-format)



The `tabnanny` module is used to detect and report on ambiguous indentation in Python scripts. Ambiguous indentation can lead to errors or unexpected behavior, so it's important to ensure consistent indentation in your code. Below are comprehensive examples demonstrating various functionalities of the `tabnanny` module.

### 1. Basic Usage

The simplest use case for `tabnanny` is to check a file for ambiguous indentation and report any issues.

```python
import tabnanny

# Path to the Python script you want to check
file_path = 'example.py'

# Run the check on the specified file
problems = tabnanny.check(open(file_path))

if problems:
    print("Ambiguous indentation found:")
    for problem in problems:
        print(problem)
else:
    print("No ambiguous indentation issues found.")
```

### 2. Custom Indentation Check

You can specify a custom indentation size when checking the file.

```python
import tabnanny

# Path to the Python script you want to check
file_path = 'example.py'

# Specify a custom indentation size (e.g., 4 spaces)
custom_indent_size = 4

# Run the check with a specified indentation size
problems = tabnanny.check(open(file_path), width=custom_indent_size)

if problems:
    print("Ambiguous indentation found:")
    for problem in problems:
        print(problem)
else:
    print("No ambiguous indentation issues found.")
```

### 3. Checking Multiple Files

You can check multiple files at once by providing a list of file paths.

```python
import tabnanny

# List of Python script paths you want to check
file_paths = ['example1.py', 'example2.py']

# Run the check on the specified files
problems = tabnanny.check([open(file_path) for file_path in file_paths])

if problems:
    print("Ambiguous indentation found:")
    for problem in problems:
        print(problem)
else:
    print("No ambiguous indentation issues found.")
```

### 4. Skipping Lines

You can specify lines to skip during the check by providing a list of line numbers.

```python
import tabnanny

# Path to the Python script you want to check
file_path = 'example.py'

# Specify lines to skip
lines_to_skip = [1, 5]  # Skip lines 1 and 5

# Run the check with specified lines to skip
problems = tabnanny.check(open(file_path), skip=[line - 1 for line in lines_to_skip])

if problems:
    print("Ambiguous indentation found:")
    for problem in problems:
        print(problem)
else:
    print("No ambiguous indentation issues found.")
```

### 5. Handling Output

You can handle the output of the check using a custom function.

```python
import tabnanny

def print_problem(problem):
    print(f"Line: {problem.line}, Column: {problem.column}, Indent: {problem.indent}")

# Path to the Python script you want to check
file_path = 'example.py'

# Run the check and handle each problem using a custom function
problems = tabnanny.check(open(file_path), line_handler=print_problem)

if problems:
    print("Ambiguous indentation found.")
else:
    print("No ambiguous indentation issues found.")
```

### 6. Using `tabnanny` as a Command-Line Tool

You can use `tabnanny` as a command-line tool to check files directly.

```sh
# Run tabnanny on a file
python -m tabnanny example.py

# Check multiple files using a wildcard
python -m tabnanny *.py
```

### 7. Customizing the Output Format

You can customize the output format by providing a custom handler function.

```python
import tabnanny

def print_custom(problem):
    print(f"Line: {problem.line}, Indent: {problem.indent}, Reason: {problem.reason}")

# Path to the Python script you want to check
file_path = 'example.py'

# Run the check with a custom line handler and format
problems = tabnanny.check(open(file_path), line_handler=print_custom, width=4)

if problems:
    print("Ambiguous indentation found:")
else:
    print("No ambiguous indentation issues found.")
```

These examples cover various scenarios for using `tabnanny` to detect and report on ambiguous indentation in Python scripts. By following these examples, you can effectively use `tabnanny` to maintain clean and consistent code indentation across your projects.
