# xml.dom.minidom - Minimal DOM implementation

Certainly! Below is a comprehensive list of code examples demonstrating various functionalities of the `xml.dom.minidom` module, which provides a simple and efficient API for parsing XML documents and creating new ones. Each example includes comments to explain each step.

### 1. Parsing an XML Document

```python
import xml.dom.minidom as minidom

# Load an XML document from a file
doc = minidom.parse('example.xml')

# Accessing elements
root_element = doc.documentElement
print("Root Element:", root_element.tagName)

# Getting child nodes
child_nodes = root_element.childNodes
for node in child_nodes:
    if node.nodeType == node.ELEMENT_NODE:
        print("Child Node:", node.tagName)

# Printing the XML string representation
xml_string = doc.toprettyxml(indent="  ")
print(xml_string)
```

### 2. Creating a New XML Document

```python
import xml.dom.minidom as minidom

# Create a new document object
doc = minidom.Document()

# Adding an element to the document
root = doc.createElement('root')
doc.appendChild(root)

# Creating child elements and adding them to the root
child1 = doc.createElement('child1')
child2 = doc.createElement('child2')

text_node = doc.createTextNode("Hello, World!")
child1.appendChild(text_node)
root.appendChild(child1)
root.appendChild(child2)

# Printing the XML string representation
xml_string = doc.toprettyxml(indent="  ")
print(xml_string)
```

### 3. Modifying an Existing XML Document

```python
import xml.dom.minidom as minidom

# Load an existing XML document
doc = minidom.parse('example.xml')

# Accessing elements and modifying their content
root_element = doc.documentElement
child_elements = root_element.getElementsByTagName('child1')
for child in child_elements:
    text_node = child.firstChild
    text_node.data = "Updated Content"

# Printing the updated XML string representation
xml_string = doc.toprettyxml(indent="  ")
print(xml_string)
```

### 4. Writing to a File

```python
import xml.dom.minidom as minidom

# Create a new document object
doc = minidom.Document()

# Adding elements to the document and saving it to a file
root = doc.createElement('root')
doc.appendChild(root)

child1 = doc.createElement('child1')
text_node = doc.createTextNode("Hello, World!")
child1.appendChild(text_node)
root.appendChild(child1)

with open('output.xml', 'w') as file:
    file.write(doc.toprettyxml(indent="  "))

print("XML saved to output.xml")
```

### 5. Searching for Elements

```python
import xml.dom.minidom as minidom

# Load an XML document
doc = minidom.parse('example.xml')

# Searching for elements by tag name
child_elements = doc.getElementsByTagName('child2')
for child in child_elements:
    print("Found:", child.tagName)

# Searching for elements by attribute
attribute_elements = doc.getElementsByTagName('child1')
for child in attribute_elements:
    if child.getAttributeNode('type'):
        print("Found with attribute:", child.tagName)
```

### 6. Handling Namespaces

```python
import xml.dom.minidom as minidom

# Load an XML document with namespaces
doc = minidom.parse('example_ns.xml')

# Accessing elements with namespaces
ns_map = {'ns': 'http://example.com/ns'}
root_element = doc.documentElement
child_elements = root_element.getElementsByTagNameNS(ns_map['ns'], 'child1')
for child in child_elements:
    print("Found with namespace:", child.tagName)
```

### 7. Traversing the DOM Tree

```python
import xml.dom.minidom as minidom

# Load an XML document
doc = minidom.parse('example.xml')

# Iterating over all elements in the tree
for elem in doc.getElementsByTagName('*'):
    print("Element:", elem.tagName)
```

### 8. Using XPath for Querying

```python
import xml.dom.minidom as minidom

# Load an XML document
doc = minidom.parse('example.xml')

# Using XPath to query elements
xpath_result = doc.evaluate('/root/child1', doc, None, minidom.XPathConstants.NODESET)
for node in xpath_result:
    print("XPath Result:", node.tagName)
```

These examples cover a range of functionalities provided by the `xml.dom.minidom` module, from parsing and creating XML documents to modifying them, saving them to files, searching for elements, handling namespaces, traversing the DOM tree, and using XPath. Each example is designed to be clear and self-contained, with comments explaining each step.
