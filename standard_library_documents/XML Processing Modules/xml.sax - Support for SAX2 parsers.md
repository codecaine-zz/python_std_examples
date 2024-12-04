# xml.sax — Support for SAX2 parsers

Here's an example of how you can use `xml.sax` to parse XML data:
```python
# Importing necessary modules
import xml.sax

# Define a class that will handle the XML data
class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.elements = []

    def startElement(self, name, attrs):
        # Print when an element starts
        print(f"Starting element: {name}")
        self.elements.append({"name": name, "attrs": attrs})

    def endElement(self, name):
        # Print when an element ends
        print(f"Ending element: {name}")

    def characters(self, content):
        # This method is called for character data in the XML file
        print("Characters:", content)

# Create a parser object with our custom handler
parser = xml.sax.make_parser()
parser.setContentHandler(MyHandler())

# Parse an XML string
xml_string = """
<catalog>
    <book id="bk101">
        <author>John Smith</author>
        <title>Python Programming</title>
        <genre>Computers</genre>
        <price>39.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>An introduction to programming.</description>
    </book>
    <book id="bk102">
        <author>Jane Doe</author>
        <title>XSLT Programming</title>
        <genre>Computers</genre>
        <price>49.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>A guide to XSLT.</description>
    </book>
</catalog>
"""

# Feed the XML string into the parser
parser.parse(xml_string)
```
This code will print out the elements of the XML file, including their names and attributes. The `characters` method is called for any character data in the XML file.

Here's a more complex example with multiple handlers:
```python
import xml.sax

# Define a class that handles element starts
class StartHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print(f"Starting element: {name}")

# Define a class that handles character data
class CharHandler(xml.sax.ContentHandler):
    def characters(self, content):
        print("Characters:", content)

# Define a class that handles element ends
class EndHandler(xml.sax.DTDHandler):
    def startElement(self, name, attrs):
        print(f"Starting element: {name}")

    def endElement(self, name):
        print(f"Ending element: {name}")

def main():
    # Create a parser object with our custom handlers
    parser = xml.sax.make_parser()
    parser.setContentHandler(StartHandler())
    parser.setDTDHandler(EndHandler())
    parser.setContentLengthHandler(CharHandler())

    # Parse an XML string
    xml_string = """
<catalog>
    <book id="bk101">
        <author>John Smith</author>
        <title>Python Programming</title>
        <genre>Computers</genre>
        <price>39.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>An introduction to programming.</description>
    </book>
    <book id="bk102">
        <author>Jane Doe</author>
        <title>XSLT Programming</title>
        <genre>Computers</genre>
        <price>49.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>A guide to XSLT.</description>
    </book>
</catalog>
"""

    # Feed the XML string into the parser
    parser.parse(xml_string)

if __name__ == "__main__":
    main()
```
This code will print out the elements of the XML file, including their names and attributes. The `EndHandler` is called for every element in the XML file.

Here's an example that uses a custom namespace:
```python
import xml.sax

# Define a class that handles element starts
class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.elements = []

    def startElement(self, name, attrs):
        # Print when an element starts
        print(f"Starting element: {name}")
        for attr in attrs:
            print(f"  Attribute: {attr[0]}={attr[1]}")
        self.elements.append({"name": name, "attrs": attrs})

    def endElement(self, name):
        # Print when an element ends
        print(f"Ending element: {name}")

    def characters(self, content):
        # This method is called for character data in the XML file
        print("Characters:", content)

# Create a parser object with our custom handler and a namespace
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.feature.NS_PREFIXES, True)
parser.setContentHandler(MyHandler())

# Parse an XML string with a custom namespace
xml_string = """
<catalog xmlns="http://example.com/catalog">
    <book id="bk101" title="Python Programming">
        <author>John Smith</author>
        <genre>Computers</genre>
        <price>39.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>An introduction to programming.</description>
    </book>
    <book id="bk102" title="XSLT Programming">
        <author>Jane Doe</author>
        <genre>Computers</genre>
        <price>49.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>A guide to XSLT.</description>
    </book>
</catalog>
"""

# Feed the XML string into the parser
parser.parse(xml_string)
```
This code will print out the elements of the XML file with their names and attributes, taking into account the custom namespace.

Here's an example that uses a DTD:
```python
import xml.sax

# Define a class that handles element starts
class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.elements = []

    def startElement(self, name, attrs):
        # Print when an element starts
        print(f"Starting element: {name}")
        for attr in attrs:
            print(f"  Attribute: {attr[0]}={attr[1]}")

# Create a parser object with our custom handler and a DTD
parser = xml.sax.make_parser()
parser.setDTDParser(xml.sax.DTDParser.parseString("""
<!ELEMENT catalog (book*)>
<!ELEMENT book (author, title, genre, price, publish_date, description)>

<!ELEMENT author (#PCDATA)>
<!ELEMENT title (#PCDATA)>
<!ELEMENT genre (#PCDATA)>
<!ELEMENT price (#PCDATA)>
<!ELEMENT publish_date (#PCDATA)>
<!ELEMENT description (#PCDATA)>
"""))

# Parse an XML string with a DTD
xml_string = """
<catalog>
    <book id="bk101">
        <author>John Smith</author>
        <title>Python Programming</title>
        <genre>Computers</genre>
        <price>39.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>An introduction to programming.</description>
    </book>
    <book id="bk102">
        <author>Jane Doe</author>
        <title>XSLT Programming</title>
        <genre>Computers</genre>
        <price>49.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>A guide to XSLT.</description>
    </book>
</catalog>
"""

# Feed the XML string into the parser
parser.parse(xml_string)
```
This code will print out the elements of the XML file with their names and attributes, taking into account the DTD.

Here's an example that uses a namespace with multiple namespaces:
```python
import xml.sax

# Define a class that handles element starts
class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.elements = []

    def startElement(self, name, attrs):
        # Print when an element starts
        print(f"Starting element: {name}")
        for attr in attrs:
            print(f"  Attribute: {attr[0]}={attr[1]}")

# Create a parser object with our custom handler and multiple namespaces
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.feature.NS_PREFIXES, True)
parser.setContentHandler(MyHandler())

# Parse an XML string with multiple namespaces
xml_string = """
<catalog xmlns:ns="http://example.com/ns1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <book id="bk101" ns:genre="Computers">
        <author>John Smith</author>
        <title>Python Programming</title>
        <xsi:schemaLocation="http://example.com/ns1 http://example.com/ns1.xsd"/>
        <genre>ns:genre</genre>
        <price>39.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>An introduction to programming.</description>
    </book>
    <book id="bk102" ns:genre="Computers">
        <author>Jane Doe</author>
        <title>XSLT Programming</title>
        <xsi:schemaLocation="http://example.com/ns1 http://example.com/ns1.xsd"/>
        <genre>ns:genre</genre>
        <price>49.95</price>
        <publish_date>2000-10-01</publish_date>
        <description>A guide to XSLT.</description>
    </book>
</catalog>
"""

# Feed the XML string into the parser
parser.parse(xml_string)
```
This code will print out the elements of the XML file with their names and attributes, taking into account multiple namespaces.
