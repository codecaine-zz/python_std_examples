# dbm - Interfaces to Unix “databases”
## Table of Contents

1. [1. Basic Usage with 'gdbm'](#1-basic-usage-with-gdbm)
2. [2. Usage with 'ndbm' (Non-Distributed DBM)](#2-usage-with-ndbm-non-distributed-dbm)
3. [3. Usage with 'gdbm' for String Values](#3-usage-with-gdbm-for-string-values)
4. [4. Usage with 'gdbm' for Binary Data](#4-usage-with-gdbm-for-binary-data)
5. [5. Usage with 'gdbm' for Multiple Keys](#5-usage-with-gdbm-for-multiple-keys)
6. [6. Usage with 'gdbm' for Conditional Storage](#6-usage-with-gdbm-for-conditional-storage)
7. [7. Usage with 'gdbm' for Error Handling](#7-usage-with-gdbm-for-error-handling)
8. [8. Usage with 'gdbm' for Database Closure](#8-usage-with-gdbm-for-database-closure)
9. [9. Usage with 'gdbm' for Database Transaction Management](#9-usage-with-gdbm-for-database-transaction-management)
10. [10. Usage with 'gdbm' for Database Cleanup](#10-usage-with-gdbm-for-database-cleanup)



The `dbm` module in Python provides a simple interface to Unix databases (like DBM, NDBM, GDBM, and BSD DB). While these are low-level interfaces, they offer a basic way to manage key-value pairs. Below are comprehensive examples demonstrating various functionalities of the `dbm` module:

### 1. Basic Usage with 'gdbm'

The first example demonstrates how to use the `gdbm` module for storing and retrieving data.

```python
import gdbm

# Open a database file in write mode
db = gdbm.open('example.db', 'c')

# Store key-value pairs
db['key1'] = 'value1'
db['key2'] = 'value2'

# Retrieve values by keys
print(db['key1'])  # Output: value1

# Iterate over all keys in the database
for key in db.keys():
    print(key, db[key])

# Close the database connection
db.close()
```

### 2. Usage with 'ndbm' (Non-Distributed DBM)

This example shows how to use `ndbm` for managing a database that is not distributed across multiple machines.

```python
import ndbm

# Open a database file in write mode
db = ndbm.open('example.ndb', 'c')

# Store key-value pairs
db['key1'] = 'value1'
db['key2'] = 'value2'

# Retrieve values by keys
print(db['key1'])  # Output: value1

# Iterate over all keys in the database
for key in db.keys():
    print(key, db[key])

# Close the database connection
db.close()
```

### 3. Usage with 'gdbm' for String Values

This example demonstrates how to use `gdbm` with string values.

```python
import gdbm

# Open a database file in write mode
db = gdbm.open('example.db', 'c')

# Store string values using Unicode
db['key1'] = b'value1'
db['key2'] = b'value2'

# Retrieve and decode the value by keys
print(db['key1'].decode('utf-8'))  # Output: value1

# Iterate over all keys in the database and decode values
for key in db.keys():
    print(key, db[key].decode('utf-8'))

# Close the database connection
db.close()
```

### 4. Usage with 'gdbm' for Binary Data

This example shows how to use `gdbm` with binary data.

```python
import gdbm

# Open a database file in write mode
db = gdbm.open('example.db', 'c')

# Store binary data using bytes
data1 = b'\x00\x01\x02'
data2 = b'\x03\x04\x05'

db['key1'] = data1
db['key2'] = data2

# Retrieve and print the binary data by keys
print(db['key1'])  # Output: b'\x00\x01\x02'
print(db['key2'])  # Output: b'\x03\x04\x05'

# Close the database connection
db.close()
```

### 5. Usage with 'gdbm' for Multiple Keys

This example demonstrates how to store and retrieve multiple key-value pairs.

```python
import gdbm

# Open a database file in write mode
db = gdbm.open('example.db', 'c')

# Store multiple key-value pairs
db['key1'] = 'value1'
db['key2'] = 'value2'
db['key3'] = 'value3'

# Retrieve values by keys
print(db['key1'])  # Output: value1
print(db['key2'])  # Output: value2
print(db['key3'])  # Output: value3

# Iterate over all keys in the database
for key in db.keys():
    print(key, db[key])

# Close the database connection
db.close()
```

### 6. Usage with 'gdbm' for Conditional Storage

This example demonstrates how to conditionally store data based on certain conditions.

```python
import gdbm

# Open a database file in write mode
db = gdbm.open('example.db', 'c')

# Conditionally store data
key_to_check = 'specific_key'
value = 'if_true_value' if key_to_check == 'specific_key' else 'if_false_value'

db[key_to_check] = value

# Retrieve and print the stored value
print(db[key_to_check])  # Output: if_true_value

# Close the database connection
db.close()
```

### 7. Usage with 'gdbm' for Error Handling

This example demonstrates how to handle errors when opening a database file.

```python
import gdbm

try:
    # Attempt to open a non-existent database file
    db = gdbm.open('nonexistent.db', 'c')
except gdbm.error as e:
    print(f"Error opening the database: {e}")

# Close the database connection if it was successfully opened
if hasattr(db, 'close'):
    db.close()
```

### 8. Usage with 'gdbm' for Database Closure

This example demonstrates how to ensure proper closure of the database.

```python
import gdbm

try:
    # Open a database file in write mode
    db = gdbm.open('example.db', 'c')

    # Store data in the database
    db['key'] = 'value'

except gdbm.error as e:
    print(f"Error opening or writing to the database: {e}")
else:
    # Ensure the database is closed
    if hasattr(db, 'close'):
        db.close()
```

### 9. Usage with 'gdbm' for Database Transaction Management

This example demonstrates how to manage transactions in `gdbm`.

```python
import gdbm

# Open a database file in write mode
db = gdbm.open('example.db', 'c')

try:
    # Begin a transaction
    db.sync()

    # Store data in the database
    db['key'] = 'value'

    # Commit the transaction
    db.sync()
except gdbm.error as e:
    print(f"Error during database operation: {e}")
else:
    # Ensure the database is closed
    if hasattr(db, 'close'):
        db.close()
```

### 10. Usage with 'gdbm' for Database Cleanup

This example demonstrates how to clean up after using `gdbm`.

```python
import gdbm

try:
    # Open a database file in write mode
    db = gdbm.open('example.db', 'c')

    # Store data in the database
    db['key'] = 'value'

except gdbm.error as e:
    print(f"Error opening or writing to the database: {e}")
else:
    # Ensure the database is closed and removed
    if hasattr(db, 'close'):
        db.close()
    import os
    os.remove('example.db')
```

These examples cover various aspects of using the `dbm` module, from basic operations to error handling and transaction management. For more detailed information, refer to the official Python documentation on [dbm](https://docs.python.org/3/library/dbm.html).
