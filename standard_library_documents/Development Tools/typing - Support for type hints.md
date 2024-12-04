# typing — Support for type hints

**typing Module**
================

The `typing` module provides support for type hints, which can improve the readability and maintainability of Python code.

### Importing the typing Module
```python
import typing as t
```
### Type Hints

Type hints are used to indicate the expected types of variables, function parameters, and return values. Here's an example:
```python
from typing import List

def greet(name: str) -> None:
    print(f"Hello, {name}!")
```
In this example, `str` is a type hint indicating that the `name` parameter should be a string.

### Type Hints for Lists and Tuples

You can use the `List` and `Tuple` types to indicate that a variable or function parameter should be a list or tuple:
```python
from typing import List, Tuple

def process_data(data: List[int]) -> None:
    print(f"Processing data: {data}")

def extract_key(data: Tuple[str, int]) -> str:
    return data[0]
```
### Type Hints for Dictionaries

You can use the `Dict` type to indicate that a variable or function parameter should be a dictionary:
```python
from typing import Dict

def process_config(config: Dict[str, bool]) -> None:
    print(f"Processing config: {config}")
```
### Type Hints for Union Types

Union types allow you to specify multiple possible types for a variable or function parameter. Here's an example using the `Union` type:
```python
from typing import Union

def process_data(data: Union[int, str]) -> None:
    if isinstance(data, int):
        print(f"Processing integer data: {data}")
    elif isinstance(data, str):
        print(f"Processing string data: {data}")
```
### Type Hints for Optional Types

Optional types allow you to specify that a variable or function parameter may be `None`. Here's an example using the `Optional` type:
```python
from typing import Optional

def process_data(data: Optional[int]) -> None:
    if data is not None:
        print(f"Processing integer data: {data}")
```
### Type Hints for Named Tuples

Named tuples are a convenient way to represent structured data in Python. Here's an example using the `TypedDict` type:
```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

def process_person(person: Person) -> None:
    print(f"Processing person: {person}")
```
### Type Hints for Generic Types

Generic types allow you to specify the types of template parameters. Here's an example using the `List` and `TypeVar` type:
```python
from typing import List, TypeVar

T = TypeVar("T")

def process_data(data: List[T]) -> None:
    print(f"Processing data: {data}")
```
### Using the `Literal` Type

The `Literal` type allows you to specify a fixed value. Here's an example:
```python
from typing import Literal

def greet(greeting: Literal["hello", "goodbye"]) -> None:
    print(greeting)
```
This code will only accept `"hello"` or `"goodbye"` as the value for the `greeting` parameter.

### Using the `Union` Type with a Single Value

You can also use the `Union` type with a single value to make it more readable. Here's an example:
```python
from typing import Union

def process_data(data: Union[str, int]) -> None:
    print(f"Processing data: {data}")
```
This code is equivalent to using the `str | int` syntax in Python 3.10 and later.

### Using the ` Any` Type

The `Any` type allows you to specify that a variable or function parameter can be any type. Here's an example:
```python
from typing import Any

def process_data(data: Any) -> None:
    print(f"Processing data: {data}")
```
This code will accept any type of value.

### Using the `NoReturn` Type

The `NoReturn` type indicates that a function does not return any value. Here's an example:
```python
from typing import NoReturn

def raise_error() -> NoReturn:
    raise Exception("Something went wrong")
```
This code is useful when you want to indicate that a function will raise an exception and never returns.

### Using the ` Callable` Type

The `Callable` type allows you to specify that a variable or function parameter should be a callable object. Here's an example:
```python
from typing import Callable

def process_data(data: Callable[[int], None]) -> None:
    data(42)
```
This code will accept any callable object that takes an `int` argument and returns `None`.

### Using the ` overload` Decorator

The `overload` decorator allows you to specify multiple types for a function parameter. Here's an example:
```python
from typing import overload

@overload
def greet(name: str) -> None:
    ...

@overload
def greet(names: tuple[str, ...]) -> None:
    ...
```
This code is useful when you want to define multiple versions of the same function with different parameter types.

### Using the ` ParamSpec` Type

The `ParamSpec` type allows you to specify a set of parameters for a function or method. Here's an example:
```python
from typing import ParamSpec

P = ParamSpec("params")

def greet(name: P) -> None:
    print(f"Hello, {name}!")
```
This code is useful when you want to define a function or method with a variable number of parameters.

### Using the ` Generic` Type

The `Generic` type allows you to specify generic types for a class or function. Here's an example:
```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get_value(self) -> T:
        return self.value
```
This code is useful when you want to define a class that works with any type of data.

### Using the ` ClassVar` Type

The `ClassVar` type allows you to specify a variable that should be stored as an attribute of a class. Here's an example:
```python
from typing import ClassVar

class Person:
    _age: ClassVar[int] = 0

    def __init__(self, age: int) -> None:
        self._age = age

    @property
    def age(self) -> int:
        return self._age
```
This code is useful when you want to define a class that has a variable that should be shared across all instances of the class.
