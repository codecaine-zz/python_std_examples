# typing - Support for type hints

The `typing` module is a powerful addition to Python that provides a way to add static type checking to your code using type hints, which are annotations that describe the expected types of variables and function arguments. Here are comprehensive and well-documented examples for various functionalities within the `typing` module:

### 1. Type Annotations

Type annotations can be added to functions, classes, methods, and variables to help with static type checking.

```python
from typing import *
import datetime

# Function with type hints
def add(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b

# Class with type annotations
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Returns a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Method with type hints
def get_current_date() -> datetime.date:
    """Returns the current date."""
    return datetime.date.today()
```

### 2. Type Aliases

Type aliases allow you to give a new name to an existing type, making your code more readable and maintainable.

```python
from typing import *
import collections

# Type alias for a list of strings
StringList = List[str]

# Using the type alias in a function
def filter_strings(strings: StringList) -> StringList:
    """Returns a list of strings that start with 'a'."""
    return [s for s in strings if s.startswith('a')]

# Example usage of the type alias
names = ["alice", "bob", "carol"]
filtered_names = filter_strings(names)
print(filtered_names)  # Output: ['alice', 'carol']
```

### 3. Optional Values

Use `Optional` to indicate that a variable can be either a specified type or `None`.

```python
from typing import *

# Function with optional parameters
def greet(name: str, age: Optional[int] = None) -> str:
    """Returns a greeting message, optionally including the age."""
    if age is not None:
        return f"Hello, my name is {name} and I am {age} years old."
    else:
        return f"Hello, my name is {name}."
```

### 4. Generic Types

Generics allow you to create reusable functions or classes that work with different types.

```python
from typing import *
import collections

# Generic function for list operations
def process_list(lst: List[T]) -> List[T]:
    """Applies a processing operation to each element in the list."""
    return [x * 2 for x in lst]

# Example usage of the generic function with integers and strings
numbers = [1, 2, 3]
strings = ["a", "b", "c"]

processed_numbers = process_list(numbers)
processed_strings = process_list(strings)

print(processed_numbers)   # Output: [2, 4, 6]
print(processed_strings)  # Output: ['aa', 'bb', 'cc']
```

### 5. Callable Types

Use `Callable` to indicate that a variable is expected to be a callable object.

```python
from typing import *
import operator

# Function with type hint for a callable
def apply_operation(op: Callable[[int, int], int], a: int, b: int) -> int:
    """Applies the provided operation to two integers."""
    return op(a, b)

# Example usage of the callable function
addition = lambda x, y: x + y
multiplication = lambda x, y: x * y

result_addition = apply_operation(addition, 3, 4)
result_multiplication = apply_operation(multiplication, 3, 4)

print(result_addition)   # Output: 7
print(result_multiplication) # Output: 12
```

### 6. Container Types

Types like `Sequence`, `Iterable`, and `Mapping` provide type hints for sequences of items.

```python
from typing import *
import collections

# Function with type hint for a sequence of numbers
def calculate_sum(seq: Sequence[int]) -> int:
    """Calculates the sum of elements in the sequence."""
    return sum(seq)

# Example usage of the sequence function
numbers = [1, 2, 3, 4, 5]
result = calculate_sum(numbers)
print(result)  # Output: 15

# Function with type hint for an iterable of strings
def filter_strings_iter(iterable: Iterable[str]) -> Iterator[str]:
    """Filters out empty strings from the iterable."""
    return (s for s in iterable if s)

# Example usage of the iterable function
strings = ["apple", "", "banana", ""]
filtered_strings = list(filter_strings_iter(strings))
print(filtered_strings)  # Output: ['apple', 'banana']
```

### 7. Union Types

Use `Union` to indicate that a variable can be one of several types.

```python
from typing import *

# Function with type hint for a union of string and int
def process_value(value: Union[str, int]) -> str:
    """Converts the value to a string."""
    if isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)

# Example usage of the union function
result1 = process_value("hello")
result2 = process_value(42)
print(result1)  # Output: 'hello'
print(result2)  # Output: '42'
```

### 8. Type Literals

Use `Literal` to denote a specific set of values.

```python
from typing import *

# Function with type hint for a literal value
def greet(name: Literal["Alice", "Bob"]) -> str:
    """Returns a greeting message for the specified name."""
    return f"Hello, {name}!"

# Example usage of the literal function
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

These examples cover a wide range of functionalities provided by the `typing` module, including type annotations, type aliases, optional values, generic types, callable types, container types, union types, and type literals. Each example is accompanied by comments to explain the purpose and usage of each part of the code.
