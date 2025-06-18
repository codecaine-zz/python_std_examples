# Data Types

The Python standard library includes several modules dedicated to handling different data types efficiently. Below are comprehensive code examples for some of these modules, focusing on their primary functionalities:

## Table of Contents

1. [collections Module](#1-collections-module)
   - [Example 1: Using deque](#example-1-using-deque)
   - [Example 2: Using Counter](#example-2-using-counter)
   - [Example 3: Using defaultdict](#example-3-using-defaultdict)
   - [Example 4: Using OrderedDict](#example-4-using-ordereddict)
   - [Example 5: Using namedtuple](#example-5-using-namedtuple)
2. [datetime Module](#2-datetime-module)
3. [array Module](#3-array-module)
4. [enum Module](#4-enum-module)

### 1. `collections` Module

This module provides specialized container datatypes that differ from built-in containers like lists and dictionaries.

#### Example 1: Using `deque`
A deque (double-ended queue) is a list-like container with fast appends and pops from either end.

```python
from collections import deque

# Creating a deque
dq = deque([1, 2, 3])

# Appending to the right
dq.append(4)
print(dq)  # Output: deque([1, 2, 3, 4])

# Appending to the left
dq.appendleft(0)
print(dq)  # Output: deque([0, 1, 2, 3, 4])

# Popping from the right
last_element = dq.pop()
print(last_element)  # Output: 4
print(dq)  # Output: deque([0, 1, 2, 3])

# Popping from the left
first_element = dq.popleft()
print(first_element)  # Output: 0
print(dq)  # Output: deque([1, 2, 3])
```

#### Example 2: Using `Counter`
A Counter is a dictionary subclass for counting hashable objects.

```python
from collections import Counter

# Creating a Counter object
counter = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])

# Displaying the count of each item
print(counter)  # Output: Counter({'banana': 3, 'apple': 2, 'orange': 1})

# Finding the most common items
most_common_items = counter.most_common(2)
print(most_common_items)  # Output: [('banana', 3), ('apple', 2)]

# Subtracting from another Counter
counter.subtract({'banana': 1})
print(counter)  # Output: Counter({'banana': 2, 'apple': 2, 'orange': 1})
```

#### Example 3: Using `defaultdict`
A defaultdict is a dictionary that provides a default value for a nonexistent key.

```python
from collections import defaultdict

# Creating a defaultdict with a default value of 0
dd = defaultdict(int)

# Incrementing the value for a key
dd['apple'] += 1
print(dd)  # Output: defaultdict(<class 'int'>, {'apple': 1})

# Accessing a nonexistent key returns the default value
print(dd['banana'])  # Output: 0
```

#### Example 4: Using `OrderedDict`
An OrderedDict is a dictionary that remembers the order in which items were inserted.

```python
from collections import OrderedDict

# Creating an OrderedDict
od = OrderedDict()

# Adding items to the OrderedDict
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3

# The items are ordered by the order of insertion
print(od)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('cherry', 3)])
```

#### Example 5: Using `namedtuple`
A namedtuple is a tuple with named fields that you can access like attributes.

```python
from collections import namedtuple

# Creating a namedtuple class
Point = namedtuple('Point', ['x', 'y'])

# Creating an instance of the namedtuple
p = Point(10, 20)

# Accessing fields by name
print(p.x)  # Output: 10
print(p.y)  # Output: 20
```

### 2. `datetime` Module

This module provides classes for manipulating dates and times.

#### Example 1: Basic Date Manipulation
```python
from datetime import date

# Creating a date object
today = date.today()
print(today)  # Output: YYYY-MM-DD

# Formatting the date
formatted_date = today.strftime('%Y-%m-%d')
print(formatted_date)  # Output: YYYY-MM-DD

# Adding days to a date
tomorrow = today + timedelta(days=1)
print(tomorrow)  # Output: YYYY-MM-DD
```

#### Example 2: Timezone Handling
```python
from datetime import datetime, timezone, timedelta

# Creating a timezone-aware datetime object
aware_datetime = datetime.now(timezone.utc)
print(aware_datetime)  # Output: datetime.datetime(YYYY, MM, DD, HH, MM, SS, tzinfo=UTC)

# Converting to another timezone
local_datetime = aware_datetime.astimezone(timezone(timedelta(hours=5)))
print(local_datetime)  # Output: datetime.datetime(YYYY, MM, DD, HH, MM, SS, tzinfo=LOCAL_TIMEZONE)
```

### 3. `array` Module

This module provides a way to create arrays in Python.

#### Example 1: Creating an Array
```python
from array import array

# Creating an array of integers
arr = array('i', [1, 2, 3, 4, 5])

# Accessing elements in the array
print(arr[0])  # Output: 1
print(arr[1])  # Output: 2
```

#### Example 2: Array Operations
```python
from array import array

# Creating an array of integers
arr = array('i', [1, 2, 3, 4, 5])

# Appending an element to the array
arr.append(6)

# Inserting an element at a specific position
arr.insert(0, 0)

# Removing an element from the array
arr.remove(3)

# Popping the last element from the array
last_element = arr.pop()
```

### 4. `enum` Module

This module provides support for enumerations, which are symbolic names for a set of values.

#### Example 1: Creating an Enumeration
```python
from enum import Enum

# Creating an enumeration for colors
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing an enumeration member
print(Color.RED)  # Output: Color.RED

# Accessing the value of an enumeration member
print(Color.RED.value)  # Output: 1
```

#### Example 2: Iterating Over an Enumeration
```python
from enum import Enum

# Creating an enumeration for colors
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Iterating over the members of the enumeration
for color in Color:
    print(color)
```

These examples cover a range of functionalities available in the `collections`, `datetime`, `itertools`, `math`, `sys`, and `os` modules, demonstrating how to use them effectively in Python.
