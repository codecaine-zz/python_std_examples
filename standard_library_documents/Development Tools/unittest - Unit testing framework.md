# unittest — Unit testing framework

**Unit Testing Framework: `unittest`**
=====================================

The `unittest` module is a built-in Python framework for writing and running unit tests.

### Example 1: Basic Usage
```python
import unittest

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_mixed_numbers(self):
        """Test adding a mix of positive and negative numbers."""
        self.assertEqual(add_numbers(-2, 3), 1)

if __name__ == '__main__':
    unittest.main()
```
### Explanation

* We define a simple `add_numbers` function that takes two arguments.
* We create a test class `TestAddNumbers` that inherits from `unittest.TestCase`.
* In the `test_add_positive_numbers`, `test_add_negative_numbers`, and `test_add_mixed_numbers` methods, we use the `assertEqual` method to verify that our `add_numbers` function behaves as expected.

### Example 2: Using Assert Methods
```python
import unittest

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        # Use assertEqual to check for equality
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        # Use assertNotEqual to check for inequality
        self.assertNotEqual(add_numbers(-2, -3), -1)
        # Use assertTrue to check for truthiness
        self.assertTrue(add_numbers(-2, 0) > 0)

if __name__ == '__main__':
    unittest.main()
```
### Explanation

* We use different `assert` methods to verify our test cases:
	+ `assertEqual`: checks if two values are equal.
	+ `assertNotEqual`: checks if two values are not equal.
	+ `assertTrue`: checks if a value is true (non-zero, non-empty string, etc.).

### Example 3: Testing Exceptions
```python
import unittest

def divide_numbers(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

class TestDivideNumbers(unittest.TestCase):
    def test_divide_positive_numbers(self):
        # Use assertRaises to check for exception
        with self.assertRaises(ValueError):
            divide_numbers(2, 3)

    def test_divide_zero(self):
        # Use assertIsNone to check if value is None
        self.assertIsNone(divide_numbers(0, 0))

if __name__ == '__main__':
    unittest.main()
```
### Explanation

* We define a `divide_numbers` function that raises a `ValueError` when dividing by zero.
* In the `test_divide_positive_numbers` and `test_divide_zero` methods, we use `assertRaises` to check if our function raises the expected exception when divided by zero.
