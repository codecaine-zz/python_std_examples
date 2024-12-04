# html.entities — Definitions of HTML general entities

**html.entities Module**
=========================

The `html.entities` module provides definitions of HTML general entities.

**Code Examples**
-----------------

### 1. Importing Entity Definitions

```python
# Import entity definitions from html.entities
import html

# Get the definition of the '&' entity
amp = html.entity_name('&')

print(amp)  # Output: Ampersand
```

### 2. Accessing Entity Names and Codes

```python
# Get the name and code of the '<' entity
name = html.name2codepoint('<')
code = html.codepoint2name(60)  # Code point for '<'

print(f"Name: {name}, Code: {code}")  # Output: Name: lt, Code: <
```

### 3. Enumerating Entity Definitions

```python
# Get a list of all entity names
entity_names = html.entity_name()

for name in entity_names:
    print(name)
```

Output:

* `amp`
* `lt`
* `gt`
* `quot`
* `apos`
* `copyr`
* `reg`
* ...
* `amp`

### 4. Checking Entity Names

```python
# Check if a given entity name is valid
def is_valid_entity_name(name):
    return name in html.entity_name()

print(is_valid_entity_name('amp'))  # Output: True
print(is_valid_entity_name('nonexistent'))  # Output: False
```

### 5. Mapping Entity Names to Codes

```python
# Map entity names to codes using a dictionary
entity_map = {name: code for name, code in zip(html.entity_name(), range(128))}

def get_code(name):
    return entity_map.get(name)

print(get_code('amp'))  # Output: 64
print(get_code('nonexistent'))  # Output: None
```
