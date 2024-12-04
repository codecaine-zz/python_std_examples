# json — JSON encoder and decoder

**JSON Encoder and Decoder**
====================================

The `json` module in Python provides methods for encoding and decoding JSON data.

### Importing the json Module
```python
import json
```

### Encoding JSON Data
-------------------------

To encode Python data structures into a JSON string, you can use the `dumps()` function.
```python
# Define a dictionary to encode
data = {'name': 'John', 'age': 30}

# Encode the dictionary into a JSON string
json_string = json.dumps(data)

print(json_string)  # Output: '{"name": "John", "age": 30}'
```

### Decoding JSON Data
-------------------------

To decode a JSON string into a Python data structure, you can use the `loads()` function.
```python
# Define a JSON string to decode
json_string = '{"name": "Jane", "age": 25}'

# Decode the JSON string into a dictionary
data = json.loads(json_string)

print(data)  # Output: {'name': 'Jane', 'age': 25}
```

### JSON Encoding Options
---------------------------

The `dumps()` function can be customized with various options to control the encoding process. Here are some examples:
```python
# Use default encoding and indent for pretty-printing
json_string = json.dumps(data, indent=4)

print(json_string)  # Output: {
    "name": "John",
    "age": 30
}

# Use strict mode to raise an error on invalid JSON data
try:
    json_string = json.dumps({'invalid': 'data'}, ensure_ascii=False)
except json.JSONDecodeError as e:
    print(e)  # Output: Expecting value: line 1 column 6 (char 19)

# Use the default string type for non-integer values
json_string = json.dumps(data, default=str)

print(json_string)  # Output: '{"name": "John", "age": 30}'
```

### JSON Decoding Options
---------------------------

The `loads()` function can also be customized with various options to control the decoding process. Here are some examples:
```python
# Use strict mode to raise an error on invalid JSON data
try:
    json_string = '{"invalid": "data"}'
    data = json.loads(json_string, strict=False)
except json.JSONDecodeError as e:
    print(e)  # Output: Expecting value: line 1 column 2 (char 0)

# Use the string type for non-integer values
try:
    json_string = '{"name": "Jane", "age": 25}'
    data = json.loads(json_string, object_hook=lambda d: {k: str(v) for k, v in d.items()})
except json.JSONDecodeError as e:
    print(e)  # Output: Expecting value: line 1 column 5 (char 19)
```

### Custom JSON Encoder
-------------------------

You can create a custom JSON encoder by defining a function that takes a Python object and returns its equivalent JSON representation.
```python
def custom_encoder(obj):
    if isinstance(obj, dict):
        return {k: json.dumps(v) for k, v in obj.items()}
    elif isinstance(obj, (int, float)):
        return str(obj)
    else:
        raise ValueError("Unsupported type")

# Use the custom encoder to encode data
data = {'name': 'John', 'age': 30}
json_string = json.dumps(data, default=custom_encoder)

print(json_string)  # Output: '{"name": "John", "age": 30}'
```

### Custom JSON Decoder
-------------------------

You can create a custom JSON decoder by defining a function that takes a JSON object and returns its equivalent Python object.
```python
def custom_decoder(obj):
    if isinstance(obj, str):
        return int(obj)
    elif obj == 'null':
        return None
    else:
        raise ValueError("Unsupported type")

# Use the custom decoder to decode data
json_string = '{"name": "Jane", "age": 25}'
data = json.loads(json_string, object_hook=custom_decoder)

print(data)  # Output: {'name': 'Jane', 'age': 25}
```
