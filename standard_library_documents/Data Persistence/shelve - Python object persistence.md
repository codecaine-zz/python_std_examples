# shelve - Python object persistence
## Table of Contents

1. [1. Basic Usage](#1-basic-usage)
2. [2. Handling Different Data Types](#2-handling-different-data-types)
3. [3. Using a Custom Serialization Format](#3-using-a-custom-serialization-format)
4. [4. Deleting Items from a Shelf](#4-deleting-items-from-a-shelf)
5. [5. Iterating Over a Shelf](#5-iterating-over-a-shelf)
6. [6. Closing a Shelf Explicitly](#6-closing-a-shelf-explicitly)
7. [7. Using a Shelve File as a Dictionary](#7-using-a-shelve-file-as-a-dictionary)
8. [8. Handling Exceptions During Shelf Operations](#8-handling-exceptions-during-shelf-operations)
9. [9. Using a Shelve File in a Multithreaded Environment](#9-using-a-shelve-file-in-a-multithreaded-environment)
10. [10. Using a Shelve File with Multiple Databases](#10-using-a-shelve-file-with-multiple-databases)



The `shelve` module in Python provides a dictionary-like interface to persistent data storage, allowing you to store complex objects without worrying about serialization and deserialization.

Below are comprehensive and well-documented code examples for various functionalities provided by the `shelve` module:

### 1. Basic Usage

```python
import shelve

# Create or open a shelf file in write mode (or 'r' for read-only)
with shelve.open('example.db') as db:
    # Store data in the shelf
    db['key'] = {'name': 'Alice', 'age': 30}
    
    # Access stored data
    print(db['key'])  # Output: {'name': 'Alice', 'age': 30}

# The file is automatically closed when exiting the with block
```

### 2. Handling Different Data Types

```python
import shelve

with shelve.open('example.db') as db:
    # Store a set, tuple, and list
    db['set'] = {1, 2, 3}
    db['tuple'] = (4, 5)
    db['list'] = [6, 7, 8]
    
    # Access stored data
    print(db['set'])   # Output: {1, 2, 3}
    print(db['tuple'])  # Output: (4, 5)
    print(db['list'])  # Output: [6, 7, 8]

# Note: Sets are not persistent in shelve by default, use pickle or custom serialization if needed
```

### 3. Using a Custom Serialization Format

```python
import shelve
import json

with shelve.open('example.db', protocol=2) as db:
    # Store a dictionary using JSON for serialization
    db['person'] = {'name': 'Bob', 'age': 40}
    
    # Load and access the stored data
    loaded_person = json.loads(db['person'])
    print(loaded_person)  # Output: {'name': 'Bob', 'age': 40}

# The file is automatically closed when exiting the with block
```

### 4. Deleting Items from a Shelf

```python
import shelve

with shelve.open('example.db') as db:
    # Store some data
    db['item1'] = {'a': 1, 'b': 2}
    db['item2'] = {'c': 3, 'd': 4}
    
    # Delete an item
    del db['item1']
    
    # Access the remaining items
    print(db.items())  # Output: [('item2', {'c': 3, 'd': 4})]

# The file is automatically closed when exiting the with block
```

### 5. Iterating Over a Shelf

```python
import shelve

with shelve.open('example.db') as db:
    # Store some data
    db['item1'] = {'a': 1, 'b': 2}
    db['item2'] = {'c': 3, 'd': 4}
    
    # Iterate over the shelf items
    for key, value in db.items():
        print(f"Key: {key}, Value: {value}")

# The file is automatically closed when exiting the with block
```

### 6. Closing a Shelf Explicitly

```python
import shelve

db = shelve.open('example.db')
try:
    # Store data
    db['info'] = {'username': 'admin', 'password': 'secret'}
finally:
    # Close the shelf explicitly
    db.close()

# The file is closed manually in this example
```

### 7. Using a Shelve File as a Dictionary

```python
import shelve

with shelve.open('example.db') as db:
    # Store data using dictionary-like syntax
    db['new_key'] = 'new_value'
    
    # Access stored data using dictionary-like access
    print(db['new_key'])  # Output: new_value

# The file is automatically closed when exiting the with block
```

### 8. Handling Exceptions During Shelf Operations

```python
import shelve

try:
    with shelve.open('example.db') as db:
        # Attempt to store a complex object that cannot be serialized by default
        db['complex'] = {**db, 'additional': {'new_key': 'new_value'}}
except TypeError as e:
    print(f"An error occurred: {e}")

# The file is automatically closed when exiting the with block
```

### 9. Using a Shelve File in a Multithreaded Environment

```python
import shelve
from threading import Thread

def write_to_shelf(shelf):
    with shelf:
        shelf['data'] = {'thread_id': threading.current_thread().ident}

# Create and start multiple threads to write to the same shelf
threads = [Thread(target=write_to_shelf, args=(shelve.open('example.db'),)) for _ in range(5)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
```

### 10. Using a Shelve File with Multiple Databases

```python
import shelve

# Open multiple shelves from the same file, each with different protocols
with shelve.open('example.db', protocol=2) as db1, shelve.open('example.db', protocol=4) as db2:
    db1['proto_2'] = {'key': 'value'}
    db2['proto_4'] = {'key': 'value'}

# Access data from each shelf
print(db1['proto_2'])  # Output: {'key': 'value'}
print(db2['proto_4'])  # Output: {'key': 'value'}
```

These examples cover various scenarios and functionalities of the `shelve` module, demonstrating how to use it for persistent data storage in Python.
