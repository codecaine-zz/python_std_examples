# 2to3 — Automated Python 2 to 3 code translation

Here are some examples of what can be done using the `2to3` module from the standard library:

```python
# Importing the 2to3 module
from 2to3 import fix_code

def translate_to_3():
    # Writing a simple Python expression to convert
    expr = "print 'Hello World!'"

    # Fixing the code using 2to3
    fixed_expr = fix_code(expr, None, None)

    print(f"Original Expression: {expr}")
    print(f"Fixed Expression: {fixed_expr}")

# Translating a Python class to use __init__ and self
def translate_class():
    class MyClass:
        def __init__(self, x, y):
            pass

    # Using 2to3 to convert the class
    fixed_class = fix_code("class MyClass:\n    def __init__(self, x, y):\n        pass", None, None)

    print(f"Original Class:\n{fixed_class}")

# Translating a Python function with default arguments
def translate_function():
    def add(x=0, y=0):
        return x + y

    # Using 2to3 to convert the function
    fixed_function = fix_code("def add(x=0, y=0):\n    return x + y", None, None)

    print(f"Original Function:\n{fixed_function}")

# Translating a Python module using find_all_and_fix
def translate_module():
    # Find all and fix the code in a given module
    import os
    file_path = "path_to_your_module.py"

    if not os.path.exists(file_path):
        print("File does not exist.")
    elif not os.path.isfile(file_path):
        print("Path is not a file.")
    else:
        # Using 2to3 to fix the code in the module
        fixed_file = fix_code(open(file_path).read(), None, None)

        # Writing the fixed code back to the file
        with open(file_path, "w") as f:
            f.write(fixed_file)
```

Here is how you can use it:

1.  Install `2to3` module if not already installed: You can install it via pip command.

    ```bash
pip install -U 2to3
```
2.  Usage of the above code examples and make necessary modifications according to your needs.
3.  To convert a specific Python file, you need to provide the path of that file. 

This is an overview of what can be done using `2to3` module from the standard library in python. For more information, refer to [Python's Official Documentation for 2to3](https://docs.python.org/3/library/2to3/index.html).
