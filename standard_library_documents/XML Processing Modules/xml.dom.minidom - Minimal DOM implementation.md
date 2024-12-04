# xml.dom.minidom — Minimal DOM implementation

**Minimal DOM Implementation using xml.dom.minidom**
=====================================================

The `xml.dom.minidom` module provides a minimal implementation of the Document Object Model (DOM) for parsing and manipulating XML documents.

### Importing the Module

```python
import xml.dom.minidom as minidom
```

### Parsing an XML String

You can parse an XML string using the `parseString()` method:

```python
xml_string = """
<person>
    <name>John Doe</name>
    <age>30</age>
    <city>New York</city>
</person>
"""

# Create a Document object from the XML string
doc = minidom.parseString(xml_string)

# Get the root element
root = doc.documentElement

# Print the tag name and text content of each child element
for child in root.childNodes:
    if isinstance(child, minidom.Node):
        print(f"Tag: {child.tagName}, Text: {child.textContent}")
```

### Parsing an XML File

You can parse an XML file using the `parse()` method:

```python
xml_file = "example.xml"

# Create a Document object from the XML file
doc = minidom.parse(xml_file)

# Get the root element
root = doc.documentElement

# Print the tag name and text content of each child element
for child in root.childNodes:
    if isinstance(child, minidom.Node):
        print(f"Tag: {child.tagName}, Text: {child.textContent}")
```

### Creating a New Document Object

You can create a new `Document` object using the `Document()` constructor:

```python
# Create a new Document object
doc = minidom.Document()

# Append a child element to the root node
root = doc.createElement("person")
root.appendChild(doc.createTextNode("John Doe"))
doc.appendChild(root)
```

### Manipulating XML Documents

You can manipulate the structure and content of an XML document by creating, moving, copying, or deleting elements:

```python
import xml.dom.minidom as minidom

# Create a new Document object
doc = minidom.Document()

# Append child elements to the root node
root = doc.createElement("person")
root.appendChild(doc.createTextNode("John Doe"))
doc.appendChild(root)
root = doc.createElement("age")
root.appendChild(doc.createTextNode("30"))
doc.appendChild(root)

# Move an element from one parent to another
child_node = doc.getElementsByTagName("name")[0]
parent_node = child_node.parentNode
parent_node.removeChild(child_node)
parent_node.appendChild(child_node)

# Copy a node using the cloneNode() method
 cloned_node = root.cloneNode(True)

# Append the cloned node to a new parent node
new_root = doc.createElement("address")
doc.appendChild(new_root)
new_root.appendChild(cloned_node)

# Delete an element from the document
doc.removeChild(root)

# Print the updated XML string
xml_string = minidom.tostring(doc, encoding="unicode")
print(xml_string)
```

### Conclusion

The `xml.dom.minidom` module provides a powerful and flexible way to parse, manipulate, and generate XML documents in Python. Its simplicity and ease of use make it an ideal choice for tasks that require minimal DOM functionality.
