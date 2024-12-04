# __future__ - Future statement definitions

The `__future__` module in Python provides a way to specify features that are still experimental or may change in future versions of the language. These features can be enabled by using "future" statements at the top of your script or module. This module is part of Python's standard library, so it doesn't need to be installed separately.

Here are some examples of how you might use `__future__` statements:

### 1. Using Generators with Expressions
In Python 3, generators can be used in expressions directly without parentheses. To enable this behavior in earlier versions of Python, you can use the `from __future__ import generator_expr`.

```python
# Example using generator expressions before Python 3
even_numbers = (x for x in range(10) if x % 2 == 0)

# Using generator expression with future statement in Python 2
from __future__ import generator_expr

even_numbers = (x for x in range(10) if x % 2 == 0)
```

### 2. Unpacking Star Expressions
In Python 3, you can use the `*` operator directly to unpack iterables into positional arguments without parentheses. To enable this behavior in earlier versions of Python, you can use the `from __future__ import star_args`.

```python
# Example using star expressions before Python 3
def print_numbers(*args):
    for num in args:
        print(num)

numbers = [1, 2, 3]
print_numbers(numbers)  # Output: 1 2 3

# Using star expressions with future statement in Python 2
from __future__ import star_args

def print_numbers(*args):
    for num in args:
        print(num)

numbers = [1, 2, 3]
print_numbers(*numbers)  # Output: 1 2 3
```

### 3. Division Behavior
In Python 3, the division of two integers results in a float. However, in earlier versions, it performed integer division and returned an integer result. To enable the behavior of returning a float, you can use the `from __future__ import division`.

```python
# Example of integer division before Python 3
result = 5 / 2  # Output: 2

# Using division with future statement in Python 2
from __future__ import division

result = 5 / 2  # Output: 2.5
```

### 4. Print Function Syntax
In Python 3, the `print` function is a built-in function and does not require parentheses around its arguments. To enable this behavior in earlier versions of Python, you can use the `from __future__ import print_function`.

```python
# Example using print function without parentheses before Python 3
print("Hello", "World")

# Using print function with future statement in Python 2
from __future__ import print_function

print("Hello", "World")
```

### 5. Float Division with `//`
In Python 3, the floor division of two integers returns an integer result. To enable this behavior in earlier versions of Python, you can use the `from __future__ import floor_division`.

```python
# Example of floor division before Python 3
result = 5 // 2  # Output: 2

# Using floor division with future statement in Python 2
from __future__ import floor_division

result = 5 // 2  # Output: 2
```

These examples demonstrate how to use `__future__` statements to leverage new features of Python without breaking compatibility with older versions. It's important to note that not all features are supported by the `__future__` module, and some may require additional imports or configuration depending on your specific use case and environment.
