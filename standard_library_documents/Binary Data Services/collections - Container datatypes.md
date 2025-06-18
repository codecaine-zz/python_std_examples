# collections - Container datatypes

## Table of Contents

1. [Counter](#1-counter) - Hash-based counting of elements
2. [OrderedDict](#2-ordereddict) - Dictionary that remembers insertion order
3. [defaultdict](#3-defaultdict) - Dictionary with automatic default values
4. [namedtuple](#4-namedtuple) - Tuple subclass with named fields
5. [deque](#5-deque) - Double-ended queue with fast operations
6. [ChainMap](#6-chainmap) - Multiple dictionaries as a single mapping
7. [UserDict](#7-userdict) - Base class for dictionary customization
8. [UserList](#8-userlist) - Base class for list customization
9. [UserString](#9-userstring) - Base class for string customization

## Overview

The `collections` module provides specialized container datatypes as alternatives to Python's built-in containers (`dict`, `list`, `set`, and `tuple`). These containers are optimized for specific use cases and can significantly improve both code readability and performance when used appropriately.

## Container Types Comparison

| Container Type | Time Complexity (Common Operations) | Memory Usage | Best For |
|---------------|-----------------------------------|--------------|-----------|
| Counter       | O(1) for updates/lookups          | Moderate     | Counting elements, multisets |
| OrderedDict   | O(1) for updates/lookups          | High         | Fixed ordering requirements |
| defaultdict   | O(1) for updates/lookups          | Moderate     | Automatic default values |
| namedtuple    | O(1) for attribute access         | Low          | Lightweight object storage |
| deque         | O(1) for both ends               | Moderate     | FIFO/LIFO queues |

---

### 1. Counter

**Description:**
A dictionary subclass for counting hashable objects. Elements are stored as dictionary keys and their counts as dictionary values.

**Common Use Cases:**

1. Word frequency analysis
2. Character counting in strings
3. Event counting in logs
4. Implementation of multisets

**Example:**

```python
from collections import Counter

# Basic counting
text = "mississippi"
char_count = Counter(text)
print(char_count)  # Output: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Advanced operations
counter1 = Counter(['a', 'b', 'b', 'c'])
counter2 = Counter(['b', 'b', 'c', 'd'])

# Addition (union)
print(counter1 + counter2)  # Counter({'b': 4, 'c': 2, 'a': 1, 'd': 1})

# Subtraction (difference)
print(counter1 - counter2)  # Counter({'a': 1})

# Most common elements
print(char_count.most_common(2))  # [('i', 4), ('s', 4)]
```

**Best Practices:**

1. Use `most_common()` for efficient top-N queries
2. Use `update()` for batch counting instead of individual additions
3. Use `total()` to get the sum of all counts

**Common Pitfalls:**

- Negative counts are allowed but not included in most operations
- `del` is needed to completely remove an element

---

### 2. OrderedDict

**Description:**
An ordered dictionary that remembers the order in which its contents are added. This is useful when you need to maintain the insertion order of keys.

**Example:**

```python
from collections import OrderedDict

# Example with an ordered dictionary
ordered_dict = OrderedDict()
ordered_dict['apple'] = 1
ordered_dict['banana'] = 2
ordered_dict['orange'] = 3
print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])

# Example with a dictionary and sorting
regular_dict = {'banana': 2, 'apple': 1, 'orange': 3}
ordered_dict = OrderedDict(sorted(regular_dict.items()))
print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])
```

**Explanation:**

- The `OrderedDict` class maintains the insertion order of its elements, which is not guaranteed by regular dictionaries.
- This can be useful in scenarios where maintaining order is important, such as caching or certain types of configurations.


---

### 3. defaultdict

**Description:**
A dictionary subclass that calls a factory function to provide missing values.

**Example:**

```python
from collections import defaultdict

# Example with a defaultdict to count even and odd numbers
count_dict = defaultdict(list)
for number in range(10):
    if number % 2 == 0:
        count_dict['even'].append(number)
    else:
        count_dict['odd'].append(number)

print(count_dict)  # Output: defaultdict(<class 'list'>, {'even': [0, 2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]})

# Example with a defaultdict and a custom factory function
def default_factory():
    return "default value"

custom_dict = defaultdict(default_factory)
print(custom_dict["missing_key"])  # Output: default value
```

**Explanation:**

- The `defaultdict` class is used to initialize dictionary values automatically.
- In this example, it initializes a list for each key that does not already exist in the dictionary.

---

### 4. namedtuple

**Description:**
A factory function returning a new tuple subclass with named fields.

**Example:**

```python
from collections import namedtuple

# Example with a named tuple to represent a point in 2D space
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(x=3, y=4)

print(p1)  # Output: Point(x=1, y=2)
print(p2)  # Output: Point(x=3, y=4)

# Example with a named tuple to represent a person
Person = namedtuple('Person', ['name', 'age'])
person = Person(name="Alice", age=30)

print(person)  # Output: Person(name='Alice', age=30)
print(person.name)  # Output: Alice
print(person.age)  # Output: 30
```

**Explanation:**

- The `namedtuple` function creates a subclass of tuple with named fields.
- This makes the tuple more readable and convenient for representing objects with specific attributes.

---

### 5. deque

**Description:**
A double-ended queue optimized for fast appends and pops from both ends, with optional maximum length.

**Use Cases:**

1. Implementing sliding windows
2. Managing history with fixed size
3. Round-robin scheduling
4. Producer-consumer queues

**Example:**

```python
from collections import deque

# Sliding window example
def moving_average(data, window_size):
    window = deque(maxlen=window_size)
    averages = []
    
    for x in data:
        window.append(x)
        averages.append(sum(window) / len(window))
    
    return averages

# Example usage
data = [1, 2, 3, 4, 5, 6, 7]
print(moving_average(data, 3))  # Output: [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]

# Circular buffer example
history = deque(maxlen=3)
for i in range(5):
    history.append(i)
print(history)  # Output: deque([2, 3, 4], maxlen=3)

# Rotation example
d = deque([1, 2, 3, 4, 5])
d.rotate(2)  # Rotate two steps right
print(d)  # Output: deque([4, 5, 1, 2, 3])
d.rotate(-2)  # Rotate two steps left
print(d)  # Output: deque([1, 2, 3, 4, 5])
```

**Performance Characteristics:**

- O(1) for append/pop at either end
- O(n) for random access
- O(k) for rotation of k elements
- Thread-safe for append/pop operations

**Best Practices:**

1. Use `maxlen` parameter for sliding windows
2. Prefer `appendleft()`/`popleft()` over `insert(0)`/`pop(0)`
3. Use `rotate()` for efficient circular operations

---

### 6. ChainMap

**Description:**
A collection which provides a way to group multiple mappings as if they were one, but which does not actually merge them.

**Example:**

```python
from collections import ChainMap

# Example with chain maps for combining multiple dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

combined_dict = ChainMap(dict1, dict2)
print(combined_dict)  # Output: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

# Example with chain maps and updating values
dict1['a'] = 5
print(combined_dict)  # Output: ChainMap({'a': 5, 'b': 2}, {'b': 3, 'c': 4})
```

**Explanation:**

- The `ChainMap` class allows you to create a new dictionary that combines multiple dictionaries.
- It will prioritize the first dictionary when retrieving values for keys that exist in more than one.

---

### 7. UserDict

**Description:**
A subclass of dict providing a base class for dictionary subclasses.

**Example:**

```python
from collections import UserDict

# Example with a user-defined dictionary subclass
class MyDict(UserDict):
    def __missing__(self, key):
        # Custom behavior when an item is missing
        return f"Key {key} not found"

my_dict = MyDict()
my_dict['name'] = 'Alice'
print(my_dict)  # Output: {'name': 'Alice'}
print(my_dict['age'])  # Output: Key age not found

# Example with a user-defined dictionary subclass and custom initialization
class MyDictWithInit(UserDict):
    def __init__(self, initial_data):
        super().__init__(initial_data)
        self.custom_attribute = 'custom_value'

my_dict_with_init = MyDictWithInit({'key1': 'value1'})
print(my_dict_with_init)  # Output: {'key1': 'value1'}
print(my_dict_with_init.custom_attribute)  # Output: custom_value
```

**Explanation:**

- The `UserDict` class allows you to create a custom dictionary subclass with additional behavior.
- It provides a method `__missing__` that can be overridden to customize the behavior when a key is missing.

---

### 8. UserList

**Description:**
A subclass of list providing a base class for list subclasses.

**Example:**

```python
from collections import UserList

# Example with a user-defined list subclass
class MyList(UserList):
    def __init__(self, iterable=()):
        # Custom initialization behavior
        super().__init__(iterable)
        self.custom_attribute = 'hello'

my_list = MyList([1, 2, 3])
print(my_list)  # Output: [1, 2, 3]
print(my_list.custom_attribute)  # Output: hello

# Example with a user-defined list subclass and custom method
class MyListWithMethod(UserList):
    def custom_method(self):
        return sum(self)

my_list_with_method = MyListWithMethod([1, 2, 3])
print(my_list_with_method)  # Output: [1, 2, 3]
print(my_list_with_method.custom_method())  # Output: 6
```

**Explanation:**

- The `UserList` class allows you to create a custom list subclass with additional behavior.
- It provides a method `__init__` that can be overridden to customize initialization.

---

### 9. UserString

**Description:**
A subclass of str providing a base class for string subclasses.

**Example:**

```python
from collections import UserString

# Example with a user-defined string subclass
class MyString(UserString):
    def __init__(self, data=''):
        # Custom initialization behavior
        super().__init__(data)
        self.custom_attribute = 'world'

my_string = MyString('hello')
print(my_string)  # Output: hello
print(my_string.custom_attribute)  # Output: world

# Example with a user-defined string subclass and custom method
class MyStringWithMethod(UserString):
    def custom_method(self):
        return self.data.upper()

my_string_with_method = MyStringWithMethod('hello')
print(my_string_with_method)  # Output: hello
print(my_string_with_method.custom_method())  # Output: HELLO
```

**Explanation:**

- The `UserString` class allows you to create a custom string subclass with additional behavior.
- It provides a method `__init__` that can be overridden to customize initialization.

---

## Common Design Patterns with Collections

### 1. Caching with OrderedDict

```python
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
```

### 2. Event Handling with defaultdict

```python
from collections import defaultdict

class EventSystem:
    def __init__(self):
        self.handlers = defaultdict(list)
    
    def subscribe(self, event_type, handler):
        self.handlers[event_type].append(handler)
    
    def emit(self, event_type, data):
        for handler in self.handlers[event_type]:
            handler(data)
```

## Best Practices Summary

1. Choose the right container:

   - Use `Counter` for counting
   - Use `defaultdict` for automatic defaults
   - Use `deque` for queue operations
   - Use `namedtuple` for lightweight objects
   - Use `OrderedDict` when order matters

2. Performance Considerations:

   - `deque` over `list` for queue operations
   - `Counter` over manual counting
   - `defaultdict` over manual key initialization

3. Memory Usage:

   - `namedtuple` for memory-efficient objects
   - Use `maxlen` with `deque` for bounded memory
   - Clear unused collections to free memory

## Common Pitfalls and Solutions

1. **Mutable Default Values**
   - Problem: Using mutable default values in `defaultdict`
   - Solution: Use factory functions that return new instances

2. **OrderedDict vs dict**
   - Problem: Using OrderedDict when regular dict would suffice (Python 3.7+)
   - Solution: Use regular dict unless explicit ordering behavior is needed

3. **Counter Arithmetic**
   - Problem: Unexpected behavior with negative counts
   - Solution: Use Counter's mathematical operations carefully

4. **namedtuple Immutability**
   - Problem: Attempting to modify namedtuple fields
   - Solution: Use _replace() method or create new instance

## Further Reading

- [Python Collections Documentation](https://docs.python.org/3/library/collections.html)
- [PEP 468 - Preserving the order of **kwargs in a function](https://www.python.org/dev/peps/pep-0468/)
- [Raymond Hettinger's Python Recipes](https://code.activestate.com/recipes/users/178123/)
