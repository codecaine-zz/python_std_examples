# dataclasses — Data Classes

**Data Classes**
================

The `dataclasses` module provides support for creating classes that mainly contain data and have minimal runtime overhead.

### Example Use Case:

Let's create a simple `Person` class using data classes:
```python
from dataclasses import dataclass

# Define a data class with fields
@dataclass
class Person:
    """A simple data class representing a person"""
    name: str  # Name of the person
    age: int   # Age of the person
    city: str  # City where the person lives

# Create an instance of the Person class
person = Person(
    name="John Doe",
    age=30,
    city="New York"
)

# Print the data stored in the class
print(person)  # Output: Person(name='John Doe', age=30, city='New York')

# Accessing fields:
print(person.name)  # Output: John Doe
print(person.age)   # Output: 30
print(person.city)  # Output: New York

# Update values:
person.name = "Jane Doe"
print(person)  # Output: Person(name='Jane Doe', age=30, city='New York')

# You can also add a constructor using the __post_init__ method
@dataclass(post_init=True)
class Person2:
    """A data class with a constructor"""
    name: str
    age: int

    def __post_init__(self):
        self.city = f"{self.name}ville"

person2 = Person2(
    name="John Doe",
    age=30
)

print(person2)  # Output: Person2(name='John Doe', age=30)
```
### Additional Methods:

Data classes also support additional methods such as `__str__` and `__repr__`. These methods allow you to customize how the data class is represented when it's converted into a string.

```python
from dataclasses import dataclass

@dataclass
class Person:
    """A simple data class representing a person"""
    name: str  # Name of the person
    age: int   # Age of the person
    city: str  # City where the person lives

# Define custom __str__ and __repr__ methods
    @staticmethod
    def _format_name(name):
        return f"{name[0].upper()} {name.lower()[1:]}"

    def __post_init__(self):
        self.city = f"{self._format_name(self.name)}ville"
        super().__post_init__()

# Create an instance of the Person class
person = Person(
    name="John Doe",
    age=30,
    city="New York"
)

# Print the data stored in the class using custom __str__ and __repr__ methods
print(person)  # Output: Person(name='JOHN doe', age=30, city='NYC')
```

### Class Attributes:

Data classes can also support class attributes. These are useful when you need to store common values that apply to all instances of the class.

```python
from dataclasses import dataclass

@dataclass
class Person:
    """A simple data class representing a person"""
    name: str  # Name of the person
    age: int   # Age of the person
    city: str  # City where the person lives

# Define class attributes
    class_name = "Human"
    species = "Homo sapiens"

# Create an instance of the Person class
person1 = Person(
    name="John Doe",
    age=30,
    city="New York"
)

# Access class attributes:
print(Person.class_name)  # Output: Human
print(person1.species)   # Output: Homo sapiens

# You can also use class attributes in methods
class PersonMethods:
    def __init__(self):
        self._species = Person.species

    @property
    def species(self):
        return self._species

person2 = PersonMethods()

print(person2.species)  # Output: Homo sapiens
```

### Enumerations:

Data classes can also support enumerations. These are useful when you need to represent a fixed set of values.

```python
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class Color(Enum):
    """An enumeration representing different colors"""
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

# Create an instance of the Color class
color = Color.RED

# Accessing values:
print(color.value)  # Output: red

# You can also use enum members as attributes
class ShapeDataclass:
    def __init__(self):
        self._shape = field(default=Color.GREEN)

    @property
    def shape(self):
        return self._shape

shape_dataclass = ShapeDataclass()

print(shape_dataclass.shape)  # Output: Color.GREEN
```

### Type Hints:

Finally, data classes support type hints. These are useful when you need to specify the types of attributes in your class.

```python
from dataclasses import dataclass

@dataclass
class Person:
    """A simple data class representing a person"""
    name: str  # Name of the person (string)
    age: int   # Age of the person (integer)

# Create an instance of the Person class with type hints
person = Person(
    name="John Doe",  # string
    age=30           # integer
)

# Accessing attributes:
print(person.name)  # Output: John Doe (string)
print(person.age)   # Output: 30 (integer)

# You can also use type aliases
from dataclasses import dataclass

@dataclass
class Person:
    """A simple data class representing a person"""
    name: str  # Name of the person (string)
    age: int   # Age of the person (integer)

    @staticmethod
    def get_age(age: int) -> int:
        return age  # integer

person = Person(
    name="John Doe",  # string
    age=30           # integer
)

# Accessing attributes using type alias:
print(Person.get_age(person.age))  # Output: 30 (integer)
```
