# shelve — Python object persistence

**Shelve Module Documentation**
=====================================

The `shelve` module provides an interface to serialize and deserialize Python objects to and from a file.

**Installation**
---------------

You can install the `shelve` module using pip:

```bash
pip install shelve
```

**Example Usage**
-----------------

Here is an example of how to use the `shelve` module to store and retrieve data:
```python
import shelve

# Open a database file for writing
with shelve.open('example.db') as db:
    # Store some data in the database
    db['name'] = 'John Doe'
    db['age'] = 30
    
    # Retrieve some data from the database
    retrieved_data = db['name']
    
# Open a database file for reading
with shelve.open('example.db') as db:
    # Check if some data was stored in the database
    print(db.get('name'))  # Output: John Doe

# Error handling
try:
    with shelve.open('non_existent_file.db') as db:
        pass
except FileNotFoundError:
    print("The file does not exist")
```

**Shelving an Object**
----------------------

You can shelved objects using the `shelve` module's object methods:

```python
import shelve

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Shelved attribute: only serialized when shelving an instance of this class
    @property
    def __shelved_attributes__(self):
        return ('name', 'age')

# Open a database file for writing
with shelve.open('example.db') as db:
    person = Person('John Doe', 30)
    
    # Shelved attribute is serialized and stored in the database
    db['person'] = person
    
    # Retrieve the shelved object from the database
    retrieved_person = db['person']

# Shelving only a specific subset of attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Shelved attribute: only serialized when shelving an instance of this class
    @property
    def __shelved_attributes__(self):
        return ('name',)

# Open a database file for writing
with shelve.open('example.db') as db:
    person = Person('John Doe', 30)
    
    # Shelved attribute is serialized and stored in the database
    db['person'] = person

# Retrieve the shelved object from the database
retrieved_person = db['person']
```

**Unshelving an Object**
------------------------

You can unshelve objects using the `shelve` module's `unshelf` method:

```python
import shelve

with shelve.open('example.db') as db:
    person = db['person']

# Unshelve the object from the database
unshelved_person = shelve.unshelf(person)

print(unshelved_person.name)  # Output: John Doe
```

**Error Handling**
------------------

The `shelve` module raises an exception when there is a problem with the file or data being shelved:

```python
import shelve

try:
    with shelve.open('non_existent_file.db') as db:
        pass
except FileNotFoundError:
    print("The file does not exist")
except Exception as e:
    print(f"An error occurred: {e}")
```

**Custom Shelving**
-------------------

You can create custom shelving behavior using a class that implements the `shelve.ShelvedObject` interface:

```python
import shelve

class CustomShelvedObject(shelve.ShelvedObject):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method to be called when serializing an instance of this class
    def serialize(self):
        return {'name': self.name, 'age': self.age}

# Open a database file for writing
with shelve.open('example.db') as db:
    person = CustomShelvedObject('John Doe', 30)
    
    # Shelved attribute is serialized and stored in the database
    db['person'] = person

# Retrieve the shelved object from the database
retrieved_person = db['person']

# Unshelve the object from the database
unshelved_person = shelve.unshelf(retrieved_person)

print(unshelved_person.name)  # Output: John Doe
```
