# xml.sax.handler — Base classes for SAX handlers

**XmlSaxHandler Example Code**
=====================================

The `xml.sax.handler` module provides base classes for creating custom SAX (Simple API for XML) handlers.

```python
import xml.sax

# Define a basic handler class
class BasicHandler(xml.sax.ContentHandler):
    """
    A simple handler that prints the parsed XML content.
    """

    def __init__(self):
        self.content = []

    def startElement(self, name, attrs):
        """
        Called when an element starts.

        Args:
            name (str): The element name.
            attrs (xml.sax.xmlAttributes): Attributes of the element.
        """
        print(f"Start Element: {name}")
        self.content.append(name)

    def endElement(self, name):
        """
        Called when an element ends.

        Args:
            name (str): The element name.
        """
        print(f"End Element: {name}")

# Define a handler class that handles start and end tags
class TagHandler(xml.sax.ContentHandler):
    """
    A handler that handles both start and end tags of elements.
    """

    def __init__(self):
        super().__init__()
        self.content = []

    def startElement(self, name, attrs):
        """
        Called when an element starts.

        Args:
            name (str): The element name.
            attrs (xml.sax.xmlAttributes): Attributes of the element.
        """
        print(f"Start Element: {name}")
        self.content.append(name)

    def endElement(self, name):
        """
        Called when an element ends.

        Args:
            name (str): The element name.
        """
        print(f"End Element: {name}")

# Define a handler class that handles specific tags
class SpecificTagHandler(xml.sax.DTDHandler, xml.sax.ContentHandler):
    """
    A handler that handles specific tags and ignores others.
    """

    def __init__(self):
        super().__init__()
        self.dtd = {
            "tag": ["tag1", "tag2"],
            "content": ["content1", "content2"]
        }

    def startElement(self, name, attrs):
        """
        Called when an element starts.

        Args:
            name (str): The element name.
            attrs (xml.sax.xmlAttributes): Attributes of the element.

        Returns:
            bool: True if the element is one of the specific tags, False otherwise.
        """
        return name in self.dtd["tag"]

    def endElement(self, name):
        """
        Called when an element ends.

        Args:
            name (str): The element name.

        Returns:
            bool: True if the element is one of the specific tags, False otherwise.
        """
        return name in self.dtd["content"]

# Define a main function to test the handlers
def main():
    # Create an XML string
    xml_string = "<root><tag1>content1</tag1><tag2>content2</tag2></root>"

    # Parse the XML string using the BasicHandler
    handler = BasicHandler()
    sax.parse(xml_string, handler)

    # Print the parsed content
    print("Parsed Content:", handler.content)

if __name__ == "__main__":
    main()

```

**Explanation**

*   We define three types of handlers:
    *   `BasicHandler`: A simple handler that prints the parsed XML content.
    *   `TagHandler`: A handler that handles both start and end tags of elements.
    *   `SpecificTagHandler`: A handler that handles specific tags and ignores others.
*   Each handler class has an `__init__` method to initialize the content, and methods for handling start and end elements (`startElement`, `endElement`).
*   The `specific_tag_handler` uses a dictionary to store the specific tags and their corresponding content. It returns True if the element is one of the specific tags, False otherwise.
*   In the `main` function, we create an XML string and parse it using each handler class.

**Example Use Cases**

*   Creating custom SAX handlers for parsing XML files or streams.
*   Handling specific XML tags or elements in a parser.
*   Integrating with other libraries that use SAX to handle XML parsing.
