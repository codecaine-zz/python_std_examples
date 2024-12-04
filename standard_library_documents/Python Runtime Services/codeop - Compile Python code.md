# codeop - Compile Python code

The `codeop` module in Python provides tools to compile Python source code into bytecode. It's particularly useful for situations where you need to dynamically execute or modify Python code at runtime, such as in interactive shells, interpreters, or during the execution of custom scripts.

Below are some comprehensive examples that demonstrate various functionalities provided by the `codeop` module:

### Example 1: Basic Compilation and Execution

```python
import codeop

# Define a Python source code string
source_code = """
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
"""

# Compile the source code into bytecode using codeop.compile_command
code_ast = codeop.compile_command(source_code)

# Execute the compiled bytecode to call the function and display output
result = eval(code_ast)
print(result)  # Output: Hello, Alice!
```

### Example 2: Compiling Source Code with Specific Mode

```python
import codeop

# Define a Python source code string
source_code = """
def add(x, y):
    return x + y
"""

# Compile the source code into bytecode using a specific mode (e.g., 'exec')
code_ast = codeop.compile_command(source_code, mode='exec')

# Execute the compiled bytecode to define the function
eval(code_ast)

# Call the function and display output
result = add(3, 5)
print(result)  # Output: 8
```

### Example 3: Compiling Source Code into Bytecode Without Executing

```python
import codeop

# Define a Python source code string
source_code = """
def multiply(x, y):
    return x * y
"""

# Compile the source code into bytecode using codeop.compile_command
code_ast = codeop.compile_command(source_code)

# The result is a syntax tree (AST) node, not executable bytecode
print(code_ast)
```

### Example 4: Handling Syntax Errors Gracefully

```python
import codeop

# Define a Python source code string with an error
source_code_with_error = """
def divide(x, y):
    return x / y
"""

try:
    # Compile the source code into bytecode
    code_ast = codeop.compile_command(source_code_with_error)
except SyntaxError as e:
    print(f"Compilation error: {e}")
```

### Example 5: Compiling and Executing Dynamically

```python
import codeop

# Define a function to compile and execute Python source code dynamically
def run_python_code(code):
    try:
        # Compile the source code into bytecode
        code_ast = codeop.compile_command(code)
        
        # Execute the compiled bytecode to call the function or execute statements
        result = eval(code_ast)
        return result
    except SyntaxError as e:
        print(f"Compilation error: {e}")
        return None

# Example usage of the run_python_code function
code_to_run = """
def square(x):
    return x * x

result = square(4)
print(result)  # Output: 16
"""
output = run_python_code(code_to_run)
print(output)  # Output: 16
```

### Example 6: Using `compile_command` with Specific Mode and Flags

```python
import codeop

# Define a Python source code string
source_code = """
x = 10
y = 20
"""

# Compile the source code into bytecode using a specific mode ('exec') and flags (optimize)
code_ast = codeop.compile_command(source_code, mode='exec', flags=codeop.OPTIMIZE)

# Execute the compiled bytecode to define variables
eval(code_ast)

# Access and print variables from the compiled environment
print(x)  # Output: 10
print(y)  # Output: 20
```

### Example 7: Using `compile_command` with Input File

```python
import codeop

# Define a file path containing Python source code
file_path = 'example.py'

# Compile the content of the file into bytecode using codeop.compile_file
with open(file_path, 'r') as file:
    file_content = file.read()
    code_ast = codeop.compile_file(file_content)

# Execute the compiled bytecode from the file
eval(code_ast)
```

These examples cover a range of use cases for the `codeop` module, including basic compilation and execution, handling syntax errors gracefully, dynamically compiling and executing Python code, and using the module with specific modes and flags. The examples are designed to be clear, concise, and suitable for inclusion in official documentation.
