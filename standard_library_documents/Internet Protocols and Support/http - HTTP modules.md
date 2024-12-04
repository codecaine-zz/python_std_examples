# http — HTTP modules

**HTTP Modules in Python**
==========================

The `http` module in Python provides classes and functions for working with HTTP protocols.

### 1. Creating an HTTP Client

You can use the `HTTPClient` class from the `http.client` module to create a client that can connect to an HTTP server and perform various operations.
```python
import http.client

# Create an HTTP client object
client = http.client.HTTPConnection('www.example.com')

try:
    # Send a GET request
    client.request('GET', '/')

    # Get the response
    response = client.getresponse()

    # Print the status code and headers
    print(response.status)
    print(response.headers)

except http.client.HTTPException as e:
    print(e.message)
finally:
    # Close the connection
    client.close()
```
### 2. Creating an HTTP Server

You can use the `BaseHTTPServer` class from the `http.server` module to create a simple HTTP server.
```python
import http.server
import socketserver

# Create a class that inherits from BaseHTTPRequestHandler
class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

# Create an HTTP server object
server = socketserver.TCPServer(('localhost', 8000), RequestHandler)

print('Server started on port 8000...')
server.serve_forever()
```
### 3. Working with HTTP Responses

You can use the `HTTPResponse` class from the `http.client` module to work with HTTP responses.
```python
import http.client

# Create an HTTP client object
client = http.client.HTTPConnection('www.example.com')

try:
    # Send a GET request
    client.request('GET', '/')

    # Get the response
    response = client.getresponse()

    # Print the status code and headers
    print(response.status)
    print(response.headers)

except http.client.HTTPException as e:
    print(e.message)

# Print the content of the response
print(response.read())
```
### 4. Working with HTTP Headers

You can use the `HTTPHeaders` class from the `http.client` module to work with HTTP headers.
```python
import http.client

# Create an HTTP client object
client = http.client.HTTPConnection('www.example.com')

try:
    # Send a GET request
    client.request('GET', '/')

    # Get the response
    response = client.getresponse()

    # Print the headers
    for key, value in response.headers.items():
        print(f'{key}: {value}')

except http.client.HTTPException as e:
    print(e.message)
```
### 5. Working with HTTP Cookies

You can use the `HTTPCookie` class from the `http.cookiejar` module to work with HTTP cookies.
```python
import http.client
from http.cookiejar import Cookie

# Create an HTTP client object
client = http.client.HTTPConnection('www.example.com')

try:
    # Send a GET request
    client.request('GET', '/')

    # Get the response
    response = client.getresponse()

    # Get the cookies
    cookies = response.getheaders().get_all('Set-Cookie')

    # Print the cookies
    for cookie in cookies:
        print(cookie)

except http.client.HTTPException as e:
    print(e.message)
```
### 6. Working with HTTP Authentication

You can use the `HTTPAuth` class from the `http.client` module to work with HTTP authentication.
```python
import http.client

# Create an HTTP client object
client = http.client.HTTPConnection('www.example.com')

try:
    # Send a request with basic authentication
    client.request('GET', '/', auth=('username', 'password'))

except http.client.HTTPException as e:
    print(e.message)
```
### 7. Working with HTTPS

You can use the `HTTPServer` class from the `http.server` module to create an HTTPS server.
```python
import http.server
import socketserver
import ssl

# Create a context for SSL
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

# Create a class that inherits from BaseHTTPRequestHandler
class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

# Create an HTTPS server object
server = socketserver.TCPServer(('localhost', 8000), RequestHandler, context=context)

print('Server started on port 8000...')
server.serve_forever()
```
### 8. Working with WebSocket

You can use the `websockets` library to work with WebSockets in Python.
```python
import asyncio
import websockets

async def handle_connection(websocket):
    while True:
        # Receive a message from the client
        message = await websocket.recv()

        # Send a response back to the client
        await websocket.send(message)

async def main():
    async with websockets.serve(handle_connection, 'localhost', 8000) as server:
        print('Server started on port 8000...')
        await server.wait_closed()

asyncio.run(main())
```
Note: The `websockets` library is not part of the standard Python library and needs to be installed separately using pip.
