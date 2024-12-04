# enum — Support for enumerations

**Enumerations in Python**
==========================

The `enum` module in Python provides support for enumerations, also known as constants or named values.

### Enum Definition

```python
from enum import Enum

# Define an enumeration class
class Color(Enum):
    """
    An enumeration of colors.
    
    Attributes:
        RED (str): The string representation of the color red.
        GREEN (str): The string representation of the color green.
        BLUE (str): The string representation of the color blue.
    """
    RED = 1
    GREEN = 2
    BLUE = 3

# Define another enumeration class
class Status(Enum):
    """
    An enumeration of HTTP status codes.
    
    Attributes:
        OK (int): The integer value for a successful response.
        NOT_FOUND (int): The integer value for a resource not found.
        INTERNAL_SERVER_ERROR (int): The integer value for an internal server error.
    """
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

# Enum member access
print(Color.RED)  # Output: Color.RED
print(Color.RED.name)  # Output: RED
print(Status.OK.value)  # Output: 200

# Iterate over enum members
for color in Color:
    print(color)  # Output: Color.RED, Color.GREEN, Color.BLUE

# Enum comparison
if Status.OK == Status.NOT_FOUND:
    print("OK is not equal to NOT_FOUND")  # Output: OK is not equal to NOT_FOUND
```

### Enum Members

Enum members can be defined as class-level variables or using the `enum member syntax`. The following examples demonstrate both approaches:

```python
# Class-level definition
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Enum member syntax
Color.RED = 4
```

### Enum Values

Enum members can be accessed using the `name` attribute or the value itself.

```python
# Access enum member using name
print(Color.RED.name)  # Output: RED

# Access enum member using value
print(Color.RED.value)  # Output: 1
```

### Enum Iteration

Enumerations can be iterated over using a `for` loop or the `.items()` method.

```python
# Iterate over enum members using for loop
for color in Color:
    print(color)

# Iterate over enum members using items() method
for name, value in Color.items():
    print(f"{name}: {value}")
```

### Enum Inheritance

Enums can inherit from other enums using the `Enum` class as a base.

```python
from enum import Enum

class Shape(Enum):
    CIRCLE = 1
    SQUARE = 2

class Triangle(Shape):
    TRIANGLE = 3
```

Note that in Python 3.4 and later, you can use the `.auto()` method to automatically create an enumeration class.

```python
from enum import Enum, auto

Color = Enum("Color", ["RED", "GREEN", "BLUE"])
Status = Enum("Status", [200, 404, 500])
```
