# xmlrpc.server — Basic XMLRPC servers

**XMLRPC Server Code Generation**
=====================================

Below is an example of how to create an XMLRPC server using Python's `xmlrpc.server` module.

```python
import xmlrpc.server

class SimpleXMLRPCServer:
    def __init__(self):
        # Create an XML-RPC server object
        self.server = xmlrpc.server.SimpleXMLRPCServer(
            host="localhost",
            port=8000,
            logRequests=True,
            allow_none=True
        )

    def add(self, x, y):
        """Add two numbers together"""
        return x + y

    def greet(self, name):
        """Print a greeting message"""
        return f"Hello, {name}!"

    def square(self, x):
        """Calculate the square of a number"""
        return x ** 2


def main():
    # Create an instance of the SimpleXMLRPCServer class
    server = SimpleXMLRPCServer()

    # Register the functions with the server
    server.register_function(server.add)
    server.register_function(server.greet)
    server.register_function(server.square)

    print("Server started on http://localhost:8000")

    # Run the server until it is stopped manually
    from threading import Thread
    def run_server():
        print("Running server...")
        server.serve_forever()
    thread = Thread(target=run_server)
    thread.start()

    while True:
        pass


if __name__ == "__main__":
    main()
```

**Explanation**
---------------

*   We create an instance of `SimpleXMLRPCServer` with the desired host, port, and other options.
*   We define three functions: `add`, `greet`, and `square`.
*   We register these functions with the server using the `register_function` method.
*   We start the server on a specific host and port, and then run it indefinitely until manually stopped.

**Using the Server**
--------------------

To use this server, you can make requests to `http://localhost:8000/` in your favorite web browser or using tools like `curl`.

Example request:

```bash
curl -X GET http://localhost:8000/?method=add&arg1=2&arg2=3
```

This should return the result of the `add` function, which is `5`.
