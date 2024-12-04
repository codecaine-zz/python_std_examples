# unittest.mock — getting started

Here's an example of how you can use `unittest.mock` to mock objects, functions, and modules:

**Mocking Objects**

```python
import unittest
from unittest import mock

# Create a mock object
def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):

    # Mock the function we want to test
    @mock.patch('my_module.add')
    def test_add(self, mock_add):
        # Set up the mock to return a specific value when called
        mock_add.return_value = 10
        
        # Call the function being tested with some arguments
        result = add(2, 3)
        
        # Assert that the returned value is correct
        self.assertEqual(result, 5)

    # Test case where we don't call the function (should raise an error)
    @mock.patch('my_module.add')
    def test_add_not_called(self, mock_add):
        with self.assertRaises(RecursionError):
            add(2, 3)
```

**Mocking Functions**

```python
import unittest
from unittest import mock

class TestPrintFunction(unittest.TestCase):

    # Mock the function we want to test
    @mock.patch('builtins.print')
    def test_print(self, mock_print):
        # Set up the mock to print a specific message when called
        mock_print.return_value = None
        
        # Call the function being tested with some arguments
        print("Hello, world!")
        
        # Assert that the printed message is correct
        self.assertEqual(mock_print.call_args, ('Hello, world!',))

    # Test case where we don't call the function (should raise an error)
    @mock.patch('builtins.print')
    def test_print_not_called(self, mock_print):
        with self.assertRaises(RecursionError):
            print("Hello, world!")
```

**Mocking Modules**

```python
import unittest
from unittest import mock

class TestRandomModule(unittest.TestCase):

    # Mock the module we want to test
    @mock.patch('random')
    def test_random(self, mock_random):
        # Set up the mock to return a specific value when called
        mock_random.randint.return_value = 42
        
        # Call the function being tested with some arguments
        import random
        result = random.randint(1, 100)
        
        # Assert that the returned value is correct
        self.assertEqual(result, 42)

    # Test case where we don't call the function (should raise an error)
    @mock.patch('random')
    def test_random_not_called(self, mock_random):
        with self.assertRaises(RecursionError):
            import random
```

**Mocking Exceptions**

```python
import unittest
from unittest import mock

class TestRaiseException(unittest.TestCase):

    # Mock the exception we want to raise
    @mock.patch('ValueError')
    def test_raise_exception(self, mock_value_error):
        # Set up the mock to raise an exception when called
        mock_value_error.side_effect = ValueError("Something went wrong!")
        
        # Call the function being tested with some arguments
        with self.assertRaises(ValueError):
            raise ValueError("Something went wrong!")

    # Test case where we don't call the function (should not raise an error)
    @mock.patch('ValueError')
    def test_raise_exception_not_called(self, mock_value_error):
        with self.assertRaises(RecursionError):
            raise ValueError
```

**Mocking Context Managers**

```python
import unittest
from unittest import mock

class TestContextManager(unittest.TestCase):

    # Mock the context manager we want to test
    @mock.patch('contextlib.contextmanager')
    def test_context_manager(self, mock_contextmanager):
        # Set up the mock to yield a specific value when called
        mock_contextmanager.return_value.__enter__.return_value = "Hello"
        
        # Call the function being tested with some arguments
        with self.assertRaises(RecursionError):
            yield from "Hello"

    # Test case where we don't call the function (should not raise an error)
    @mock.patch('contextlib.contextmanager')
    def test_context_manager_not_called(self, mock_contextmanager):
        with self.assertRaises(RecursionError):
            import contextlib
```

**Mocking Decorators**

```python
import unittest
from unittest import mock

class TestDecorator(unittest.TestCase):

    # Mock the decorator we want to test
    @mock.patch('functools.wraps')
    def test_decorator(self, mock_functor_wraps):
        # Set up the mock to return a specific value when called
        mock_functor_wraps.return_value = "Hello"
        
        # Call the function being tested with some arguments
        from functools import wraps
        @wraps("Hello")
        def hello(name):
            return f"Hello, {name}!"
        result = hello("world")
        
        # Assert that the returned value is correct
        self.assertEqual(result, "Hello, world!")

    # Test case where we don't call the function (should not raise an error)
    @mock.patch('functools.wraps')
    def test_decorator_not_called(self, mock_functor_wraps):
        with self.assertRaises(RecursionError):
            from functools import wraps
```
