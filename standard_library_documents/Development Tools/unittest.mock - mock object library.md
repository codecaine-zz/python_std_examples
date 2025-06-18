# unittest.mock - mock object library
## Table of Contents

1. [Example 1: Basic Usage](#example-1-basic-usage)
2. [Example 2: Mocking Functions](#example-2-mocking-functions)
3. [Example 3: Mocking Classes](#example-3-mocking-classes)
4. [Example 4: Mocking with Arguments](#example-4-mocking-with-arguments)
5. [Example 5: Mocking with Side Effects](#example-5-mocking-with-side-effects)
6. [Example 6: Mocking with Return Values](#example-6-mocking-with-return-values)
7. [Example 7: Mocking with Return Value Count](#example-7-mocking-with-return-value-count)
8. [Example 8: Mocking with Side Effect and Return Value Count](#example-8-mocking-with-side-effect-and-return-value-count)



The `unittest.mock` module is a powerful tool for creating test doubles in Python, allowing you to isolate parts of your code that interact with external systems or dependencies. This module provides several useful functions and classes to help you simulate various scenarios in your tests.

Below are comprehensive examples for each functionality provided by the `unittest.mock` module:

### Example 1: Basic Usage

```python
import unittest
from unittest.mock import Mock, patch

class TestMockExample(unittest.TestCase):
    def test_basic_usage(self):
        # Create a mock object
        mock_object = Mock()

        # Call the mock object
        mock_object.method_name()

        # Check if the method was called
        self.assertTrue(mock_object.method_name.called)

        # Get the arguments passed to the method
        args, kwargs = mock_object.method_name.call_args

        # Assert that no additional calls were made
        self.assertFalse(mock_object.method_name.called_more_than_once())

if __name__ == '__main__':
    unittest.main()
```

### Example 2: Mocking Functions

```python
import unittest
from unittest.mock import patch, MagicMock

class TestMockFunction(unittest.TestCase):
    def test_mock_function(self):
        # Use a partial to mock a function from another module
        with patch('module_name.function_name') as mock_func:
            mock_func.return_value = "Mocked Output"
            result = module_name.function_name()
            self.assertEqual(result, "Mocked Output")
            mock_func.assert_called_once()

    def test_mocking_builtin_function(self):
        # Mock the built-in `open` function
        with patch('builtins.open', return_value=MagicMock()) as mock_open:
            mock_file_obj = mock_open.return_value
            mock_file_obj.read.return_value = "Mocked File Content"
            content = open("example.txt").read()
            self.assertEqual(content, "Mocked File Content")
            mock_open.assert_called_once_with('example.txt')

if __name__ == '__main__':
    unittest.main()
```

### Example 3: Mocking Classes

```python
import unittest
from unittest.mock import patch, MagicMock

class TestMockClass(unittest.TestCase):
    def test_mock_class(self):
        # Create a mock class instance
        with patch('module_name.MyClass') as mock_cls:
            mock_obj = mock_cls.return_value
            mock_obj.method_name.return_value = "Mocked Method Output"
            result = MyClass().method_name()
            self.assertEqual(result, "Mocked Method Output")
            mock_obj.method_name.assert_called_once()

    def test_mock_subclass(self):
        # Mock a subclass of a class
        with patch('module_name.BaseClass') as mock_base:
            mock_base.return_value = MagicMock(spec=BaseClass)
            mock_base.instance_method.return_value = "Mocked Instance Method Output"
            instance = BaseClass()
            result = instance.instance_method()
            self.assertEqual(result, "Mocked Instance Method Output")
            mock_base.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```

### Example 4: Mocking with Arguments

```python
import unittest
from unittest.mock import patch

class TestMockWithArguments(unittest.TestCase):
    def test_mock_with_arguments(self):
        # Create a mock object and specify the expected arguments
        mock_object = Mock()

        # Call the mock object with specific arguments
        mock_object.method_name('arg1', arg2='value2')

        # Check if the method was called with the correct arguments
        args, kwargs = mock_object.method_name.call_args

        self.assertEqual(args[0], 'arg1')
        self.assertEqual(kwargs['arg2'], 'value2')

    def test_mock_with_mixed_arguments(self):
        # Create a mock object and specify expected keyword arguments
        mock_object = Mock()

        # Call the mock object with both positional and keyword arguments
        mock_object.method_name('arg1', arg2='value2')

        # Check if the method was called with the correct arguments
        args, kwargs = mock_object.method_name.call_args

        self.assertEqual(args[0], 'arg1')
        self.assertEqual(kwargs['arg2'], 'value2')

if __name__ == '__main__':
    unittest.main()
```

### Example 5: Mocking with Side Effects

```python
import unittest
from unittest.mock import patch, MagicMock

class TestMockSideEffects(unittest.TestCase):
    def test_mock_side_effects(self):
        # Create a mock object and define a side effect function
        mock_object = Mock(side_effect=lambda x: x * 2)

        # Call the mock object with different inputs
        result1 = mock_object(3)
        result2 = mock_object('a')

        # Check if the results match the expected outputs
        self.assertEqual(result1, 6)
        self.assertEqual(result2, 'aa')

    def test_mock_with_raising_side_effects(self):
        # Create a mock object and define a side effect that raises an exception
        mock_object = Mock(side_effect=Exception("Mocked Exception"))

        # Call the mock object to see if it raises an exception
        with self.assertRaises(Exception) as context:
            mock_object()

        # Check if the exception matches the expected message
        self.assertEqual(str(context.exception), "Mocked Exception")

if __name__ == '__main__':
    unittest.main()
```

### Example 6: Mocking with Return Values

```python
import unittest
from unittest.mock import patch, MagicMock

class TestMockReturnValues(unittest.TestCase):
    def test_mock_return_values(self):
        # Create a mock object and define the return value for different calls
        mock_object = Mock(return_value="Initial Return")

        # First call to get the initial return value
        result1 = mock_object()
        self.assertEqual(result1, "Initial Return")

        # Second call to use the default side effect (returns 0)
        result2 = mock_object()
        self.assertEqual(result2, 0)

    def test_mock_with_mixed_return_values(self):
        # Create a mock object and define different return values for specific inputs
        mock_object = Mock(side_effect=lambda x: {
            1: "One",
            2: "Two"
        }.get(x, 3))

        # Call the mock object with different inputs
        result1 = mock_object(1)
        result2 = mock_object(2)
        result3 = mock_object(3)

        # Check if the results match the expected outputs
        self.assertEqual(result1, "One")
        self.assertEqual(result2, "Two")
        self.assertEqual(result3, 3)

if __name__ == '__main__':
    unittest.main()
```

### Example 7: Mocking with Return Value Count

```python
import unittest
from unittest.mock import patch, MagicMock

class TestMockReturnValueCount(unittest.TestCase):
    def test_mock_return_value_count(self):
        # Create a mock object and set the return value count
        mock_object = Mock(return_value="Initial Return", side_effect=1)

        # Call the mock object multiple times to check the return values
        result1 = mock_object()
        result2 = mock_object()

        # Check if the first call returns the initial return value, and subsequent calls raise an exception
        self.assertEqual(result1, "Initial Return")
        with self.assertRaises(ValueError):
            mock_object()

    def test_mock_with_mixed_return_value_count(self):
        # Create a mock object and set different return values for specific inputs and a side effect count
        mock_object = Mock(return_value="Initial Return", side_effect=[lambda x: x * 2, lambda x: x + 1])

        # Call the mock object with different inputs to check the return values
        result1 = mock_object(1)
        result2 = mock_object(2)

        # Check if the results match the expected outputs
        self.assertEqual(result1, 2)  # Double of input 1
        self.assertEqual(result2, 3)  # Input 2 plus 1

if __name__ == '__main__':
    unittest.main()
```

### Example 8: Mocking with Side Effect and Return Value Count

```python
import unittest
from unittest.mock import patch, MagicMock

class TestMockSideEffectAndReturnValueCount(unittest.TestCase):
    def test_mock_side_effect_and_return_value_count(self):
        # Create a mock object and set the side effect and return value count
        mock_object = Mock(side_effect=[lambda x: x * 2, lambda x: x + 1], return_value="Initial Return", side_effect_count=2)

        # Call the mock object multiple times to check the return values and exceptions
        result1 = mock_object(1)
        result2 = mock_object(2)
        result3 = mock_object(3)

        # Check if the results match the expected outputs and subsequent calls raise an exception
        self.assertEqual(result1, 2)  # Double of input 1
        self.assertEqual(result2, 3)  # Input 2 plus 1
        with self.assertRaises(ValueError):
            mock_object()

if __name__ == '__main__':
    unittest.main()
```

These examples demonstrate various ways to use the `unittest.mock` module to create and configure mock objects for testing in Python. Each example includes comments explaining key points, such as setting return values, mocking function calls, handling side effects, and checking argument counts.
