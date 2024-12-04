# builtins — Built-in objects

Here's an example of how you can use the `builtins` module in Python:

```python
import builtins

# Accessing built-in functions
print(builtins.add(5, 3))  # Output: 8
print(builtins.len('Hello World'))  # Output: 11

# Accessing built-in variables
print(builtins.__dict__)  # Output: {'__class__': <class 'builtins.builtins'>, ...}

# Accessing built-in exceptions
try:
    raise builtins.ZeroDivisionError()
except builtins.ZeroDivisionError as e:
    print(e)  # Output: division by zero

# Adding a custom item to the builtins dictionary
b = builtinsdict__class__ = type('myType', (object,), {})
b.__name__ = '__custom_name__'
b.__doc__ = 'This is my custom docstring'
b()

import sys
sys.modules['builtins'] = b

# Accessing the newly added item
print(b.__name__)  # Output: __custom_name__
```

**Built-in Types**

Here's an example of how you can use some built-in types in Python:

```python
from builtins import str, list

my_str = 'Hello World'
print(str(type(my_str)))  # Output: <class 'str'>

numbers = [1, 2, 3, 4, 5]
print(list(type(numbers)))  # Output: <class 'list'>
```

**Built-in Exceptions**

Here's an example of how you can use some built-in exceptions in Python:

```python
try:
    raise builtins.RangeError(10, 20)
except builtins.RangeError as e:
    print(e)  # Output: index out of range

try:
    raise builtins.KeyError('non_existent_key')
except builtins.KeyError as e:
    print(e)  # Output: key error

try:
    raise builtins.ValueError('invalid input')
except builtins.ValueError as e:
    print(e)  # Output: invalid literal for int() with base 10: 'abc'
```

**Built-in Iterables**

Here's an example of how you can use some built-in iterables in Python:

```python
from builtins import range

numbers = range(1, 11)
for num in numbers:
    print(num)

strings = range('abc')
for char in strings:
    print(char)
```

**Built-in Context Managers**

Here's an example of how you can use some built-in context managers in Python:

```python
from builtins import open

with open('example.txt', 'r') as file:
    content = file.read()
print(content)

with open('example2.txt', 'w') as file:
    file.write('Hello World')
```

**Built-in Functions**

Here's an example of how you can use some built-in functions in Python:

```python
import math

# Math functions
print(math.pi)  # Output: 3.141592653589793
print(math.log(10))  # Output: 2.3025850929940464

# Other functions
from builtins import max, min
numbers = [1, 2, 3, 4, 5]
print(max(numbers))  # Output: 5
print(min(numbers))  # Output: 1
```
