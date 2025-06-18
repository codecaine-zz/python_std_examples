# ssl - TLS/SSL wrapper for socket objects
## Table of Contents

1. [1. Creating an SSL Context](#1-creating-an-ssl-context)
2. [2. Server-Side SSL Configuration](#2-server-side-ssl-configuration)
3. [3. Client-Side Verification of Server Certificate](#3-client-side-verification-of-server-certificate)
4. [4. Using a Custom Certificate Store](#4-using-a-custom-certificate-store)
5. [5. Handling SSL Errors](#5-handling-ssl-errors)
6. [6. Using a Specific SSL Protocol](#6-using-a-specific-ssl-protocol)
7. [7. Server-Side Handling of Client Authentication](#7-server-side-handling-of-client-authentication)
8. [8. Using SSL/TLS with SOCKS Proxy](#8-using-ssltls-with-socks-proxy)



The `ssl` module in Python provides a way to create secure network connections using SSL/TLS protocols. It allows you to wrap existing socket objects with an encrypted layer, making it suitable for applications that require secure communication.

Below are some comprehensive code examples demonstrating various functionalities of the `ssl` module:

### 1. Creating an SSL Context

```python
import ssl
import socket

# Create a context object using the default settings
context = ssl.create_default_context()

# Alternatively, create a context with specific options
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# context.verify_mode = ssl.CERT_REQUIRED
# context.load_verify_locations('path/to/certificates')

# Wrap an existing socket object with the SSL context
with socket.create_connection(('example.com', 443)) as sock:
    with context.wrap_socket(sock, server_hostname='example.com') as ssock:
        print("SSL connection established successfully!")
```

### 2. Server-Side SSL Configuration

```python
import ssl
import socket

# Create a secure socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to an address and port
server_socket.bind(('localhost', 443))

# Set the socket to listen for incoming connections
server_socket.listen(5)

# Create an SSL context with specific options
context = ssl.create_default_context()
context.load_cert_chain('path/to/cert.pem', 'path/to/key.pem')

# Accept a connection and wrap it with SSL
client_socket, addr = server_socket.accept()
with context.wrap_socket(client_socket, server_side=True) as ssock:
    print("SSL handshake completed:", ssock.version)
```

### 3. Client-Side Verification of Server Certificate

```python
import ssl
import socket

# Create a context object with certificate verification enabled
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations('path/to/certificates')

# Wrap an existing socket object with the SSL context
with socket.create_connection(('example.com', 443)) as sock:
    with context.wrap_socket(sock, server_hostname='example.com') as ssock:
        print("SSL connection established successfully!")
```

### 4. Using a Custom Certificate Store

```python
import ssl
import socket

# Create a custom certificate store for the context
context = ssl.create_default_context()
context.load_verify_locations('path/to/custom/certs')

# Wrap an existing socket object with the SSL context
with socket.create_connection(('example.com', 443)) as sock:
    with context.wrap_socket(sock, server_hostname='example.com') as ssock:
        print("SSL connection established successfully!")
```

### 5. Handling SSL Errors

```python
import ssl
import socket

# Create a context object using default settings
context = ssl.create_default_context()

try:
    # Wrap an existing socket object with the SSL context
    with socket.create_connection(('example.com', 443)) as sock:
        with context.wrap_socket(sock, server_hostname='example.com') as ssock:
            print("SSL connection established successfully!")
except ssl.SSLError as e:
    print(f"An SSL error occurred: {e}")
```

### 6. Using a Specific SSL Protocol

```python
import ssl
import socket

# Create a context object for a specific SSL protocol version
context = ssl.create_default_context(ssl.PROTOCOL_TLSv1_2)

# Wrap an existing socket object with the SSL context
with socket.create_connection(('example.com', 443)) as sock:
    with context.wrap_socket(sock, server_hostname='example.com') as ssock:
        print(f"SSL connection using TLSv1.2 established successfully!")
```

### 7. Server-Side Handling of Client Authentication

```python
import ssl
import socket

# Create a secure socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to an address and port
server_socket.bind(('localhost', 443))

# Set the socket to listen for incoming connections
server_socket.listen(5)

# Create an SSL context with client authentication enabled
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain('path/to/cert.pem', 'path/to/key.pem')
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations('path/to/certificates')

# Accept a connection and wrap it with SSL
client_socket, addr = server_socket.accept()
with context.wrap_socket(client_socket, server_side=True) as ssock:
    print("SSL handshake completed:", ssock.version)
    # Check if the client provided a valid certificate
    try:
        peer_cert = ssock.getpeercert()
        print("Client's certificate:", peer_cert)
    except ssl.SSLError:
        print("The client did not provide a valid certificate.")
```

### 8. Using SSL/TLS with SOCKS Proxy

```python
import ssl
import socket
import socks

# Set up a SOCKS proxy (e.g., using PySocks)
socks.set_default_proxy(socks.SOCKS5, 'proxy_host', 1080)

# Create a context object for the default protocol
context = ssl.create_default_context()

# Wrap an existing socket object with the SSL context
with socket.create_connection(('example.com', 443)) as sock:
    with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as ssock:
        ssock.connect((socks.DEFAULT_PROXY_HOST, socks.DEFAULT_PROXY_PORT))
        with context.wrap_socket(ssock) as ssl_sock:
            print("SSL connection through SOCKS proxy established successfully!")
```

These examples cover a range of use cases for the `ssl` module, from basic server and client configurations to handling errors and using specific SSL protocols. Each example includes comments to help understand each step and is designed to be included in official documentation or tutorials.
