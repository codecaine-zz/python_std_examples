# compileall - Byte-compile Python libraries

The `compileall` module in Python is used to byte-compile all modules within a specified directory, which can help improve the performance of your Python application by compiling source files into bytecode during execution. Below are comprehensive code examples for using the `compileall` module.

### Example 1: Byte-Compile All Modules in a Directory

This example demonstrates how to use `compileall.compile_dir()` to byte-compile all modules in a directory.

```python
import compileall

# Specify the directory to be compiled
directory_to_compile = '/path/to/your/python/library'

# Compile all Python files in the specified directory
compiled_files = compileall.compile_dir(directory=directory_to_compile)

# Print the list of compiled files
print("Compiled files:", compiled_files)
```

### Explanation:

1. **Import `compileall`:** Start by importing the `compileall` module.
2. **Specify the Directory:** Define the path to the directory containing your Python modules that you want to compile.
3. **Compile All Files:** Use `compileall.compile_dir()` with the specified directory. This function returns a list of filenames that were compiled.
4. **Print Compiled Files:** Print the list of files that were successfully compiled.

### Example 2: Byte-Compile Only Modified Modules

This example shows how to use `compileall.compile_dir()` with the `force` parameter to byte-compile only modified modules since the last compilation.

```python
import compileall

# Specify the directory to be compiled
directory_to_compile = '/path/to/your/python/library'

# Compile only modified files, including those that were already compiled but have been updated
compiled_files = compileall.compile_dir(directory=directory_to_compile, force=True)

# Print the list of compiled files
print("Compiled files:", compiled_files)
```

### Explanation:

1. **Import `compileall`:** Again, import the `compileall` module.
2. **Specify the Directory:** Define the path to the directory containing your Python modules.
3. **Compile Only Modified Files:** Use `compileall.compile_dir()` with the `force=True` parameter. This ensures that only files that have been modified since their last compilation are compiled again.
4. **Print Compiled Files:** Print the list of files that were successfully compiled, including any that were already present but updated.

### Example 3: Compile All Modules in a Directory and Output Errors to a File

This example demonstrates how to use `compileall.compile_dir()` with an output file to capture any errors that occur during compilation.

```python
import compileall

# Specify the directory to be compiled
directory_to_compile = '/path/to/your/python/library'

# Specify the output file for error messages
output_file = 'compile_errors.txt'

# Compile all Python files in the specified directory and write errors to a file
compiled_files, errors = compileall.compile_dir(directory=directory_to_compile, force=True, quiet=False)

# Print the list of compiled files and any errors encountered
print("Compiled files:", compiled_files)
print("Errors:")
for error in errors:
    print(error)
```

### Explanation:

1. **Import `compileall`:** Import the `compileall` module.
2. **Specify the Directory:** Define the path to the directory containing your Python modules.
3. **Compile All Files and Capture Errors:** Use `compileall.compile_dir()` with `force=True` and `quiet=False`. The `quiet=False` parameter ensures that errors are printed during compilation, and the results are also captured in a file specified by `output_file`.
4. **Print Compiled Files and Errors:** Print the list of files that were compiled and any error messages that occurred.

### Example 4: Compile All Modules in a Directory with Optimization

This example shows how to use `compileall.compile_dir()` to byte-compile all modules in a directory, optimizing them for performance.

```python
import compileall

# Specify the directory to be compiled
directory_to_compile = '/path/to/your/python/library'

# Compile all Python files in the specified directory with optimization level 2
compiled_files = compileall.compile_dir(directory=directory_to_compile, force=True, optimize=2)

# Print the list of compiled files
print("Compiled files:", compiled_files)
```

### Explanation:

1. **Import `compileall`:** Import the `compileall` module.
2. **Specify the Directory:** Define the path to the directory containing your Python modules.
3. **Compile All Files with Optimization:** Use `compileall.compile_dir()` with `force=True` and `optimize=2`. The optimization level 2 enables more aggressive optimizations, which can improve performance.
4. **Print Compiled Files:** Print the list of files that were successfully compiled.

These examples provide a comprehensive overview of using the `compileall` module in Python to byte-compile your Python libraries. Each example demonstrates different use cases and options available for fine-tuning the compilation process.
