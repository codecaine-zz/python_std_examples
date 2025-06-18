# plistlib - Generate and parse Apple .plist files
## Table of Contents

1. [Example 1: Writing a Simple Plist](#example-1-writing-a-simple-plist)
2. [Example 2: Parsing a Plist](#example-2-parsing-a-plist)
3. [Example 3: Writing a Plist with DateTime Objects](#example-3-writing-a-plist-with-datetime-objects)
4. [Example 4: Parsing a Plist with DateTime Objects](#example-4-parsing-a-plist-with-datetime-objects)
5. [Example 5: Writing a Plist with Nested Lists](#example-5-writing-a-plist-with-nested-lists)
6. [Example 6: Parsing a Plist with Nested Lists](#example-6-parsing-a-plist-with-nested-lists)
7. [Example 7: Writing a Plist with Custom Objects](#example-7-writing-a-plist-with-custom-objects)
8. [Example 8: Parsing a Plist with Custom Objects](#example-8-parsing-a-plist-with-custom-objects)



The `plistlib` module in Python is used to read from and write to Apple Property List (`.plist`) files, which are a common data storage format used by macOS. Below are comprehensive code examples that demonstrate how to use the `plistlib` module to generate and parse `.plist` files.

### Example 1: Writing a Simple Plist

```python
import plistlib

# Create a dictionary
data = {
    "Name": "John Doe",
    "Age": 30,
    "IsEmployed": True,
    "Address": {
        "Street": "123 Elm St",
        "City": "Anytown"
    },
    "Phones": [
        {"Type": "Home", "Number": "555-1234"},
        {"Type": "Work", "Number": "555-5678"}
    ]
}

# Write the dictionary to a .plist file
with open('example.plist', 'wb') as f:
    plistlib.dump(data, f)

print("Plist has been written to example.plist")
```

### Example 2: Parsing a Plist

```python
import plistlib

# Read a .plist file and parse it into a dictionary
with open('example.plist', 'rb') as f:
    data = plistlib.load(f)

# Print the parsed data
print("Parsed Data:")
print(data)
```

### Example 3: Writing a Plist with DateTime Objects

```python
import plistlib
from datetime import datetime

# Create a dictionary with a date-time object
data = {
    "EventDate": datetime.now(),
    "Description": "This is an example event."
}

# Write the dictionary to a .plist file
with open('event.plist', 'wb') as f:
    plistlib.dump(data, f)

print("Plist has been written to event.plist")
```

### Example 4: Parsing a Plist with DateTime Objects

```python
import plistlib
from datetime import datetime

# Read a .plist file and parse it into a dictionary
with open('event.plist', 'rb') as f:
    data = plistlib.load(f)

# Extract and print the date-time object
event_date = data.get('EventDate')
if event_date:
    print("Event Date:", event_date)
else:
    print("Event Date not found.")
```

### Example 5: Writing a Plist with Nested Lists

```python
import plistlib

# Create a dictionary with nested lists
data = {
    "Tasks": [
        {"Name": "Complete report", "DueDate": datetime.now() + timedelta(days=7)},
        {"Name": "Read a book", "DueDate": datetime.now() + timedelta(days=3)}
    ]
}

# Write the dictionary to a .plist file
with open('tasks.plist', 'wb') as f:
    plistlib.dump(data, f)

print("Plist has been written to tasks.plist")
```

### Example 6: Parsing a Plist with Nested Lists

```python
import plistlib
from datetime import datetime

# Read a .plist file and parse it into a dictionary
with open('tasks.plist', 'rb') as f:
    data = plistlib.load(f)

# Extract and print the tasks list
tasks = data.get('Tasks')
if tasks:
    for task in tasks:
        print("Task Name:", task.get('Name'))
        print("Due Date:", task.get('DueDate'))
else:
    print("Tasks not found.")
```

### Example 7: Writing a Plist with Custom Objects

If you need to handle custom objects, `plistlib` can be extended by using the `DataHandler` class. Here’s an example of how to define and use a custom handler for a specific type:

```python
import plistlib

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_to_plist(person):
    return {
        '_type': 'Person',
        'name': person.name,
        'age': person.age
    }

def person_from_plist(data):
    if data['_type'] != 'Person':
        raise ValueError("Invalid data type")
    return Person(data['name'], data['age'])

# Create a list of custom objects
people = [Person('Alice', 30), Person('Bob', 25)]

# Define a custom handler for the Person class
handler = plistlib.DataHandler(person_to_plist, person_from_plist)

# Write the list of custom objects to a .plist file using the custom handler
with open('people.plist', 'wb') as f:
    plistlib.dump(people, f, data_handler=handler)

print("Plist has been written to people.plist")
```

### Example 8: Parsing a Plist with Custom Objects

```python
import plistlib

# Define the custom handler for the Person class
def person_to_plist(person):
    return {
        '_type': 'Person',
        'name': person.name,
        'age': person.age
    }

def person_from_plist(data):
    if data['_type'] != 'Person':
        raise ValueError("Invalid data type")
    return Person(data['name'], data['age'])

# Read a .plist file and parse it into a list of custom objects using the custom handler
with open('people.plist', 'rb') as f:
    people = plistlib.load(f, data_handler=handler)

# Print the parsed persons
for person in people:
    print("Person Name:", person.name)
    print("Person Age:", person.age)
```

These examples cover various aspects of using `plistlib`, from basic dictionary operations to handling custom objects and date-time objects. The code is designed to be clear, well-documented, and suitable for inclusion in official documentation.
