# unittest.mock - getting started

The `unittest.mock` module is a powerful tool used for creating mock objects in Python, which are essential for testing purposes. These mocks allow you to simulate the behavior of real objects without executing them, making your tests more isolated and predictable.

Below are comprehensive code examples demonstrating how to use `unittest.mock` for various common use cases:

### Example 1: Creating a Simple Mock Object

```python
import unittest
from unittest.mock import MagicMock

class TestMyModule(unittest.TestCase):
    def test_simple_mock(self):
        # Create a mock object
        my_mock = MagicMock()

        # Use the mock object as if it were a real object
        my_mock.some_method.return_value = 'mocked result'

        # Assert that the method was called and return the expected value
        self.assertEqual(my_mock.some_method(), 'mocked result')
        self.assertTrue(my_mock.some_method.called)

    def test_arguments(self):
        # Create a mock object
        my_mock = MagicMock()

        # Specify that the method should be called with specific arguments
        my_mock.some_method.return_value = 'mocked result'
        my_mock.some_method.assert_called_once_with('arg1', 'arg2')

        # Assert that the method was called multiple times with different arguments
        my_mock.some_method.side_effect = ['result1', 'result2']
        self.assertEqual(my_mock.some_method('a', 'b'), 'result1')
        self.assertEqual(my_mock.some_method('c', 'd'), 'result2')
        self.assertTrue(my_mock.some_method.called)

    def test_calls(self):
        # Create a mock object
        my_mock = MagicMock()

        # Record all calls to the method
        my_mock.some_method('arg1', 'arg2')

        # Assert that the method was called with specific arguments
        self.assertEqual(len(my_mock.some_method.call_args_list), 1)
        self.assertEqual(my_mock.some_method.call_args_list[0], (('arg1', 'arg2'), {}))

    def test_call_counter(self):
        # Create a mock object
        my_mock = MagicMock()

        # Record all calls to the method
        my_mock.some_method()
        my_mock.some_method()
        my_mock.some_method()

        # Assert that the method was called 3 times
        self.assertEqual(my_mock.some_method.call_count, 3)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
```

### Example 2: Mocking a Class Method

```python
import unittest
from unittest.mock import MagicMock

class MyClass:
    def some_method(self):
        return 'real result'

class TestMyClass(unittest.TestCase):
    def test_mock_class_method(self):
        # Create an instance of MyClass
        my_instance = MyClass()

        # Create a mock object for the class method
        my_mock = MagicMock(return_value='mocked result')

        # Replace the original class method with the mock
        MyClass.some_method = my_mock

        # Call the modified class method
        self.assertEqual(my_instance.some_method(), 'mocked result')
        self.assertTrue(MyClass.some_method.called)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
```

### Example 3: Mocking a Static Method

```python
import unittest
from unittest.mock import MagicMock

class MyClass:
    @staticmethod
    def some_static_method(x):
        return x * 2

class TestMyClass(unittest.TestCase):
    def test_mock_static_method(self):
        # Create a mock object for the static method
        my_mock = MagicMock(return_value='mocked result')

        # Replace the original static method with the mock
        MyClass.some_static_method = my_mock

        # Call the modified static method
        self.assertEqual(MyClass.some_static_method(3), 'mocked result')
        self.assertTrue(my_mock.called)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
```

### Example 4: Mocking a Module Function

```python
import unittest
from unittest.mock import patch

# Assuming we have a function `some_module.some_function` defined in `some_module.py`
with patch('some_module.some_function') as mock_some_function:
    # Modify the behavior of the mocked function
    mock_some_function.return_value = 'mocked result'

    # Import and use the module that contains the function
    from some_module import some_function

    # Call the mocked function
    result = some_function()

    # Assert the expected result
    self.assertEqual(result, 'mocked result')
```

### Example 5: Mocking an External Library Function

```python
import unittest
from unittest.mock import patch
import requests

# Replace the actual `requests.get` call with a mock
with patch('requests.get') as mock_get:
    # Modify the behavior of the mocked function to return a specific response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'data': 'mocked data'}

    # Make an HTTP request using the patched `requests`
    response = requests.get('https://example.com/api/data')

    # Assert that the mocked function was called with the expected URL
    self.assertEqual(mock_get.call_args.args[0], 'https://example.com/api/data')
    self.assertTrue(response.json() == {'data': 'mocked data'})

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
```

### Example 6: Using `patch` Decorator

```python
import unittest
from unittest.mock import patch
import requests

@patch('requests.get')
def test_patch_decorator(mock_get):
    # Modify the behavior of the mocked function to return a specific response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'data': 'mocked data'}

    # Make an HTTP request using the patched `requests`
    response = requests.get('https://example.com/api/data')

    # Assert that the mocked function was called with the expected URL
    self.assertEqual(mock_get.call_args.args[0], 'https://example.com/api/data')
    self.assertTrue(response.json() == {'data': 'mocked data'})

class TestRequestsPatching(unittest.TestCase):
    def test_example(self):
        test_patch_decorator()

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
```

These examples cover basic mocking techniques using `unittest.mock`, including:

1. Creating simple mock objects.
2. Mocking class and static methods.
3. Mocking module functions.
4. Mocking external library functions.
5. Using the `patch` decorator.

Each example includes detailed comments to explain the purpose of each step and how it relates to the functionality being tested. These examples are suitable for inclusion in official documentation, providing clear guidance on how to use `unittest.mock` effectively for testing purposes.
