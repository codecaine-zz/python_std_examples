# xml.etree.ElementTree — The ElementTree XML API

**XML Parsing and Manipulation using xml.etree.ElementTree**

The `xml.etree.ElementTree` module is a built-in Python module for parsing and manipulating XML documents.

### Importing the Module
```python
import xml.etree.ElementTree as ET
```

### Creating an XML Document
```python
# Create an empty XML document
root = ET.Element("root")

# Add child elements to the root element
child1 = ET.SubElement(root, "child1")
child2 = ET.SubElement(root, "child2")

# Set text content for child elements
child1.text = "Hello, World!"
child2.text = "This is a test."

# Create an XML document string
xml_doc = ET.tostring(root, encoding="unicode")

print(xml_doc)
```

Output:
```xml
<root>
  <child1>Hello, World!</child1>
  <child2>This is a test.</child2>
</root>
```

### Parsing an XML Document
```python
# Load an XML file into an ElementTree object
tree = ET.parse("example.xml")

# Get the root element of the parsed XML document
root = tree.getroot()

# Print the attributes of the root element
print(root.attrib)

# Print the text content of the root element
print(root.text)
```

Assuming `example.xml` contains:
```xml
<root attr="value">
  <child>Hello, World!</child>
</root>
```
Output:
```python
{'attr': 'value'}
Hello, World!
```

### Element Creation and Manipulation
```python
# Create a new element with a specified tag and attributes
person = ET.Element("person", {"name": "John", "age": 30})

# Add child elements to the person element
ET.SubElement(person, "address").text = "123 Main St"
ET.SubElement(person, "phone").text = "555-555-5555"

# Print the ElementTree object as a string
print(ET.tostring(person, encoding="unicode"))
```

Output:
```xml
<person name="John" age="30">
  <address>123 Main St</address>
  <phone>555-555-5555</phone>
</person>
```

### Iterating over XML Elements
```python
# Parse an XML file into an ElementTree object
tree = ET.parse("example.xml")

# Get the root element of the parsed XML document
root = tree.getroot()

# Iterate over child elements of the root element
for child in root:
    # Print the tag and text content of each child element
    print(child.tag, child.text)
```

Assuming `example.xml` contains:
```xml
<root>
  <child1>Hello, World!</child1>
  <child2>This is a test.</child2>
</root>
```
Output:
```
child1 Hello, World!
child2 This is a test.
```

### XML Validation and Dumps
```python
# Create an ElementTree object with invalid XML
invalid_tree = ET.fromstring("<root><child>Hello, World!</child></root>")

try:
    # Attempt to parse the invalid ElementTree object as valid XML
    tree = ET.parse(ET.tostring(invalid_tree, encoding="unicode"))
except ET.ParseError as e:
    print(e)  # Output: Parse error in document

# Create an ElementTree object with valid XML
valid_tree = ET.fromstring("<root><child>Hello, World!</child></root>")

# Print the ElementTree object as a string using dumps
print(ET.tostring(valid_tree, encoding="unicode"))
```

Output:
```xml
Parse error in document
<root><child>Hello, World!</child></root>
```
