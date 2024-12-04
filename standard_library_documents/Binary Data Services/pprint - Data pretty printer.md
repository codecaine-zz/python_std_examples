# pprint - Data pretty printer

Below are comprehensive code examples for using the `pprint` module in Python, along with detailed explanations of each example.

### Example 1: Basic Usage

```python
import pprint

# Define a sample data structure
data = {
    'name': 'John Doe',
    'age': 30,
    'is_student': False,
    'courses': ['Math', 'Science', 'English'],
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip': '12345'
    }
}

# Use pprint.pprint() to pretty-print the data
pprint.pprint(data)
```

**Explanation:**
- The `pprint` module provides a way to print complex data structures in a readable format.
- The `pprint.pprint()` function takes an object and prints it with indentation, making it easier to read.

### Example 2: Customizing Output

```python
import pprint

# Define a sample data structure
data = {
    'name': 'Jane Smith',
    'age': 35,
    'is_student': True,
    'courses': ['Biology', 'Chemistry'],
    'address': {
        'street': '456 Elm St',
        'city': 'Othertown',
        'state': 'NY',
        'zip': '67890'
    }
}

# Create a PrettyPrinter instance with custom settings
pp = pprint.PrettyPrinter(indent=2, width=50)

# Use the custom PrettyPrinter to print the data
pp.pprint(data)
```

**Explanation:**
- The `PrettyPrinter` class allows for more customization of the output.
- You can specify the number of spaces per indentation level with the `indent` parameter.
- The maximum line length is controlled by the `width` parameter.

### Example 3: Handling Large Data Structures

```python
import pprint

# Define a large sample data structure
data = {
    'employees': [
        {'name': 'Alice Johnson', 'department': 'Sales'},
        {'name': 'Bob Brown', 'department': 'Marketing'},
        {'name': 'Charlie Smith', 'department': 'IT'}
    ],
    'orders': [
        {'order_id': 101, 'amount': 29.99},
        {'order_id': 102, 'amount': 45.75},
        {'order_id': 103, 'amount': 69.49}
    ]
}

# Use pprint.pprint() to pretty-print the large data structure
pprint.pprint(data)
```

**Explanation:**
- The `pprint` module is particularly useful for handling large or complex data structures.
- It automatically breaks lines and adjusts the indentation to fit within a specified width, which can be helpful when dealing with extensive data.

### Example 4: Using PrettyPrinter for Files

```python
import pprint

# Define a sample data structure
data = {
    'name': 'David Wilson',
    'age': 28,
    'is_student': False,
    'courses': ['History', 'Literature'],
    'address': {
        'street': '789 Oak St',
        'city': 'Somewhere',
        'state': 'TX',
        'zip': '56789'
    }
}

# Open a file for writing and use PrettyPrinter to write the data
with open('data.txt', 'w') as file:
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(data, stream=file)
```

**Explanation:**
- You can also use the `PrettyPrinter` instance to print to a file instead of the console.
- The `stream` parameter is used to specify where the output should be written.

### Example 5: Pretty Printing JSON-like Structures

```python
import pprint
import json

# Define a sample data structure
data = {
    'name': 'Eve Johnson',
    'age': 22,
    'is_student': True,
    'courses': ['Physics', 'Astrophysics'],
    'address': {
        'street': '101 Pine St',
        'city': 'Somewhere Else',
        'state': 'FL',
        'zip': '43210'
    }
}

# Convert the data structure to a JSON string
json_data = json.dumps(data, indent=2)

# Use pprint.pprint() to pretty-print the JSON-like structure
pprint.pprint(json_data)
```

**Explanation:**
- The `json` module can be used to convert data structures into JSON format.
- You can then use the `pprint` module to print this JSON string in a readable format.

These examples demonstrate various ways to use the `pprint` module, from basic usage to more complex scenarios. By following these examples, you can effectively leverage the `pprint` module to enhance the readability of your data structures in Python.
