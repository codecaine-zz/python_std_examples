# unittest - Unit testing framework
## Table of Contents

1. [Example 1: Basic Test Case](#example-1-basic-test-case)
2. [Example 2: Test Case with Setup and Teardown](#example-2-test-case-with-setup-and-teardown)
3. [Example 3: Test Case with Assertions](#example-3-test-case-with-assertions)
4. [Example 4: Test Case with Assertions for Exceptions](#example-4-test-case-with-assertions-for-exceptions)
5. [Example 5: Test Case with Parameterized Tests](#example-5-test-case-with-parameterized-tests)
6. [Example 6: Test Case with Test Suite](#example-6-test-case-with-test-suite)
7. [Example 7: Test Case with Test Loader](#example-7-test-case-with-test-loader)



The `unittest` module is a powerful tool for writing unit tests in Python. It provides a flexible framework that allows you to create test cases, define assertions, and run tests programmatically. Below are comprehensive examples covering various functionalities of the `unittest` module.

### Example 1: Basic Test Case

```python
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any resources or state that need to be initialized before each test
        self.value = 10

    def tearDown(self):
        # Clean up any resources or state after each test
        pass

    def test_addition(self):
        # Test the addition of two numbers
        result = self.value + 5
        self.assertEqual(result, 15, "The sum should be 15")

    def test_subtraction(self):
        # Test the subtraction of a number from another number
        result = self.value - 3
        self.assertEqual(result, 7, "The difference should be 7")

if __name__ == '__main__':
    unittest.main()
```

### Example 2: Test Case with Setup and Teardown

```python
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any resources or state that need to be initialized before each test
        self.value = 10

    def tearDown(self):
        # Clean up any resources or state after each test
        pass

    def test_addition(self):
        # Test the addition of two numbers
        result = self.value + 5
        self.assertEqual(result, 15, "The sum should be 15")

    def test_subtraction(self):
        # Test the subtraction of a number from another number
        result = self.value - 3
        self.assertEqual(result, 7, "The difference should be 7")

    @classmethod
    def setUpClass(cls):
        # Set up any resources or state that need to be initialized before all tests
        cls.shared_resource = [1, 2, 3]

    @classmethod
    def tearDownClass(cls):
        # Clean up any resources or state after all tests
        del cls.shared_resource

if __name__ == '__main__':
    unittest.main()
```

### Example 3: Test Case with Assertions

```python
import unittest

class MyTestCase(unittest.TestCase):
    def test_greater_than(self):
        # Test if a value is greater than another
        self.assertGreater(15, 10, "15 should be greater than 10")

    def test_less_than_or_equal_to(self):
        # Test if a value is less than or equal to another
        self.assertLessEqual(10, 10, "10 should be less than or equal to 10")

    def test_is_instance(self):
        # Test if an object is an instance of a class
        self.assertIsInstance("Hello", str, "The string 'Hello' should be an instance of str")

if __name__ == '__main__':
    unittest.main()
```

### Example 4: Test Case with Assertions for Exceptions

```python
import unittest

class MyTestCase(unittest.TestCase):
    def test_division_by_zero(self):
        # Test if a division by zero raises a ZeroDivisionError
        self.assertRaises(ZeroDivisionError, lambda: 10 / 0)

    def test_invalid_input(self):
        # Test if an invalid input raises a ValueError
        with self.assertRaises(ValueError):
            int("a")

if __name__ == '__main__':
    unittest.main()
```

### Example 5: Test Case with Parameterized Tests

```python
import unittest
from parameterized import parameterized

class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        (1, 2, 3),
        (4, 5, 9),
        (-1, -1, 0),
        (0, 0, 0)
    ])
    def test_addition_with_parameters(self, a, b, expected):
        # Test the addition of two numbers with parameterized inputs
        result = a + b
        self.assertEqual(result, expected, f"The sum should be {expected}")

if __name__ == '__main__':
    unittest.main()
```

### Example 6: Test Case with Test Suite

```python
import unittest

class TestCase1(unittest.TestCase):
    def test_addition(self):
        # Test the addition of two numbers in TestCase1
        self.assertEqual(5 + 5, 10)

class TestCase2(unittest.TestCase):
    def test_subtraction(self):
        # Test the subtraction of two numbers in TestCase2
        self.assertEqual(10 - 5, 5)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCase1('test_addition'))
    suite.addTest(TestCase2('test_subtraction'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

### Example 7: Test Case with Test Loader

```python
import unittest

def load_tests(loader, tests=None, pattern='test_*.py'):
    if tests is None:
        tests = loader.discover('.')
    return tests

if __name__ == '__main__':
    suite = unittest.TestLoader().discover()
    runner = unittest.TextTestRunner()
    runner.run(suite)
```

These examples cover a range of functionalities within the `unittest` module, from basic test cases to more advanced features like parameterized testing and test loading. Each example is designed to be clear, concise, and suitable for integration into Python documentation.
