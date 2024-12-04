# Data Types

The Python standard library includes several modules dedicated to handling different data types efficiently. Below are comprehensive code examples for some of these modules, focusing on their primary functionalities:

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

### 3. `itertools` Module

This module provides various functions to create iterators for efficient looping.

#### Example 1: Using `count`
```python
from itertools import count

# Creating an infinite counter
counter = count(start=5)

# Generating the first five numbers in the sequence
for _ in range(5):
    print(next(counter))  # Output: 5, 6, 7, 8, 9
```

#### Example 2: Using `cycle`
```python
from itertools import cycle

# Creating an infinite cycle iterator
cycler = cycle(['A', 'B', 'C'])

# Generating the first ten elements in the sequence
for _ in range(10):
    print(next(cycler))  # Output: A, B, C, A, B, C, A, B, C, A
```

### 4. `random` Module

This module provides functions to generate random numbers and make random selections.

#### Example 1: Generating a Random Float
```python
import random

# Generating a random float between 0.0 and 1.0
random_float = random.random()
print(random_float)  # Output: 0.987654321 (approximately)
```

#### Example 2: Choosing a Random Element from a List
```python
import random

fruits = ['apple', 'banana', 'cherry']
random_fruit = random.choice(fruits)
print(random_fruit)  # Output: apple or banana or cherry randomly selected
```

### 5. `math` Module

This module provides mathematical functions.

#### Example 1: Mathematical Constants
```python
import math

# Accessing the value of pi
pi_value = math.pi
print(pi_value)  # Output: 3.141592653589793

# Calculating the square root of a number
sqrt_2 = math.sqrt(2)
print(sqrt_2)  # Output: 1.4142135623730951
```

#### Example 2: Trigonometric Functions
```python
import math

# Calculating the sine of an angle in radians
sin_value = math.sin(math.pi / 4)
print(sin_value)  # Output: 0.7071067811865476
```

### 6. `sys` Module

This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

#### Example 1: Accessing Command-Line Arguments
```python
import sys

# List of command-line arguments (sys.argv)
print(sys.argv)  # Output: ['script_name', 'arg1', 'arg2', ...]
```

### 7. `os` Module

This module provides a portable way of using operating system dependent functionality.

#### Example 1: Listing Files in a Directory
```python
import os

# List all files and directories in the current working directory
files_and_dirs = os.listdir('.')
print(files_and_dirs)  # Output: ['file1.txt', 'file2.txt', ...]
```

#### Example 2: Changing Current Working Directory
```python
import os

os.chdir('/path/to/new/directory')
current_directory = os.getcwd()
print(current_directory)  # Output: /path/to/new/directory
```

These examples cover a range of functionalities available in the `collections`, `datetime`, `itertools`, `math`, `sys`, and `os` modules, demonstrating how to use them effectively in Python.
