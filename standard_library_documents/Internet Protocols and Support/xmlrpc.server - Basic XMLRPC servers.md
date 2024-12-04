# xmlrpc.server - Basic XMLRPC servers

The `xmlrpc.server` module is part of Python's standard library, providing a simple way to create basic XML-RPC servers. Below are comprehensive examples demonstrating various functionalities within this module, including creating both HTTP and SimpleXMLRPC servers.

### Example 1: Creating an HTTP Basic Server

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import xmlrpc.server

# Define a custom request handler class
class RequestHandler(xmlrpc.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Parse the request and extract XML-RPC data
        content_length = int(self.headers['Content-Length'])
        payload = self.rfile.read(content_length)
        
        # Process the XML-RPC call
        response = handle_xmlrpc_call(payload.decode())
        
        # Send the response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/xml')
        self.end_headers()
        self.wfile.write(response.encode())

def handle_xmlrpc_call(method):
    # This is a placeholder function where you can implement your XML-RPC logic
    if method == "add":
        return xmlrpc.server.dumps([20, 30], methodname="result")
    else:
        return xmlrpc.server.dumps("Unknown method", faultcode=1, faultstring="Method not found")

# Set up the server and port
server_address = ('', 8000)
httpd = HTTPServer(server_address, RequestHandler)

# Start the server
print("Starting XML-RPC Server on port 8000")
httpd.serve_forever()
```

### Explanation:
- **HTTPServer**: This is used to create an HTTP server. The `RequestHandler` class is a subclass of `SimpleHTTPRequestHandler` from `xmlrpc.server`, which handles XML-RPC requests.
- **do_POST Method**: This method processes POST requests, extracts the payload, and sends a response back to the client. It uses `xmlrpc.server.dumps` to serialize the result of an XML-RPC call.
- **handle_xmlrpc_call Function**: This function contains the logic for processing XML-RPC methods. In this example, it handles an `add` method that returns the sum of two numbers.

### Example 2: Creating a SimpleXMLRPC Server

```python
import xmlrpc.server

# Define a simple class with XML-RPC methods
class Math:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

# Create an instance of the handler class and specify the port
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8001))

# Register methods with the server
server.register_instance(Math())

# Print a message indicating that the server is running
print("Starting XML-RPC Server on port 8001")

# Start the server
server.serve_forever()
```

### Explanation:
- **Math Class**: This class contains two XML-RPC methods: `add` and `subtract`.
- **SimpleXMLRPCServer**: This creates a simple XML-RPC server that listens on localhost at port 8001.
- **register_instance Method**: This method registers the instance of the `Math` class with the server, making its methods available via XML-RPC.
- **serve_forever Method**: This starts the server and keeps it running indefinitely, accepting incoming connections.

These examples provide a basic framework for creating XML-RPC servers using Python's standard library. You can expand upon these examples by adding more methods, handling different types of requests, or integrating with other parts of your application.
