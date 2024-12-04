# collections.abc — Abstract Base Classes for Containers

**Abstract Base Classes for Containers**

The `collections.abc` module provides abstract base classes for common container types such as sets, dictionaries, lists, and tuples.

### Importing Modules

```python
import collections.abc
```

### 1. `ABC`
The `ABC` class is the base class for all other abstract base classes in this module.

```python
# Define a new abstract class that inherits from ABC
class MyAbstractClass(collections.abc.ABC):
    @collections.abcabstractmethod
    def my_method(self) -> None:
        """Define an abstract method"""
        pass

# Attempt to create an instance of the abstract class will raise an error
try:
    obj = MyAbstractClass()
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```

### 2. `ABCMeta`
The `ABCMeta` class is a metaclass used for creating abstract base classes.

```python
# Use ABCMeta to create an abstract base class
class MyAbstractClass(collections.abc.ABC, metaclass=collections.abc.ABCMeta):
    @collections.abcabstractmethod
    def my_method(self) -> None:
        """Define an abstract method"""
        pass

# This will not raise an error because it's a concrete class
obj = MyAbstractClass()
print(obj)
```

### 3. `AbstractSet`
The `AbstractSet` class is an abstract base class for sets.

```python
# Create a new set of integers
my_set = {1, 2, 3}

try:
    # Attempt to create a set with duplicate elements will raise an error
    my_set_with_duplicates = {1, 2, 2}
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```

### 4. `AbstractMapping`
The `AbstractMapping` class is an abstract base class for dictionaries.

```python
# Create a new dictionary of integers
my_dict = {1: 'a', 2: 'b'}

try:
    # Attempt to create a dictionary with duplicate keys will raise an error
    my_dict_with_duplicates = {1: 'a', 2: 'b', 3: 'c'}
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```

### 5. `AbstractSequence`
The `AbstractSequence` class is an abstract base class for sequences.

```python
# Create a new sequence of integers
my_sequence = [1, 2, 3]

try:
    # Attempt to create a sequence with non-sequential elements will raise an error
    my_sequence_with_non_sequential_elements = ['a', 'b', 1]
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```

### 6. `AbstractMutableSequence`
The `AbstractMutableSequence` class is an abstract base class for mutable sequences.

```python
# Create a new mutable sequence of integers
my_mutable_sequence = [1, 2, 3]

try:
    # Attempt to modify the mutable sequence will raise an error
    my_mutable_sequence[0] = 'a'
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```

### 7. `AbstractMutableMapping`
The `AbstractMutableMapping` class is an abstract base class for mutable mappings.

```python
# Create a new mutable mapping of integers to strings
my_mutable_mapping = {1: 'a', 2: 'b'}

try:
    # Attempt to modify the mutable mapping will raise an error
    my_mutable_mapping[3] = 'c'
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```

### 8. `AbstractMutableSequenceProxy`
The `AbstractMutableSequenceProxy` class is an abstract base class for mutable sequence proxies.

```python
# Create a new mutable sequence proxy of integers
my_mutable_sequence_proxy = collections.abc.AbstractMutableSequenceProxy()

try:
    # Attempt to modify the mutable sequence proxy will raise an error
    my_mutable_sequence_proxy[0] = 'a'
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```

### 9. `AbstractMutableMappingProxy`
The `AbstractMutableMappingProxy` class is an abstract base class for mutable mapping proxies.

```python
# Create a new mutable mapping proxy of integers to strings
my_mutable_mapping_proxy = collections.abc.AbstractMutableMappingProxy()

try:
    # Attempt to modify the mutable mapping proxy will raise an error
    my_mutable_mapping_proxy[3] = 'c'
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```

### 10. `AbstractSetProxy`
The `AbstractSetProxy` class is an abstract base class for set proxies.

```python
# Create a new set proxy of integers
my_set_proxy = collections.abc.AbstractSetProxy()

try:
    # Attempt to add an element to the set proxy will raise an error
    my_set_proxy.add(1)
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```

### 11. `AbstractMappingProxy`
The `AbstractMappingProxy` class is an abstract base class for mapping proxies.

```python
# Create a new mapping proxy of integers to strings
my_mapping_proxy = collections.abc.AbstractMappingProxy()

try:
    # Attempt to modify the mapping proxy will raise an error
    my_mapping_proxy[1] = 'b'
except collections.abc.ABCError as e:
    print(f"Error: {e}")
```
