# functools - Higher-order functions and operations on callable objects

The `functools` module in Python provides a collection of higher-order functions that can be used to work with callable objects, such as functions, methods, and other functions. These functions are particularly useful for optimizing or managing common patterns of code execution.

Here are some comprehensive code examples demonstrating various functionalities provided by the `functools` module:

1. **`lru_cache`**: This decorator is used to cache the results of expensive function calls and reuse them when the same inputs occur again. It is especially useful in scenarios where a function calls itself recursively or repeatedly with the same arguments.

```python
from functools import lru_cache

@lru_cache(maxsize=128)  # Cache up to 128 results
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
print(factorial(5))  # Reuses cached result, no additional computation needed
```

2. **`partial`**: This function creates a new callable from an existing callable and some fixed arguments.

```python
from functools import partial

def multiply(x, y):
    return x * y

# Create a new function that multiplies by 5
multiply_by_5 = partial(multiply, 5)

# Example usage
print(multiply_by_5(4))  # Output: 20
```

3. **`reduce`**: This function applies a binary function cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single output.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Calculate the product of all numbers in the list
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
```

4. **`cmp_to_key`**: This function converts a `cmp` callable to a key function for use with sorting functions.

```python
from functools import cmp_to_key

def compare(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

# Create a key function using cmp_to_key
key_function = cmp_to_key(compare)

# Example usage with sorted
sorted_list = sorted([3, 1, 4, 1, 5, 9], key=key_function)
print(sorted_list)  # Output: [1, 1, 3, 4, 5, 9]
```

5. **`total_ordering`**: This class decorator can be used to automatically implement rich comparison operations (`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, and `__ge__`) based on the implementations of some of them.

```python
from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)

# Example usage
point1 = Point(1, 2)
point2 = Point(1, 3)
print(point1 == point2)  # Output: True
print(point1 < point2)   # Output: False
```

6. **`reduce` with `operator.add`**: Using the `reduce` function along with the `operator.add` function, you can sum all elements in an iterable.

```python
import operator

numbers = [1, 2, 3, 4, 5]

# Calculate the sum of all numbers in the list
total_sum = reduce(operator.add, numbers)
print(total_sum)  # Output: 15
```

7. **`reduce` with `operator.mul`**: Similarly, you can use `operator.mul` to multiply all elements in an iterable.

```python
import operator

numbers = [1, 2, 3, 4, 5]

# Calculate the product of all numbers in the list
total_product = reduce(operator.mul, numbers)
print(total_product)  # Output: 120
```

8. **`reduce` with `operator.add` and a custom lambda**: Using a lambda function can also be used to perform operations on iterable elements.

```python
import operator

numbers = [1, 2, 3, 4, 5]

# Calculate the sum of all numbers in the list using a lambda
total_sum_lambda = reduce(lambda x, y: x + y, numbers)
print(total_sum_lambda)  # Output: 15
```

9. **`reduce` with `operator.mul` and a custom lambda**: Similarly, you can use a lambda function to multiply all elements in an iterable.

```python
import operator

numbers = [1, 2, 3, 4, 5]

# Calculate the product of all numbers in the list using a lambda
total_product_lambda = reduce(lambda x, y: x * y, numbers)
print(total_product_lambda)  # Output: 120
```

These examples demonstrate various ways to use the `functools` module to enhance and optimize Python code. Each example includes comments that explain its purpose and functionality, making it easier for users to understand how these functions can be applied in different scenarios.
