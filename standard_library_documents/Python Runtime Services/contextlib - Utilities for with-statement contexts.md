# contextlib — Utilities for with-statement contexts

Here's an example of how you can use the `contextlib` module from Python's standard library.

```python
import contextlib

# Define a function that uses contextlib to create a context manager
@contextlib.contextmanager
def my_context_manager():
    """
    A simple context manager that prints a message before entering and after exiting the context.
    """
    print("Entering the context")
    try:
        # Yield control to the caller within this block
        yield
    finally:
        print("Exiting the context")

# Example usage of the context manager
with my_context_manager():
    # Code that should be executed within the context
    print("Inside the context")

# Another example using the contextlib.suppress function
@contextlib.contextmanager
def suppress_warnings():
    """
    A context manager that suppresses warnings during execution.
    """
    import warnings
    warnings.simplefilter('ignore')
    try:
        # Yield control to the caller within this block
        yield
    finally:
        warnings.simplefilter(*warnings.defaultFilters())

with suppress_warnings():
    # Code that may produce warnings
    raise ValueError("This should not be a warning")
```

However, you can also create your own custom context manager using `contextlib.contextmanager`.

```python
import contextlib

@contextlib.contextmanager
def my_custom_context_manager(open_file):
    """
    A custom context manager that opens a file and closes it when exiting the context.
    """
    print("Opening the file")
    with open_file as f:
        # Yield control to the caller within this block
        yield
    print("Closing the file")

# Example usage of the custom context manager
with my_custom_context_manager(open('example.txt', 'r')) as f:
    # Code that should be executed within the context
    data = f.read()
```

Here's a more complex example that combines multiple `contextlib` features.

```python
import contextlib
from contextlib import suppress, redirect_stdout

@contextlib.contextmanager
def with_output redirected():
    """
    A context manager that redirects stdout during execution.
    """
    with suppress(IOError):
        with open('/dev/null', 'w') as f:
            # Yield control to the caller within this block
            yield from redirect_stdout(f)

# Example usage of the context manager
with with_output_redirected():
    # Code that may produce output
    import math
    print(math.sqrt(-1))
```

Here's a more complex example that uses `contextlib.suppress` and `redirect_stdout` to capture exceptions.

```python
import contextlib

@contextlib.contextmanager
def suppress_exceptions_and_capture_output():
    """
    A context manager that captures exceptions and redirects stdout during execution.
    """
    with suppress(Exception):
        with redirect_stdout(sys.stdout):
            # Yield control to the caller within this block
            yield

# Example usage of the context manager
with suppress_exceptions_and_capture_output():
    # Code that may raise an exception
    import math
    print(math.sqrt(-1))
```
