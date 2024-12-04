# xml.dom.pulldom — Support for building partial DOM trees

**Module: `xml.dom.pulldom`**

The `xml.dom.pulldom` module provides support for building partial DOM (Document Object Model) trees. This module is designed to be used in conjunction with the `xml.dom.minidom` module, which provides a way to parse and manipulate XML documents.

**Code Examples:**
```python
import xml.dom.pulldom

# Create an empty document object
doc = xml.dom.pulldom.Document()

# Append some elements to the document
doc.appendChild(doc.createElement("root"))
doc.documentElement.appendChild(doc.createElement("child1"))
doc.documentElement.appendChild(doc.createElement("child2"))

# Get the first child element of the root element
child1 = doc.getDocumentElement().firstChild
print(child1.nodeValue)  # Output: ""

# Append a text node to the document
doc.createTextNode("Hello, World!").appendChild(doc)

# Create a new document object and start building it from scratch
new_doc = xml.dom.pulldom.Document()
new_element = new_doc.createElement("grandchild")
new_element.appendChild(new_doc.createTextNode("This is a grandchild"))
new_doc.documentElement.appendChild(new_element)

# Convert the partial DOM tree to a string
xml_string = doc.toprettyxml(indent="  ")
print(xml_string)
# Output:
# <?xml version="1.0" ?>
# <root>
#   <child1 />
#   <child2 />
#   Hello, World!
# </root>

# Use an iterator to iterate over the elements in the document
for elem in doc.iterElements():
    print(elem.tagName, elem.nodeValue)

# Get the parent element of a given element
parent = new_doc.getElementsByTagName("grandchild")[0].parentNode
print(parent.tagName)  # Output: "root"
```
**Explanation of Key Functions and Methods:**

*   `xml.dom.pulldom.Document()`: Creates an empty document object.
*   `doc.createElement(elementName)`: Creates a new element with the specified name and appends it to the current document.
*   `doc.appendChild(child)` : Appends the specified child element or text node to the end of the current document.
*   `doc.toprettyxml(indent="  ")`: Converts the partial DOM tree to a string, formatting it for human readability.
*   `iterElements()`: An iterator that yields the elements in the document in reverse topological order.
*   `getElementsByTagName(elementName)`: Returns a list of elements with the specified name in the current document.

**Tips and Tricks:**

*   The `pulldom` module is designed to be more memory-efficient than other DOM parsing libraries, making it suitable for large XML documents.
*   You can use the `iterElements()` iterator to iterate over the elements in a document without loading the entire document into memory.
*   The `toprettyxml()` method provides a convenient way to convert a partial DOM tree to a formatted string.
