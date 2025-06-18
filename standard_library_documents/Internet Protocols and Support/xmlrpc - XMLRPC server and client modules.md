# xmlrpc - XMLRPC server and client modules
## Table of Contents

1. [1. Creating an XML-RPC Server](#1-creating-an-xml-rpc-server)
2. [2. Handling XML-RPC Requests](#2-handling-xml-rpc-requests)
3. [3. Using an XML-RPC Client](#3-using-an-xml-rpc-client)
4. [4. Customizing XML-RPC Server Behavior](#4-customizing-xml-rpc-server-behavior)
5. [5. Using `jsonrpc` Module for JSON-RPC Server and Client](#5-using-jsonrpc-module-for-json-rpc-server-and-client)
6. [Server Example with `jsonrpc`:](#server-example-with-jsonrpc)
7. [Client Example with `jsonrpc`:](#client-example-with-jsonrpc)



The `xmlrpc` module in Python is a part of the Standard Library and provides support for making XML-RPC requests and responses. Below are comprehensive code examples that demonstrate various functionalities within this module, including creating an XML-RPC server, handling XML-RPC requests, and using an XML-RPC client to communicate with an XML-RPC server.

### 1. Creating an XML-RPC Server

This example demonstrates how to create a basic XML-RPC server using the `SimpleXMLRPCServer` class from the `xmlrpc.server` module.

```python
from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers. Returns None if division by zero is attempted."""
    if y == 0:
        raise Exception("Cannot divide by zero")
    return x / y

# Create an XML-RPC server instance on port 8000
server = SimpleXMLRPCServer(("localhost", 8000))

# Register functions to the server
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

# Start the XML-RPC server loop
print("Starting server...")
server.serve_forever()
```

### 2. Handling XML-RPC Requests

This example shows how to handle requests received by the XML-RPC server.

```python
from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    """Add two numbers."""
    return x + y

# Create an instance of SimpleXMLRPCServer and register functions
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add, "add")

# Define a custom exception handler to log errors
def handle_exception(exc, value, tb):
    print(f"Error: {exc}, {value}")

server.set_exception_handler(handle_exception)

# Start the server
print("Starting server...")
server.serve_forever()
```

### 3. Using an XML-RPC Client

This example demonstrates how to use a client to communicate with an XML-RPC server.

```python
import xmlrpc.client

def add(x, y):
    """Add two numbers."""
    return x + y

# Create an XML-RPC client and connect to the server
client = xmlrpc.client.ServerProxy("http://localhost:8000")

# Call a method on the server
result = client.add(5, 3)
print(f"The result of add is {result}")

# Handle exceptions for RPC calls
try:
    result = client.divide(10, 0)
except xmlrpc.client.Fault as fault:
    print(f"Error from server: {fault.faultString}")
```

### 4. Customizing XML-RPC Server Behavior

This example shows how to customize the behavior of an XML-RPC server by adding error handling and logging.

```python
from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    """Add two numbers."""
    return x + y

# Create an XML-RPC server instance
server = SimpleXMLRPCServer(("localhost", 8000))

# Register functions to the server
server.register_function(add, "add")

# Define custom exception handling to log errors
def handle_exception(exc, value, tb):
    print(f"Error: {exc}, {value}")

server.set_exception_handler(handle_exception)

# Start the server and handle exceptions
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server shutting down...")
```

### 5. Using `jsonrpc` Module for JSON-RPC Server and Client

The `jsonrpc` module provides a more modern, feature-rich alternative to XML-RPC.

#### Server Example with `jsonrpc`:

```python
from jsonrpcserver import methods, serve

@methods.add
def add(x, y):
    """Add two numbers."""
    return x + y

@methods.add
def subtract(x, y):
    """Subtract two numbers."""
    return x - y

if __name__ == "__main__":
    serve(add)
```

#### Client Example with `jsonrpc`:

```python
import requests

# Define the URL of the JSON-RPC server
url = "http://localhost:8001"

# Function to make a JSON-RPC request
def make_rpc_request(method, params):
    response = requests.post(url, json={"method": method, "params": params, "jsonrpc": "2.0", "id": 1})
    return response.json()

# Call the 'add' method on the server
result = make_rpc_request("add", [5, 3])
print(f"The result of add is {result}")
```

These examples cover basic and advanced functionalities of the `xmlrpc` module. Each example includes comments to explain key steps and behaviors. You can adapt these examples to suit your specific needs or integrate them into larger applications.
