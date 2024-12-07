# json - JSON encoder and decoder

Below are comprehensive code examples for various functionalities of the `json` module in Python, along with detailed comments explaining each step.

```python
# Importing the json module
import json

# Example 1: Encoding a simple dictionary to JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Using json.dumps() to convert the dictionary to a JSON string
json_data = json.dumps(data)
print("Encoded JSON:", json_data)

# Example 2: Encoding a Python object (list) to JSON
data_list = ["apple", "banana", "cherry"]
json_list = json.dumps(data_list)
print("Encoded list as JSON:", json_list)

# Example 3: Decoding a JSON string back to a dictionary
json_encoded_string = '{"name": "John", "age": 30, "city": "New York"}'
decoded_data = json.loads(json_encoded_string)
print("Decoded data from JSON:", decoded_data)

# Example 4: Encoding with specific indentation for readability
data_with_indentation = {
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}
json_with_indent = json.dumps(data_with_indentation, indent=4)
print("Encoded data with indentation:", json_with_indent)

# Example 5: Encoding to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
print("Data written to data.json")

# Example 6: Decoding from a file
with open('data.json', 'r') as file:
    decoded_data_from_file = json.load(file)
print("Decoded data from data.json:", decoded_data_from_file)

# Example 7: Handling JSON with special characters (ensure correct encoding)
special_characters_data = {"name": "John Doe", "address": "123 Main St, New York, USA"}
json_special_chars = json.dumps(special_characters_data)
print("Encoded data with special characters:", json_special_chars)

# Example 8: Encoding to a file in binary mode
with open('binary_data.json', 'wb') as file:
    file.write(json.dumps(data).encode('utf-8'))
print("Binary data written to binary_data.json")

# Example 9: Decoding from a file in binary mode
with open('binary_data.json', 'rb') as file:
    decoded_binary_data = json.loads(file.read().decode('utf-8'))
print("Decoded binary data:", decoded_binary_data)

# Example 10: Handling errors during encoding or decoding
try:
    # Attempt to encode a non-serializable object
    json.dumps([{"name": "John", "age": 30}, None, {"nested": [1, 2, 3]}])
except TypeError as e:
    print("Error:", e)

# Example 11: Encoding with custom serialization (if needed)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_to_dict(person):
    return {"name": person.name, "age": person.age}

person = Person("Jane", 25)
json_person = json.dumps(person, default=person_to_dict)
print("Encoded custom object:", json_person)

# Example 12: Handling errors during encoding with custom serialization
class InvalidPerson:
    def __init__(self, name):
        self.name = name

try:
    # Attempt to encode an invalid custom object
    json.dumps([{"name": "John", "age": 30}, InvalidPerson("Jane")])
except TypeError as e:
    print("Error:", e)
```

### Explanation:

1. **Encoding and Decoding**:
   - `json.dumps()` converts a Python dictionary or list to a JSON string.
   - `json.loads()` parses a JSON string back into a Python object (dictionary, list).

2. **Indentation for Readability**:
   - The `indent` parameter in `json.dumps()` can be used to format the output with indentation for better readability.

3. **Encoding to and Decoding from Files**:
   - Use `open()` to write to or read from files.
   - `json.dump()` writes a Python object to a file.
   - `json.load()` reads a JSON formatted file and converts it back into a Python object.

4. **Special Characters and Encoding**:
   - Ensure that special characters are properly encoded by using the correct encoding when writing to or reading from files.

5. **Binary Mode**:
   - Use binary mode (`'wb'` for writing and `'rb'` for reading) when dealing with binary data.

6. **Error Handling**:
   - Catch `TypeError` exceptions when attempting to encode non-serializable objects.
   - Implement custom serialization functions to handle complex objects or types that are not natively serializable by Python's default JSON encoder.

7. **Custom Serialization**:
   - Define a function to convert custom objects into a format that can be serialized by the `json` module.

These examples cover various aspects of the `json` module, providing a comprehensive guide for using it in different scenarios.
