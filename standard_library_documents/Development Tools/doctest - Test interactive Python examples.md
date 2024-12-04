# doctest — Test interactive Python examples

**doctest Module**
====================

The `doctest` module provides a way to run interactive Python examples as test cases.

### Installation

You don't need to install anything, as this is a standard library module in Python.

### Example Use Cases

1. **Running doctests**: You can use the `doctest` module to run your interactive Python examples as tests.
2. **Writing custom test cases**: You can write your own test cases using the `doctest` module.

### Code Examples
```python
import doctest

# Interactive example from the docstring of a function
def greet(name):
    """Prints out a personalized greeting."""
    print(f"Hello, {name}!")

def main():
    # Running the interactive example as a test case
    result = doctest.testmod(greet)
    if result.failures:
        print("Test cases failed:", result.failures)

if __name__ == "__main__":
    main()
```

### Explanation

In this code:

1. We import the `doctest` module.
2. We define a simple function `greet` that prints out a personalized greeting.
3. The docstring of the `greet` function is used as a test case to verify its correctness.
4. In the `main` function, we use `doctest.testmod(greet)` to run the interactive example as a test case.
5. If any test cases fail, their failure messages are printed out.

### Additional Example: Writing Custom Test Cases

```python
import doctest

# Interactive example from the docstring of a function
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def main():
    # Writing our own test case
    def test_add():
        result = add(2, 3)
        assert result == 5, "Test failed"
        print("Addition test passed")

    # Running our custom test case
    doctest.testmod(add, module='test_add', optionflags=doctest.ELLIPSIS)

if __name__ == "__main__":
    main()
```

### Explanation

In this code:

1. We import the `doctest` module.
2. We define a simple function `add` that returns the sum of two numbers.
3. In the `main` function, we write our own test case using a custom function `test_add`.
4. We use `doctest.testmod(add, ...)`, specifying our custom test case and some additional options (`optionflags=doctest.ELLIPSIS`).
