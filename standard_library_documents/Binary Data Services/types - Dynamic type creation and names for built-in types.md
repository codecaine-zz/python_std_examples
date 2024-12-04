# types — Dynamic type creation and names for built-in types

**Types Module**
================

The `types` module provides several classes for working with dynamic typing, including the `TypeVar`, `Generic`, `Mapping`, `Sequence`, and `Union` types.

### 1. TypeVar

A `TypeVar` represents a type variable, which can be instantiated with any type.

```python
from types import TypeVar

# Define a type variable
T = TypeVar('T')

# Create a class that uses the type variable
class MyClass:
    def __init__(self, value: T):
        self.value = value

# Instantiate the class with different types
obj1 = MyClass(1)  # obj1 is of type MyClass[T] where T = int
obj2 = MyClass("hello")  # obj2 is of type MyClass[str]
```

### 2. Generic

A `Generic` represents a generic type that can be parameterized with any type.

```python
from types import Generic

# Define a generic class
class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

# Instantiate the class with different types
obj1 = Container(1)  # obj1 is of type Container[int]
obj2 = Container("hello")  # obj2 is of type Container[str]
```

### 3. Mapping

A `Mapping` represents a mapping, which can be used to store key-value pairs.

```python
from types import MappingProxyType

# Create an empty dictionary
d: dict = {}

# Add key-value pairs
d["key1"] = "value1"
d["key2"] = 2

# Use the MappingProxyType to make the dictionary immutable
d_proxy = MappingProxyType(d)

try:
    d_proxy["key3"] = "new_value"
except AttributeError as e:
    print(e)  # Output: 'mapping' object has no attribute '_dict'
```

### 4. Sequence

A `Sequence` represents a sequence, which can be used to store elements in a particular order.

```python
from types import SequenceType

# Create an empty list
lst: list = []

# Add elements
lst.append(1)
lst.append("hello")
lst.append(2)

try:
    lst.pop()
except AttributeError as e:
    print(e)  # Output: 'list' object has no attribute '_pop'
```

### 5. Union

A `Union` represents a union of types, which can be used to indicate that a value can be one of multiple types.

```python
from types import UnionType

# Define a union type
T = UnionType[int, str]

def process_value(value: T) -> None:
    if isinstance(value, int):
        print("Int value:", value)
    elif isinstance(value, str):
        print("Str value:", value)

process_value(1)  # Output: Int value: 1
process_value("hello")  # Output: Str value: hello
```

### 6. Type Alias

A `TypeAlias` represents a type alias, which can be used to give a name to an existing type.

```python
from types import TypeAlias

# Define a type alias for int
Int = TypeAlias('int')

def process_value(value: Int) -> None:
    print("Int value:", value)

process_value(1)  # Output: Int value: 1
```

### 7. Newtype

A `Newtype` represents a newtype, which can be used to create a new type from an existing type.

```python
from types import NewType

# Define a newtype for Date
Date = NewType('Date', tuple)

def process_date(date: Date) -> None:
    print("Date value:", date)

process_date((2022, 1, 1))  # Output: Date value: (2022, 1, 1)
```
