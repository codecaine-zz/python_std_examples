# ssl - TLS/SSL wrapper for socket objects

**ssl Module Examples**
==========================

The `ssl` module provides a way to access SSL/TLS support in Python's standard library.

### 1. Creating an SSL Context

An SSL context is used to specify the SSL/TLS parameters for a connection.
```python
import ssl

# Create a new SSL context
context = ssl.create_default_context()

# Get the default server certificate
print(context.check_hostname('www.example.com'))  # Should print: True
print(context.verify_mode)  # Should print: SSL_VERIFIED

# Create an SSL connection
with ssl.wrap_socket(socket.socket(socket.AF_INET), server_side=True, cert_reqs=ssl.CERT_REQUIRED, ca_certs=None) as s:
    print(s.getpeercert())  # Should print the server's certificate
```
### 2. Creating a Client-Side Connection

To create a client-side connection, you need to specify the SSL/TLS parameters and the server hostname.
```python
import ssl

# Create an SSL context with custom parameters
context = ssl.create_default_context()
context.check_hostname('www.example.com')  # Should print: True
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile='path/to/ca.crt')

# Create a client socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Wrap the socket with SSL/TLS
    with context.wrap_socket(s, server_hostname='www.example.com') as ssl_s:
        # Establish the connection
        ssl_s.connect(('www.example.com', 443))
```
### 3. Creating a Server-Side Connection

To create a server-side connection, you need to specify the SSL/TLS parameters and handle incoming connections.
```python
import socket
import ssl

# Create a server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to a address and port
    s.bind(('localhost', 443))
    # Listen for incoming connections
    s.listen(1)

    while True:
        # Accept an incoming connection
        with ssl.wrap_socket(s.accept()[0], server_side=True, cert_reqs=ssl.CERT_REQUIRED) as ssl_s:
            print('Connection accepted')
            while True:
                # Receive data from the client
                data = ssl_s.recv(1024)
                if not data:
                    break
                print(data.decode())
```
### 4. Verifying Server Certificates

To verify a server's certificate, you can use the `check_hostname` method or `verify_mode`.
```python
import ssl

# Create an SSL context with custom parameters
context = ssl.create_default_context()
context.check_hostname('www.example.com')  # Should print: True
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile='path/to/ca.crt')

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Wrap the socket with SSL/TLS
        with context.wrap_socket(s, server_hostname='www.example.com') as ssl_s:
            # Establish the connection
            ssl_s.connect(('www.example.com', 443))
except ssl.SSLError:
    print('Server certificate is invalid')
```
### 5. Using TLS Certificates

To use a custom TLS certificate, you can specify it when creating an SSL context.
```python
import ssl

# Create an SSL context with custom parameters
context = ssl.create_default_context()
context.load_cert_chain(certfile='path/to/client.crt', keyfile='path/to/client.key')

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Wrap the socket with SSL/TLS
        with context.wrap_socket(s, server_hostname='www.example.com') as ssl_s:
            # Establish the connection
            ssl_s.connect(('www.example.com', 443))
except ssl.SSLError:
    print('Server certificate is invalid')
```
### 6. Handling SSL/TLS Errors

To handle SSL/TLS errors, you can use try-except blocks.
```python
import ssl

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Wrap the socket with SSL/TLS
        with context.wrap_socket(s, server_hostname='www.example.com') as ssl_s:
            # Establish the connection
            ssl_s.connect(('www.example.com', 443))
except ssl.SSLError as e:
    print(f'SSL/TLS error: {e}')
```
Note: The above examples are for illustration purposes only and should not be used in production without proper testing and validation.
