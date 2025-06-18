# http.server - HTTP servers
## Table of Contents

1. [Example 1: Simple HTTP Server](#example-1-simple-http-server)
2. [Example 2: Handling GET Requests](#example-2-handling-get-requests)
3. [Example 3: Handling POST Requests](#example-3-handling-post-requests)
4. [Example 4: Serving Static Files](#example-4-serving-static-files)
5. [Example 5: Using HTTPS](#example-5-using-https)
6. [Example 6: Using the `http.server` module with a custom handler](#example-6-using-the-httpserver-module-with-a-custom-handler)
7. [Example 7: Using `http.server` with a multi-threaded server](#example-7-using-httpserver-with-a-multi-threaded-server)



Below is a comprehensive set of code examples demonstrating various functionalities provided by the `http.server` module in Python 3.12. These examples cover creating simple HTTP servers, handling GET and POST requests, serving static files, and more.

### Example 1: Simple HTTP Server

A basic example of setting up an HTTP server using `http.server`.

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Write the HTML message
        html_message = "<html><head><title>Simple HTTP Server</title></head><body>Hello, World!</body></html>"
        self.wfile.write(html_message.encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

### Example 2: Handling GET Requests

This example demonstrates handling GET requests by retrieving a query parameter.

```python
from http.server import BaseHTTPRequestHandler, CGIHTTPRequestHandler
import cgi

class MyCGIHTTPRequestHandler(CGIHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL to get parameters
        params = cgi.parse_qs(self.path[1:])
        
        if 'name' in params:
            name = params['name'][0]
            html_message = f"<html><head><title>GET Request Handler</title></head><body>Hello, {name}!</body></html>"
        else:
            html_message = "<html><head><title>GET Request Handler</title></head><body>Please provide a name.</body></html>"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_message.encode())

def run(server_class=HTTPServer, handler_class=MyCGIHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

### Example 3: Handling POST Requests

This example demonstrates handling POST requests by processing form data.

```python
from http.server import BaseHTTPRequestHandler, CGIHTTPRequestHandler
import cgi

class MyCGIHTTPRequestHandler(CGIHTTPRequestHandler):
    def do_POST(self):
        # Parse the form data from the request
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Parse the POST data as URL-encoded parameters
        params = cgi.parse_qs(post_data.decode())
        
        if 'name' in params:
            name = params['name'][0]
            html_message = f"<html><head><title>POST Request Handler</title></head><body>Hello, {name}!</body></html>"
        else:
            html_message = "<html><head><title>POST Request Handler</title></head><body>Please provide a name.</body></html>"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_message.encode())

def run(server_class=HTTPServer, handler_class=MyCGIHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

### Example 4: Serving Static Files

This example demonstrates serving static files from a directory.

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleStaticHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve files from the current directory
        try:
            file_path = self.path[1:]
            if not file_path:
                file_path = 'index.html'
            
            with open(file_path, 'rb') as f:
                content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "File not found")

def run(server_class=HTTPServer, handler_class=SimpleStaticHTTPServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

### Example 5: Using HTTPS

This example demonstrates setting up an HTTPS server using the `http.server` module with a self-signed certificate.

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

class SimpleHTTPSRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code and headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Write the HTML message
        html_message = "<html><head><title>HTTPS Server</title></head><body>Hello, World!</body></html>"
        self.wfile.write(html_message.encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPSRequestHandler, port=443):
    # Generate a self-signed certificate and key
    server_address = ('', port)
    
    # Use ssl.wrap_socket to secure the server connection
    httpd = server_class(server_address, handler_class)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                     server_side=True,
                                     certfile='server.crt',
                                     keyfile='server.key')
    
    print(f"Serving HTTPS on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

### Example 6: Using the `http.server` module with a custom handler

This example demonstrates using a custom handler class to handle requests in more complex ways.

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code and headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Handle the request based on the URL path
        if self.path == '/':
            html_message = "<html><head><title>Custom Request Handler</title></head><body>Welcome to the custom handler.</body></html>"
        else:
            html_message = f"<html><head><title>Error</title></head><body>Unknown endpoint: {self.path}</body></html>"
        
        self.wfile.write(html_message.encode())

def run(server_class=HTTPServer, handler_class=CustomRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

### Example 7: Using `http.server` with a multi-threaded server

This example demonstrates running an HTTP server using multiple threads to handle concurrent requests.

```python
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

class ThreadedSimpleHTTPRequestHandler(ThreadingHTTPServer):
    def __init__(self, server_address, handler_class=BaseHTTPRequestHandler):
        super().__init__(server_address, handler_class)
        self.daemon_threads = True  # Allow threads to exit when main program exits

def run(server_class=ThreadedSimpleHTTPRequestHandler, handler_class=BaseHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {port} (multi-threaded)...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

These examples provide a comprehensive overview of the functionalities available in the `http.server` module. Each example is designed to be clear and self-contained, making it suitable for inclusion in official documentation or as part of a larger application.
