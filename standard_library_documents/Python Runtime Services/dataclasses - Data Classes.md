# dataclasses - Data Classes
## Table of Contents

1. [Installation](#installation)
2. [Example 1: Basic Usage](#example-1-basic-usage)
3. [Example 2: Multiple Default Values](#example-2-multiple-default-values)
4. [Example 3: Immutable Attributes](#example-3-immutable-attributes)
5. [Example 4: Custom Initialization](#example-4-custom-initialization)
6. [Example 5: Auto-Generated Special Methods](#example-5-auto-generated-special-methods)
7. [Example 6: Optional Attributes](#example-6-optional-attributes)
8. [Example 7: Recursive Data Classes](#example-7-recursive-data-classes)
9. [Example 8: Custom Class Methods](#example-8-custom-class-methods)
10. [Example 9: Custom Class Variables](#example-9-custom-class-variables)



Data classes in Python provide a convenient way to create classes with default values, immutable attributes, and automatically generated special methods like `__init__`, `__repr__`, `__eq__`, etc. They are particularly useful for creating classes that represent complex data structures.

Here is a comprehensive guide with code examples for various functionalities of the `dataclasses` module in Python 3.12:

### Installation
Data classes are part of Python's standard library starting from version 3.7, so no installation is necessary. However, if you're using an older version of Python, ensure you have it installed.

### Example 1: Basic Usage

```python
from dataclasses import dataclass

# Define a simple data class with default values
@dataclass
class Point:
    x: int = 0
    y: int = 0

# Create an instance of the Point class
p = Point(3, 4)

# Print the object representation
print(p)  # Output: Point(x=3, y=4)

# Accessing attributes
print(p.x)  # Output: 3
print(p.y)  # Output: 4

# Modify an attribute and print again
p.x = 5
print(p)  # Output: Point(x=5, y=4)
```

### Example 2: Multiple Default Values

```python
from dataclasses import dataclass

# Define a data class with multiple default values
@dataclass
class Circle:
    radius: float = 1.0
    color: str = "red"

# Create an instance of the Circle class
c = Circle()

# Print the object representation
print(c)  # Output: Circle(radius=1.0, color='red')

# Modify attributes and print again
c.radius = 2.5
c.color = "blue"
print(c)  # Output: Circle(radius=2.5, color='blue')
```

### Example 3: Immutable Attributes

```python
from dataclasses import dataclass

# Define a data class with an immutable attribute
@dataclass(frozen=True)
class PointImmutable:
    x: int = 0
    y: int = 0

# Create an instance of the PointImmutable class
p_immutable = PointImmutable(3, 4)

# Attempt to modify an immutable attribute (will raise an error)
try:
    p_immutable.x = 5
except AttributeError as e:
    print(e)  # Output: can't set attribute
```

### Example 4: Custom Initialization

```python
from dataclasses import dataclass

# Define a data class with custom initialization logic
@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        self.full_name = f"{self.name} {self.age}"

# Create an instance of the Person class
p_person = Person("John", 30)

# Print the object representation and the custom attribute
print(p_person)  # Output: Person(name='John', age=30)
print(p_person.full_name)  # Output: John 30
```

### Example 5: Auto-Generated Special Methods

```python
from dataclasses import dataclass

# Define a data class with auto-generated special methods
@dataclass
class Employee:
    name: str
    position: str
    salary: float = 0.0

    def __post_init__(self):
        self.full_name = f"{self.name} ({self.position})"

# Create an instance of the Employee class
e_employee = Employee("Alice", "Developer")

# Print the object representation and the custom attribute
print(e_employee)  # Output: Employee(name='Alice', position='Developer')
print(e_employee.full_name)  # Output: Alice (Developer)
```

### Example 6: Optional Attributes

```python
from dataclasses import dataclass, field

# Define a data class with optional attributes using the `field` function
@dataclass
class Book:
    title: str = field(default="Unknown Title")
    author: str
    year: int = None

# Create an instance of the Book class without specifying optional attributes
b_book = Book("Python Programming")

# Print the object representation and default values for optional attributes
print(b_book)  # Output: Book(title='Python Programming', author=None, year=None)
```

### Example 7: Recursive Data Classes

```python
from dataclasses import dataclass

# Define a recursive data class to represent a tree structure
@dataclass
class TreeNode:
    value: int
    left: 'TreeNode' = None
    right: 'TreeNode' = None

# Create an instance of the TreeNode class as a simple binary search tree
tree = TreeNode(10, TreeNode(5), TreeNode(15))

# Print the object representation and structure
print(tree)  # Output: TreeNode(value=10, left=TreeNode(value=5, left=None, right=None), right=TreeNode(value=15, left=None, right=None))
```

### Example 8: Custom Class Methods

```python
from dataclasses import dataclass

# Define a data class with custom class methods
@dataclass
class Triangle:
    side_a: float
    side_b: float
    side_c: float

    @property
    def is_equilateral(self) -> bool:
        return self.side_a == self.side_b and self.side_b == self.side_c

# Create an instance of the Triangle class
t_triangle = Triangle(3, 3, 3)

# Check if the triangle is equilateral
print(t_triangle.is_equilateral)  # Output: True
```

### Example 9: Custom Class Variables

```python
from dataclasses import dataclass

# Define a data class with custom class variables
@dataclass
class Account:
    balance: float = 0.0

    @classmethod
    def create_new_account(cls, initial_deposit: float) -> 'Account':
        account = cls(initial_deposit)
        return account

# Create a new instance of the Account class using the class method
a_account = Account.create_new_account(100.0)

# Print the object representation and balance
print(a_account)  # Output: Account(balance=100.0)
```

### Example 10: Handling Nested Data Classes

```python
from dataclasses import dataclass

# Define nested data classes to represent a tree structure
@dataclass
class TreeNode:
    value: int
    children: list['TreeNode'] = field(default_factory=list)

# Create an instance of the TreeNode class as a simple binary search tree with nested nodes
tree_nested = TreeNode(10, [TreeNode(5), TreeNode(15)])

# Print the object representation and structure
print(tree_nested)  # Output: TreeNode(value=10, children=[TreeNode(value=5, children=[]), TreeNode(value=15, children=[])])
```

### Example 11: Data Classes with `from __future__ import annotations`

```python
from dataclasses import dataclass
from typing import Union

# Define a data class that uses type hints with `Union` and `from __future__ import annotations`
@dataclass
class Shape:
    shape_type: str = "unknown"
    size: Union[int, float] = 0.0

# Create an instance of the Shape class using type hints
s_shape = Shape(shape_type="circle", size=3.14)

# Print the object representation and attributes
print(s_shape)  # Output: Shape(shape_type='circle', size=3.14)
```

### Example 12: Using `dataclasses.asdict` for Serialization

```python
from dataclasses import dataclass, asdict

# Define a data class with default values
@dataclass
class Person:
    name: str = "John"
    age: int = 30

# Create an instance of the Person class
p_person = Person()

# Convert the data class to a dictionary using `asdict`
person_dict = asdict(p_person)

# Print the resulting dictionary
print(person_dict)  # Output: {'name': 'John', 'age': 30}
```

### Example 13: Using `dataclasses.astuple` for Serialization

```python
from dataclasses import dataclass, astuple

# Define a simple data class with default values
@dataclass
class Point:
    x: int = 0
    y: int = 0

# Create an instance of the Point class
p_point = Point(3, 4)

# Convert the data class to a tuple using `astuple`
point_tuple = astuple(p_point)

# Print the resulting tuple
print(point_tuple)  # Output: (3, 4)
```

### Example 14: Using `dataclasses.replace` for Object Modification

```python
from dataclasses import dataclass, replace

# Define a simple data class with default values
@dataclass
class Person:
    name: str = "John"
    age: int = 30

# Create an instance of the Person class
p_person = Person(name="Alice", age=25)

# Modify the object using `replace`
new_person = replace(p_person, name="Bob")

# Print the modified object
print(new_person)  # Output: Person(name='Bob', age=30)
```

These examples demonstrate various use cases and features of Python's `dataclasses` module, including default values, class methods, custom variables, nested data classes, type hints, serialization, and object modification. Each example provides a practical application of the module to handle complex data structures efficiently.
