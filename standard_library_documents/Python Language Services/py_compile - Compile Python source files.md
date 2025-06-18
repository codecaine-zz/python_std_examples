# py_compile - Compile Python source files
## Table of Contents

1. [Example 1: Compile a Single Source File](#example-1-compile-a-single-source-file)
2. [Example 2: Compile Multiple Source Files in a Directory](#example-2-compile-multiple-source-files-in-a-directory)
3. [Example 3: Compile a Source File with Specific Options](#example-3-compile-a-source-file-with-specific-options)
4. [Example 4: Check if a File is Already Compiled](#example-4-check-if-a-file-is-already-compiled)
5. [Example 5: Compile a Source File with Specific Mode](#example-5-compile-a-source-file-with-specific-mode)



The `py_compile` module in Python's standard library provides a simple way to compile Python source files into bytecode using the built-in compiler. This is useful for distributing Python programs, as it allows you to distribute only the compiled bytecode instead of the source code. Below are several examples demonstrating various functionalities of the `py_compile` module.

### Example 1: Compile a Single Source File

```python
import py_compile

# Specify the source file and its output path (compiled bytecode)
source_file = 'example.py'
bytecode_file = 'example.pyc'

try:
    # Compile the source file into bytecode
    py_compile.compile(source_file, outdir=bytecode_file)
    print(f"Source file '{source_file}' compiled to '{bytecode_file}'.")
except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")
except Exception as e:
    print(f"An error occurred during compilation: {e}")
```

### Example 2: Compile Multiple Source Files in a Directory

```python
import py_compile
import os

# Specify the directory containing source files and the output directory for bytecode
src_dir = 'src'
bytecode_dir = 'build'

try:
    # Ensure the output directory exists
    if not os.path.exists(bytecode_dir):
        os.makedirs(bytecode_dir)

    # Compile all .py files in the source directory into bytecode
    for filename in os.listdir(src_dir):
        if filename.endswith('.py'):
            py_compile.compile(os.path.join(src_dir, filename), outdir=bytecode_dir)
            print(f"Compiled {filename} to {os.path.join(bytecode_dir, filename)}")
except FileNotFoundError:
    print("Error: Source directory not found.")
except Exception as e:
    print(f"An error occurred during compilation: {e}")
```

### Example 3: Compile a Source File with Specific Options

```python
import py_compile

# Specify the source file and its output path (compiled bytecode)
source_file = 'example.py'
bytecode_file = 'example.pyc'

try:
    # Compile the source file into bytecode with optimization enabled
    py_compile.compile(source_file, outdir=bytecode_dir, optimize=2)
    print(f"Source file '{source_file}' compiled to '{bytecode_file}' with optimization level 2.")
except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print(f"An error occurred during compilation: {e}")
```

### Example 4: Check if a File is Already Compiled

```python
import py_compile

# Specify the source and bytecode files
source_file = 'example.py'
bytecode_file = 'example.pyc'

if py_compile.is_compiled(source_file):
    print(f"{source_file} is already compiled to {bytecode_file}.")
else:
    print(f"{source_file} is not yet compiled.")
```

### Example 5: Compile a Source File with Specific Mode

```python
import py_compile

# Specify the source file and its output path (compiled bytecode)
source_file = 'example.py'
bytecode_file = 'example.pyc'

try:
    # Compile the source file into bytecode using the standard compiler mode
    py_compile.compile(source_file, outdir=bytecode_dir, modname='example')
    print(f"Source file '{source_file}' compiled to '{bytecode_dir}/__pycache__/example.cpython-312-py3-none-any.pyc' with module name 'example'.")
except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print(f"An error occurred during compilation: {e}")
```

These examples cover basic use cases for the `py_compile` module, including compiling a single source file, multiple files in a directory, specifying optimization levels, checking if a file is already compiled, and using a specific mode for compilation. Each example includes error handling to manage potential issues such as missing files or compilation errors.
