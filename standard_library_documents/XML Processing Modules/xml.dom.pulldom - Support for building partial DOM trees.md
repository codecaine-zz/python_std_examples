# xml.dom.pulldom - Support for building partial DOM trees

The `xml.dom.pulldom` module in Python provides a way to parse XML documents without creating a full DOM tree in memory. This is particularly useful when dealing with large XML files or when you only need to access specific parts of the document. Below are comprehensive examples demonstrating various functionalities of the `xml.dom.pulldom` module.

### Example 1: Basic Usage of pulldom

```python
from xml.dom import pulldom

# Create a parser
parser = pulldom.make_parser()

# Define handlers for different events
handler = pulldom.ContentHandler()
handler.startElement = lambda name, attrs: print(f"Start Element: {name}, Attributes: {attrs}")
handler.endElement   = lambda name: print(f"End Element: {name}")

# Parse an XML file
with open('example.xml', 'r') as file:
    for event, node in parser.parse(file):
        handler.handleEvent(event, node)

# Clear the parser after parsing to avoid memory leaks
parser.clear()
```

### Example 2: Parsing Multiple Nodes

```python
from xml.dom import pulldom

# Create a parser
parser = pulldom.make_parser()

# Define handlers for different events
handler = pulldom.ContentHandler()
handler.startElement = lambda name, attrs: print(f"Start Element: {name}, Attributes: {attrs}")
handler.endElement   = lambda name: print(f"End Element: {name}")

# Parse an XML file
with open('example.xml', 'r') as file:
    for event, node in parser.parse(file):
        handler.handleEvent(event, node)

# Clear the parser after parsing to avoid memory leaks
parser.clear()
```

### Example 3: Using a Callback Function

```python
from xml.dom import pulldom

def handle_event(event, node):
    if event == pulldom.START_ELEMENT:
        print(f"Start Element: {node.nodeName}, Attributes: {node.attributes}")
    elif event == pulldom.END_ELEMENT:
        print(f"End Element: {node.nodeName}")

# Create a parser
parser = pulldom.make_parser()

# Parse an XML file
with open('example.xml', 'r') as file:
    for event, node in parser.parse(file):
        handle_event(event, node)

# Clear the parser after parsing to avoid memory leaks
parser.clear()
```

### Example 4: Parsing with Namespaces

```python
from xml.dom import pulldom

def handle_event(event, node):
    if event == pulldom.START_ELEMENT:
        print(f"Start Element: {node.nodeName}, Attributes: {node.attributes}")
        for name, value in node.getNamespaceMap().items():
            print(f"Namespace: {name} -> {value}")
    elif event == pulldom.END_ELEMENT:
        print(f"End Element: {node.nodeName}")

# Create a parser
parser = pulldom.make_parser()

# Parse an XML file with namespaces
with open('example.xml', 'r') as file:
    for event, node in parser.parse(file):
        handle_event(event, node)

# Clear the parser after parsing to avoid memory leaks
parser.clear()
```

### Example 5: Parsing and Accessing Attributes

```python
from xml.dom import pulldom

def handle_event(event, node):
    if event == pulldom.START_ELEMENT:
        attributes = {attr.nodeName: attr.nodeValue for attr in node.attributes}
        print(f"Start Element: {node.nodeName}, Attributes: {attributes}")
    elif event == pulldom.END_ELEMENT:
        print(f"End Element: {node.nodeName}")

# Create a parser
parser = pulldom.make_parser()

# Parse an XML file
with open('example.xml', 'r') as file:
    for event, node in parser.parse(file):
        handle_event(event, node)

# Clear the parser after parsing to avoid memory leaks
parser.clear()
```

### Example 6: Parsing with Namespaces and Attributes

```python
from xml.dom import pulldom

def handle_event(event, node):
    if event == pulldom.START_ELEMENT:
        attributes = {attr.nodeName: attr.nodeValue for attr in node.attributes}
        print(f"Start Element: {node.nodeName}, Attributes: {attributes}")
        for name, value in node.getNamespaceMap().items():
            print(f"Namespace: {name} -> {value}")
    elif event == pulldom.END_ELEMENT:
        print(f"End Element: {node.nodeName}")

# Create a parser
parser = pulldom.make_parser()

# Parse an XML file with namespaces and attributes
with open('example.xml', 'r') as file:
    for event, node in parser.parse(file):
        handle_event(event, node)

# Clear the parser after parsing to avoid memory leaks
parser.clear()
```

These examples demonstrate various ways to use the `xml.dom.pulldom` module to parse XML documents and handle events such as start and end elements. Each example includes comments explaining the purpose of each part of the code, making it easy for readers to understand and modify as needed.
