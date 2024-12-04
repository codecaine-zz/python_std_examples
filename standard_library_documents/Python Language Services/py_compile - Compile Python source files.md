# py_compile — Compile Python source files

Here's an example of how you can use `compile` function from `py_compile` module:

```python
# Import the compile function from py_compile module
from py_compile import compile

def main():
    # Create a string containing Python code
    code = """
    def add(a, b):
        return a + b
    
    print(add(3, 4))
    """

    try:
        # Compile the code with Python 3.9 as target Python version
        compiled_code = compile(code, '<string>', 'exec', {'__builtins__': None})

        # Execute the compiled code
        exec(compiled_code)

    except SyntaxError as e:
        print(f"Syntax error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This example demonstrates how to compile a Python source string into bytecode and execute it.

### Compiling and Running a Script

To compile and run a Python script, you can use the following code:

```python
# Import the compile function from py_compile module
from py_compile import compile

def main():
    # Specify the path to your Python script
    script_path = 'example.py'

    try:
        # Open the script file in read mode
        with open(script_path, 'r') as file:
            # Read the contents of the script
            code = file.read()

        # Compile the code with Python 3.9 as target Python version
        compiled_code = compile(code, script_path, 'exec')

        # Execute the compiled code
        exec(compiled_code)

    except FileNotFoundError as e:
        print(f"The file {script_path} was not found: {e}")
    except SyntaxError as e:
        print(f"Syntax error in {script_path}: {e}")
    except Exception as e:
        print(f"An error occurred while executing the script: {e}")

if __name__ == "__main__":
    main()
```

This example compiles and executes a Python script by reading it from a file.

### Compiling a Module

To compile a Python module, you can use the following code:

```python
# Import the compile function from py_compile module
from py_compile import compile

def main():
    # Specify the path to your Python module
    module_path = 'example.py'

    try:
        # Compile the module with Python 3.9 as target Python version
        compiled_module = compile(open(module_path).read(), module_path, 'exec')

        # Execute the compiled module
        exec(compiled_module)

    except FileNotFoundError as e:
        print(f"The file {module_path} was not found: {e}")
    except SyntaxError as e:
        print(f"Syntax error in {module_path}: {e}")
    except Exception as e:
        print(f"An error occurred while executing the module: {e}")

if __name__ == "__main__":
    main()
```

This example compiles a Python module and executes it.

### Using compile with other Options

You can use different options when compiling Python source files using `compile` function:

*   `mode`: Specifies the execution mode. Options are `'exec'`, `'eval'`, and `'single'.
*   `filenames`: A list of filenames to be compiled.
*   `dumps`: If `True`, generates a byte string containing the compiled code.

Here's an example using `compile` with different options:

```python
# Import the compile function from py_compile module
from py_compile import compile

def main():
    # Create a string containing Python code
    code = """
    def add(a, b):
        return a + b
    
    print(add(3, 4))
    """

    try:
        # Compile the code with Python 3.9 as target Python version and 'exec' mode
        compiled_code_exec = compile(code, '<string>', 'exec', {'__builtins__': None})

        # Compile the code with Python 3.9 as target Python version and 'eval' mode
        compiled_code_eval = compile(code, '<string>', 'eval', {'__builtins__': None})

        # Compile the code with Python 3.9 as target Python version and 'single' mode
        compiled_code_single = compile(code, '<string>', 'single')

    except SyntaxError as e:
        print(f"Syntax error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This example demonstrates how to use `compile` function with different modes.

### Compiling and Running a Script in a Loop

You can compile and run a Python script in a loop using the following code:

```python
# Import the compile function from py_compile module
from py_compile import compile

def main():
    # Specify the path to your Python script
    script_path = 'example.py'

    try:
        # Open the script file in read mode
        with open(script_path, 'r') as file:
            # Read the contents of the script
            code = file.read()

        # Compile the code with Python 3.9 as target Python version
        compiled_code = compile(code, script_path, 'exec')

        # Number of times to execute the script
        num_executions = 5

        for i in range(num_executions):
            # Execute the compiled code
            exec(compiled_code)

    except FileNotFoundError as e:
        print(f"The file {script_path} was not found: {e}")
    except SyntaxError as e:
        print(f"Syntax error in {script_path}: {e}")
    except Exception as e:
        print(f"An error occurred while executing the script: {e}")

if __name__ == "__main__":
    main()
```

This example compiles and executes a Python script multiple times.
