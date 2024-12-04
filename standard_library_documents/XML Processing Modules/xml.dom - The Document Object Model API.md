# xml.dom — The Document Object Model API

**Xml Dom Module Code Examples**
=====================================

The `xml.dom` module provides an interface for parsing and manipulating XML documents.

### 1. Parsing an XML File

```python
import xml.dom.minidom as minidom

def parse_xml_file(file_path):
    """
    Parse an XML file and return the parsed document.
    
    Args:
        file_path (str): The path to the XML file.
    
    Returns:
        str: The parsed XML document as a string.
    """
    # Create a new DOMParser object
    parser = minidom.Parser()
    
    # Parse the XML file using the Parser object
    doc = parser.parse(file_path)
    
    # Return the parsed document as a string
    return doc.toprettyxml()

# Example usage:
file_path = 'example.xml'
parsed_doc = parse_xml_file(file_path)
print(parsed_doc)
```

### 2. Creating an XML Document

```python
import xml.dom.minidom as minidom

def create_xml_document():
    """
    Create a new XML document using the DOM API.
    
    Returns:
        str: The created XML document as a string.
    """
    # Create a new DOMDocument object
    doc = minidom.Document()
    
    # Create an element node
    elem = doc.createElement('root')
    
    # Add some text content to the element node
    elem.textContent = 'Hello, World!'
    
    # Append the element node to the document
    doc.appendChild(elem)
    
    # Return the created XML document as a string
    return doc.toprettyxml()

# Example usage:
created_doc = create_xml_document()
print(created_doc)
```

### 3. Querying an XML Document

```python
import xml.dom.minidom as minidom

def query_xml_document(doc, xpath_expr):
    """
    Query an XML document using the XPath expression.
    
    Args:
        doc (str): The parsed XML document as a string.
        xpath_expr (str): The XPath expression to query the document with.
    
    Returns:
        list: A list of element nodes that match the XPath expression.
    """
    # Create a new DOMParser object
    parser = minidom.Parser()
    
    # Parse the XML document using the Parser object
    parsed_doc = parser.parseString(doc)
    
    # Use the XPath expression to query the document
    nodes = parsed_doc.getElementsByTagName(xpath_expr)
    
    # Return the matching element nodes as a list
    return [node.childNodes[0].nodeValue for node in nodes]

# Example usage:
file_path = 'example.xml'
parsed_doc = parse_xml_file(file_path)

xpath_expr = '//title'
query_results = query_xml_document(parsed_doc, xpath_expr)
print(query_results)
```

### 4. Modifying an XML Document

```python
import xml.dom.minidom as minidom

def modify_xml_document(doc, xpath_expr, new_text):
    """
    Modify an XML document by replacing the text content of a node.
    
    Args:
        doc (str): The parsed XML document as a string.
        xpath_expr (str): The XPath expression to query the document with.
        new_text (str): The new text content for the node.
    
    Returns:
        str: The modified XML document as a string.
    """
    # Create a new DOMParser object
    parser = minidom.Parser()
    
    # Parse the XML document using the Parser object
    parsed_doc = parser.parseString(doc)
    
    # Use the XPath expression to query the document
    nodes = parsed_doc.getElementsByTagName(xpath_expr)
    
    # Replace the text content of the first node with the new text
    if nodes:
        nodes[0].textContent = new_text
    
    # Return the modified XML document as a string
    return parsed_doc.toprettyxml()

# Example usage:
file_path = 'example.xml'
parsed_doc = parse_xml_file(file_path)

xpath_expr = '//title'
new_text = 'My Modified Title'
modified_doc = modify_xml_document(parsed_doc, xpath_expr, new_text)
print(modified_doc)
```

### 5. Saving an XML Document to a File

```python
import xml.dom.minidom as minidom

def save_xml_document(doc, file_path):
    """
    Save an XML document to a file using the DOM API.
    
    Args:
        doc (str): The parsed XML document as a string.
        file_path (str): The path to the output file.
    
    Returns:
        None
    """
    # Create a new DOMDocument object
    doc = minidom.Document()
    
    # Append the original document content to the new document
    doc.appendChild(doc.createTextNode(doc))
    
    # Save the modified document to a file using the DOMWriter
    with open(file_path, 'w') as f:
        doc.save(f)

# Example usage:
file_path = 'output.xml'
save_xml_document(parsed_doc, file_path)
```
