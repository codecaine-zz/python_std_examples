# xml.dom - The Document Object Model API

The `xml.dom` module is part of Python's standard library and provides a convenient way to work with XML documents using the DOM (Document Object Model) approach. This module allows you to create, manipulate, and parse XML data in a structured object-oriented manner.

Below are comprehensive examples for each functionality available in the `xml.dom` module:

### 1. Creating an XML Document

```python
import xml.dom.minidom

# Create a new DOM document
doc = xml.dom.minidom.Document()

# Create root element
root = doc.createElement("Root")
doc.appendChild(root)

# Create child elements and add them to the root
child1 = doc.createElement("Child1")
child1.setAttribute("name", "Item1")
child2 = doc.createElement("Child2")
child2.setAttribute("value", "Value2")

root.appendChild(child1)
root.appendChild(child2)

# Print the XML string representation of the document
xml_str = doc.toprettyxml(indent="  ")
print(xml_str)
```

### 2. Parsing an XML String

```python
import xml.dom.minidom

# Define an XML string
xml_string = """
<Root>
    <Child1 name="Item1">
        <Subchild>Content</Subchild>
    </Child1>
    <Child2 value="Value2"/>
</Root>
"""

# Parse the XML string
dom_doc = xml.dom.minidom.parseString(xml_string)

# Access elements by tag name
root_element = dom_doc.documentElement
child_elements = root_element.getElementsByTagName("Child1")

for child in child_elements:
    print(child.getAttribute("name"), child.firstChild.data)
```

### 3. Creating an XML Element and Attribute

```python
import xml.dom.minidom

# Create a new DOM document
doc = xml.dom.minidom.Document()

# Create a root element
root = doc.createElement("Root")
doc.appendChild(root)

# Create a child element with an attribute
child_element = doc.createElement("ChildElement")
child_element.setAttribute("attr", "attributeValue")

# Add the child to the root
root.appendChild(child_element)

# Print the XML string representation of the document
xml_str = doc.toprettyxml(indent="  ")
print(xml_str)
```

### 4. Iterating Over Elements and Attributes

```python
import xml.dom.minidom

# Define an XML string
xml_string = """
<Root>
    <Child1 name="Item1">
        <Subchild>Content</Subchild>
    </Child1>
    <Child2 value="Value2"/>
</Root>
"""

# Parse the XML string
dom_doc = xml.dom.minidom.parseString(xml_string)

# Access elements and attributes by tag name
root_element = dom_doc.documentElement

# Iterate over child elements and print their attributes
child_elements = root_element.getElementsByTagName("Child1")
for child in child_elements:
    for attr_name, attr_value in child.attributes.items():
        print(f"Attribute: {attr_name}, Value: {attr_value}")

# Iterate over child elements and print their text content
for child in child_elements:
    print(child.firstChild.data)
```

### 5. Writing XML to a File

```python
import xml.dom.minidom

# Create a new DOM document
doc = xml.dom.minidom.Document()

# Create root element
root = doc.createElement("Root")
doc.appendChild(root)

# Create child elements and add them to the root
child1 = doc.createElement("Child1")
child1.setAttribute("name", "Item1")
child2 = doc.createElement("Child2")
child2.setAttribute("value", "Value2")

root.appendChild(child1)
root.appendChild(child2)

# Write the XML document to a file
with open("output.xml", "w") as file:
    file.write(doc.toprettyxml(indent="  "))
```

### 6. Handling Namespaces

```python
import xml.dom.minidom

# Define an XML string with namespaces
xml_string = """
<ns1:Root xmlns:ns1="http://www.example.com/ns1">
    <ns1:Child1 name="Item1"/>
    <ns2:Child2 value="Value2" xmlns:ns2="http://www.example.com/ns2"/>
</ns1:Root>
"""

# Parse the XML string
dom_doc = xml.dom.minidom.parseString(xml_string)

# Access elements by namespace
root_element = dom_doc.documentElement
child_elements = root_element.getElementsByTagNameNS("http://www.example.com/ns1", "Child1")

for child in child_elements:
    print(child.getAttribute("name"))

# Access elements by another namespace
child_elements = root_element.getElementsByTagNameNS("http://www.example.com/ns2", "Child2")
for child in child_elements:
    print(child.getAttribute("value"))
```

### 7. Creating a DOM Element from Scratch

```python
import xml.dom.minidom

# Create a new DOM document
doc = xml.dom.minidom.Document()

# Create root element with namespace
root = doc.createElementNS("http://www.example.com/ns1", "ns1:Root")
doc.appendChild(root)

# Create child elements and add them to the root
child1 = doc.createElementNS("http://www.example.com/ns2", "ns2:Child1")
child1.setAttributeNS("http://www.example.com/ns1", "attr", "attributeValue")

root.appendChild(child1)

# Print the XML string representation of the document
xml_str = doc.toprettyxml(indent="  ")
print(xml_str)
```

### 8. Copying and Modifying Nodes

```python
import xml.dom.minidom

# Define an XML string
xml_string = """
<Root>
    <Child1 name="Item1">
        <Subchild>Content</Subchild>
    </Child1>
    <Child2 value="Value2"/>
</Root>
"""

# Parse the XML string
dom_doc = xml.dom.minidom.parseString(xml_string)

# Copy a node and modify its text content
root_element = dom_doc.documentElement
child1 = root_element.getElementsByTagName("Child1")[0]
new_child1 = child1.cloneNode(deep=True)
new_subchild = doc.createElement("Subchild")
new_subchild.appendChild(doc.createTextNode("Modified Content"))
new_child1.replaceChild(new_subchild, child1.firstChild)

# Print the modified XML string representation of the document
xml_str = doc.toprettyxml(indent="  ")
print(xml_str)
```

These examples demonstrate various functionalities available in the `xml.dom` module, including creating and parsing XML documents, handling elements and attributes, working with namespaces, and copying and modifying nodes. Each example is well-documented to help you understand how to use each feature effectively.
