# doctest - Test interactive Python examples
## Table of Contents

1. [Example 1: Basic Usage](#example-1-basic-usage)
2. [Example 2: Testing Functions with More Complex Arguments](#example-2-testing-functions-with-more-complex-arguments)
3. [Example 3: Testing Functions with Lists and Tuples](#example-3-testing-functions-with-lists-and-tuples)
4. [Example 4: Testing Functions with String Manipulation](#example-4-testing-functions-with-string-manipulation)
5. [Example 5: Testing Functions with Conditional Logic](#example-5-testing-functions-with-conditional-logic)
6. [Example 6: Testing Functions with Class Methods](#example-6-testing-functions-with-class-methods)
7. [Example 7: Testing Functions with External Modules](#example-7-testing-functions-with-external-modules)
8. [Example 8: Testing Functions with Assertions](#example-8-testing-functions-with-assertions)



The `doctest` module in Python is a testing framework that provides tools to run and verify tests written as docstrings in Python modules, classes, functions, and methods. It is particularly useful for verifying that the examples provided in docstrings are correct and up-to-date.

Below are comprehensive code examples demonstrating various functionalities of the `doctest` module:

### Example 1: Basic Usage

```python
import doctest
import unittest

def add(a, b):
    """
    >>> add(1, 2)
    3
    >>> add(5, 7)
    12
    """
    return a + b

# Run the doctests in the module
doctest.testmod()
```

### Example 2: Testing Functions with More Complex Arguments

```python
def multiply(a, b):
    """
    >>> multiply(3, 4)
    12
    >>> multiply(-2, 5)
    -10
    """
    return a * b

# Run the doctests in the module
doctest.testmod()
```

### Example 3: Testing Functions with Lists and Tuples

```python
def sort_and_filter(numbers):
    """
    Sorts a list of numbers in ascending order and filters out even numbers.
    
    >>> sort_and_filter([5, 3, 8, 1, 4])
    [1, 3, 5]
    """
    return sorted(filter(lambda x: x % 2 != 0, numbers))

# Run the doctests in the module
doctest.testmod()
```

### Example 4: Testing Functions with String Manipulation

```python
def reverse_string(s):
    """
    Reverses a given string.
    
    >>> reverse_string('hello')
    'olleh'
    >>> reverse_string('Python')
    'nohtyP'
    """
    return s[::-1]

# Run the doctests in the module
doctest.testmod()
```

### Example 5: Testing Functions with Conditional Logic

```python
def is_positive(n):
    """
    Determines if a number is positive.
    
    >>> is_positive(10)
    True
    >>> is_positive(-3)
    False
    """
    return n > 0

# Run the doctests in the module
doctest.testmod()
```

### Example 6: Testing Functions with Class Methods

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

# Define the class and its method docstrings
doc = """
Calculator class provides basic arithmetic operations.

>>> calc = Calculator()
>>> calc.add(3, 4)
7
>>> calc.multiply(5, 6)
30
"""

# Run the doctests in the module
doctest.testmod()

# Optionally, you can run the doctests using unittest framework
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(3, 4), 7)

    def test_multiply(self):
        self.assertEqual(Calculator().multiply(5, 6), 30)

# Run the tests
unittest.main(argv=[''], exit=False)
```

### Example 7: Testing Functions with External Modules

```python
def parse_json(json_str):
    """
    Parses a JSON string and returns a Python dictionary.
    
    >>> data = parse_json('{"name": "John", "age": 30}')
    {'name': 'John', 'age': 30}
    """
    import json
    return json.loads(json_str)

# Run the doctests in the module
doctest.testmod()
```

### Example 8: Testing Functions with Assertions

```python
def check_even(num):
    """
    Asserts that a number is even.
    
    >>> check_even(4)
    True
    >>> check_even(7)
    Traceback (most recent call last):
        ...
    AssertionError: 7 is not even
    """
    assert num % 2 == 0, f"{num} is not even"

# Run the doctests in the module
doctest.testmod()
```

These examples cover various scenarios and functionalities of the `doctest` module. Each example includes a docstring with test cases that are verified by running the `testmod()` function or using an external testing framework like `unittest`. This approach ensures that the documentation is self-contained and easily verifiable.
