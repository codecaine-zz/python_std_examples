# pprint — Data pretty printer

Here's an example of how you can use the `pprint` function from Python's standard library:

```python
import pprint

# Define a simple data structure (a dictionary)
data = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'US',
        'zip': '12345'
    },
    'interests': ['reading', 'hiking', 'coding']
}

# Pretty print the data structure
pprint.pprint(data)

# Pretty print a nested list
nested_list = [1, 2, [3, 4], {'a': 5}]
pprint.pprint(nested_list)

# Pretty print a dictionary with values that are lists or dictionaries themselves
data_with_nested_values = {
    'name': 'Jane Doe',
    'age': 25,
    'address': {
        'street': '456 Elm St',
        'city': 'Othertown',
        'state': 'Canada',
        'zip': '67890'
    },
    'interests': ['reading', 'traveling']
}
pprint.pprint(data_with_nested_values)
```

Output:

```python
{'age': 30, 
 'address': {'city': 'Anytown', 
  'state': 'US', 
  'street': '123 Main St', 
  'zip': '12345'}, 
 'interests': ['reading', 'hiking', 'coding'], 
 'name': 'John Doe'}

[1, 2, [3, 4], {'a': 5}]

{'age': 25, 
 'address': {'city': 'Othertown', 
  'state': 'Canada', 
  'street': '456 Elm St', 
  'zip': '67890'}, 
 'interests': ['reading', 'traveling'], 
 'name': 'Jane Doe'}
```

This function is useful for printing data structures in a human-readable format, making it easier to debug and understand complex data.

Here's an example of how you can customize the pretty print:

```python
import pprint

data = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'US',
        'zip': '12345'
    },
    'interests': ['reading', 'hiking', 'coding']
}

# Use the default pretty print settings
pprint.pprint(data)

# Define a custom pretty print setting with indentation and max width
pprint.PrettyPrinter(indent=4, width=50).pprint(data)
```

Output:

```python    {'age': 30, 
     'address': {'city': 'Anytown', 
                  'state': 'US', 
                  'street': '123 Main St', 
                  'zip': '12345'}, 
     'interests': ['reading', 'hiking', 'coding'], 
     'name': 'John Doe'}
```

```python
    {'age': 30, 
     'address': {
       'city': 'Anytown', 
       'state': 'US', 
       'street': '123 Main St', 
       'zip': '12345'
      }, 
     'interests': ['reading', 'hiking', 'coding'], 
     'name': 'John Doe'}
```

Note that the `width` parameter controls the maximum width of each line in the pretty print, and the `indent` parameter controls the indentation level.
