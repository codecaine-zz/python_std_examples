# inspect - Inspect live objects

The `inspect` module in Python provides several functions to access information about live objects such as modules, classes, methods, and frames. Below are comprehensive examples demonstrating various functionalities of the `inspect` module:

```python
import inspect

# Example 1: Get the source code of a function
def example_function(x):
    """A simple function for demonstration."""
    return x * 2

source_code = inspect.getsource(example_function)
print("Source code of example_function:")
print(source_code)

# Example 2: Check if an object is a class
class MyClass:
    pass

is_class = inspect.isclass(MyClass)
print(f"Is MyClass a class? {is_class}")

# Example 3: Get the docstring of a function
docstring = inspect.getdoc(example_function)
print("Docstring of example_function:")
print(docstring)

# Example 4: Get the argument specification of a function
argspec = inspect.signature(example_function)
print("Argument specification of example_function:")
for param in argspec.parameters.values():
    print(f"Parameter name: {param.name}, Default value: {param.default}")

# Example 5: Get the module containing a class or function
module_name = inspect.getmodule(MyClass).__name__
print(f"The module containing MyClass is: {module_name}")

# Example 6: List all functions and classes in a module
import math

for name, obj in inspect.getmembers(math):
    if inspect.isfunction(obj) or inspect.isclass(obj):
        print(name)

# Example 7: Get the current stack frame information
frame = inspect.currentframe()
print("Current stack frame details:")
print(frame.f_code.co_filename)
print(frame.f_lineno)
print(frame.f_locals)

# Example 8: Get all local variables in the current stack frame
locals_vars = frame.f_locals.copy()  # Create a copy of the dictionary
print("Local variables in the current stack frame:")
for key, value in locals_vars.items():
    print(f"{key}: {value}")

# Example 9: Trace execution of a function using inspect.getsource and eval
def trace_function(func):
    source = inspect.getsource(func)
    # Replace 'func' with its source code to simulate execution
    exec(source)

trace_function(example_function)

# Example 10: Get the file path where an object was defined
file_path = inspect.getmodule(example_function).__file__
print(f"The file path of example_function is: {file_path}")

# Example 11: Check if an object is a frame
is_frame = inspect.isframe(inspect.currentframe())
print(f"Is current frame? {is_frame}")
```

### Explanation:

- **Source Code**: `inspect.getsource` retrieves the source code of a function or method, allowing you to see the exact code that was written.
- **Class/Function Checks**: `inspect.isclass` and `inspect.isfunction` determine if an object is a class or function, respectively, which is useful for type checking and validation.
- **Docstring**: `inspect.getdoc` fetches the docstring of a function, providing a way to access the documentation string for better understanding of the function's purpose.
- **Argument Specification**: `inspect.signature` provides detailed information about the parameters of a function, including their names and default values, which is helpful for introspection and debugging.
- **Module Information**: `inspect.getmodule` returns the module where a class or function is defined, giving context about where the object originates from.
- **Member List**: `inspect.getmembers` lists all members (functions and classes) in a module, which can be used to dynamically explore the contents of a module.
- **Stack Frame Details**: `inspect.currentframe`, `f_code.co_filename`, `f_lineno`, and `f_locals` provide information about the current stack frame, useful for debugging and understanding the state of the program at a specific point in time.
- **Local Variables**: `frame.f_locals` gives access to the local variables of the current stack frame, allowing inspection of the current state of local variables.
- **Execution Tracing**: By simulating execution, `inspect.getsource` can be used to trace the flow of a function, which is useful for debugging and understanding how a function operates.
- **File Path**: `inspect.getmodule` returns the file path where an object is defined, providing information about the location of the source code.
- **Frame Check**: `inspect.isframe` checks if an object is a frame, which can be used to validate and work with frame objects in the current execution context.

These examples cover various aspects of inspecting live objects in Python, providing a comprehensive overview of its capabilities.
