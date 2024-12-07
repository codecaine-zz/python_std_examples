# html.entities - Definitions of HTML general entities

The `html.entities` module provides a comprehensive dictionary mapping HTML numeric character references to their corresponding characters. These entities are used in HTML documents to represent special characters that cannot be directly included due to formatting issues or restrictions. Below are several examples demonstrating how to use the `html.entities` module, including reading from and writing to entity files, converting between numeric and named entities, and using them in HTML strings.

### Example 1: Reading Entity Definitions

```python
import html.entities as ent

# Access all available HTML character entities as a dictionary
entity_dict = ent.entitydefs

# Print the first few key-value pairs from the entity dictionary
for name, code in list(entity_dict.items())[:5]:
    print(f"{name}: {code}")
```

### Example 2: Writing Entity Definitions to a File

```python
import html.entities as ent
import os

# Define the path where you want to save the entity definitions
output_file = "entity_definitions.txt"

# Create a list of all entities and their corresponding numeric values
entities = [(name, code) for name, code in ent.entitydefs.items()]

# Write the entities to a file
with open(output_file, "w") as file:
    for name, code in entities:
        file.write(f"{name}: {code}\n")

print(f"Entity definitions have been written to {output_file}")
```

### Example 3: Converting Between Numeric and Named Entities

```python
import html.entities as ent

# Convert a named entity to its numeric equivalent
named_entity = "gt"
numeric_value = ent.name2codepoint[named_entity]
print(f"The numeric value for '{named_entity}' is {numeric_value}")

# Convert a numeric entity back to its named equivalent
numeric_entity = 62
named_entity = ent.codepoint2name[numeric_entity]
print(f"The named entity for {numeric_entity} is '{named_entity}'")
```

### Example 4: Using Entities in HTML Strings

```python
import html
import html.entities as ent

# Define a string with special characters that can be represented by entities
html_string = "<div>This is an example of using HTML entities.</div>"

# Replace special characters with their corresponding named entities
escaped_html_string = html.escape(html_string)
print("Original HTML String:", html_string)
print("Escaped HTML String:", escaped_html_string)

# Convert back to the original string
unescaped_html_string = html.unescape(escaped_html_string)
print("Unescaped HTML String:", unescaped_html_string)
```

### Example 5: Handling Non-ASCII Characters

```python
import html.entities as ent

# Define a string with non-ASCII characters
non_ascii_string = "Hello, world! 😊"

# Convert non-ASCII characters to their corresponding named entities
non_ascii_entities = {char: f"&#x{ord(char):04X};" for char in non_ascii_string if ord(char) > 127}

# Print the original string and its entity replacements
print("Original String:", non_ascii_string)
for char, entity in non_ascii_entities.items():
    print(f"{char}: {entity}")
```

### Example 6: Using Entities with HTML Libraries

If you are using an HTML library like `BeautifulSoup` or `lxml`, the `html.entities` module can be used to handle character entities in parsed content.

```python
from bs4 import BeautifulSoup
from html import entities as ent

# Define a string with HTML containing special characters
html_content = "<div>This is a <span>sample</span> of HTML content with special characters: &gt; &lt;</div>"

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Print the parsed content and its entities
print("Original HTML Content:", html_content)
print("Parsed HTML Content:", str(soup))

# Use the entity dictionary to manually replace named entities if necessary
for text_node in soup.find_all(text=True):
    new_text = text_node
    for name, code in ent.html5.items():
        new_text = new_text.replace(name, f"&#{code};")
    text_node.replace_with(new_text)

print("Parsed HTML Content with Entities Replaced:", str(soup))
```

Note: To use `BeautifulSoup`, you need to install the `beautifulsoup4` package using pip:

```sh
pip install beautifulsoup4
```

These examples cover a variety of scenarios involving the `html.entities` module, from basic entity handling to more advanced uses in web development and data processing.
