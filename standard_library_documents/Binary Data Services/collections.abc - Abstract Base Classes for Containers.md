# collections.abc - Abstract Base Classes for Containers

Below are comprehensive examples of how to use the `collections.abc` module, which provides abstract base classes for various container types like sequences and mappings.

### 1. Sequence ABC

#### Example: Implementing a Custom Sequence

```python
from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self, elements):
        self._elements = list(elements)

    def __getitem__(self, index):
        return self._elements[index]

    def __len__(self):
        return len(self._elements)

# Usage
my_list = MyList([1, 2, 3, 4, 5])
print(list(my_list))  # Output: [1, 2, 3, 4, 5]
print(len(my_list))    # Output: 5
```

### 2. Mapping ABC

#### Example: Implementing a Custom Dictionary

```python
from collections.abc import Mapping

class MyDict(Mapping):
    def __init__(self, key_value_pairs):
        self._data = dict(key_value_pairs)

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def keys(self):
        return iter(self._data.keys())

    def values(self):
        return iter(self._data.values())

# Usage
my_dict = MyDict({'a': 1, 'b': 2, 'c': 3})
print(my_dict['a'])     # Output: 1
print(len(my_dict))       # Output: 3
for key in my_dict:
    print(key)             # Output: a b c
```

### 3. Mutable Sequence ABC

#### Example: Implementing a Custom Mutable List

```python
from collections.abc import MutableSequence

class MyMutableList(MutableSequence):
    def __init__(self, elements=None):
        self._elements = list(elements) if elements is not None else []

    def insert(self, index, element):
        self._elements.insert(index, element)

    def __getitem__(self, index):
        return self._elements[index]

    def __delitem__(self, index):
        del self._elements[index]

    def __len__(self):
        return len(self._elements)

# Usage
my_list = MyMutableList([1, 2, 3])
print(my_list)     # Output: [1, 2, 3]
my_list.insert(1, 4)
print(my_list)     # Output: [1, 4, 2, 3]
del my_list[1]
print(my_list)     # Output: [1, 2, 3]
```

### 4. Mutable Mapping ABC

#### Example: Implementing a Custom Mutable Dictionary

```python
from collections.abc import MutableMapping

class MyMutableDict(MutableMapping):
    def __init__(self, key_value_pairs=None):
        self._data = dict(key_value_pairs) if key_value_pairs is not None else {}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __len__(self):
        return len(self._data)

    def keys(self):
        return iter(self._data.keys())

    def values(self):
        return iter(self._data.values())

# Usage
my_dict = MyMutableDict({'a': 1, 'b': 2})
print(my_dict)           # Output: {'a': 1, 'b': 2}
my_dict['c'] = 3
print(my_dict)           # Output: {'a': 1, 'b': 2, 'c': 3}
del my_dict['a']
print(my_dict)           # Output: {'b': 2, 'c': 3}
```

### 5. Set ABC

#### Example: Implementing a Custom Set

```python
from collections.abc import Set

class MySet(Set):
    def __init__(self, elements=None):
        self._elements = set(elements) if elements is not None else set()

    def add(self, element):
        self._elements.add(element)

    def remove(self, element):
        self._elements.remove(element)

    def __contains__(self, element):
        return element in self._elements

    def __len__(self):
        return len(self._elements)

# Usage
my_set = MySet([1, 2, 3])
print(1 in my_set)      # Output: True
my_set.add(4)
print(4 in my_set)      # Output: True
my_set.remove(1)
print(my_set)            # Output: {2, 3, 4}
```

### 6. Deque ABC

#### Example: Implementing a Custom Double-Ended Queue

```python
from collections.abc import Deque

class MyDeque(Deque):
    def appendleft(self, element):
        self._elements.appendleft(element)

    def popleft(self):
        return self._elements.popleft()

# Usage
my_deque = MyDeque()
my_deque.appendleft(1)
my_deque.appendleft(2)
print(list(my_deque))  # Output: [2, 1]
first_element = my_deque.popleft()
print(first_element)    # Output: 2
```

These examples demonstrate how to implement custom container types by subclassing the abstract base classes provided in `collections.abc`. Each example includes comments explaining the purpose of each method and demonstrates its usage.
