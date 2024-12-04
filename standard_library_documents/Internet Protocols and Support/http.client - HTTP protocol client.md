# http.client - HTTP protocol client

The `http.client` module is part of the Python standard library and provides a simple HTTP/1.1 client interface for making requests to web servers. Below are comprehensive examples for various functionalities provided by this module:

### 1. Basic GET Request

```python
import http.client

# Create an HTTP connection to a server
conn = http.client.HTTPConnection("example.com")

# Make a GET request
conn.request("GET", "/")
response = conn.getresponse()

# Read the response from the server
data = response.read()
print(data.decode('utf-8'))

# Close the connection
conn.close()
```

### 2. Handling Headers and Query Parameters

```python
import http.client
from urllib.parse import urlencode

# Create an HTTP connection to a server
conn = http.client.HTTPConnection("example.com")

# Define query parameters
params = {"key": "value", "page": 1}

# Encode the parameters into a URL string
query_string = urlencode(params)

# Make a GET request with query parameters
url = "/search?" + query_string
conn.request("GET", url)
response = conn.getresponse()

# Read and decode the response
data = response.read()
print(data.decode('utf-8'))

# Close the connection
conn.close()
```

### 3. POST Request with Form Data

```python
import http.client
from urllib.parse import urlencode

# Create an HTTP connection to a server
conn = http.client.HTTPConnection("example.com")

# Define form data
form_data = {"username": "user", "password": "pass"}

# Encode the form data into a URL-encoded string
data = urlencode(form_data)

# Make a POST request with form data
url = "/login"
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
conn.request("POST", url, headers=headers, body=data)
response = conn.getresponse()

# Read and decode the response
data = response.read()
print(data.decode('utf-8'))

# Close the connection
conn.close()
```

### 4. Using HTTP/1.1 Connection Pooling

```python
import http.client
from urllib.parse import urlencode
import socket

# Create an HTTP connection pool manager
pool_manager = http.client.HTTPConnectionPool(maxsize=5)

# Define query parameters
params = {"key": "value", "page": 1}

# Encode the parameters into a URL string
query_string = urlencode(params)

# Make a GET request with query parameters using the connection pool
url = "/search?" + query_string

with pool_manager.connection() as conn:
    conn.request("GET", url)
    response = conn.getresponse()

# Read and decode the response
data = response.read()
print(data.decode('utf-8'))
```

### 5. Handling Redirects

```python
import http.client

# Create an HTTP connection to a server
conn = http.client.HTTPConnection("example.com")

# Make a GET request that may result in a redirect
url = "/redirect"
conn.request("GET", url)
response = conn.getresponse()

# Read and decode the response
data = response.read()
print(data.decode('utf-8'))

# Get the location header to follow the redirect
location = response.getheader('Location')
if location:
    print(f"Redirecting to: {location}")
else:
    print("No redirect found.")

# Close the connection
conn.close()
```

### 6. Handling Exceptions

```python
import http.client

try:
    # Create an HTTP connection to a server that may not be reachable
    conn = http.client.HTTPConnection("nonexistent-domain.com")
    
    # Make a GET request
    conn.request("GET", "/")
    response = conn.getresponse()
    
    # Read and decode the response
    data = response.read()
    print(data.decode('utf-8'))
except http.client.HTTPException as e:
    print(f"HTTP error occurred: {e}")
finally:
    # Close the connection
    conn.close()
```

### 7. Using SSL/TLS

```python
import http.client

# Create an HTTPS connection to a server with SSL/TLS enabled
conn = http.client.HTTPSConnection("example.com")

# Make a GET request over HTTPS
conn.request("GET", "/")
response = conn.getresponse()

# Read and decode the response
data = response.read()
print(data.decode('utf-8'))

# Close the connection
conn.close()
```

### 8. Handling Large Responses

```python
import http.client

# Create an HTTP connection to a server that may have large responses
conn = http.client.HTTPConnection("example.com")

# Make a GET request for a large file
url = "/large-file"
conn.request("GET", url)
response = conn.getresponse()

# Read the response in chunks to handle large files
chunk_size = 1024
while True:
    chunk = response.read(chunk_size)
    if not chunk:
        break
    print(chunk.decode('utf-8'), end='')

# Close the connection
conn.close()
```

### 9. Handling Keep-Alive Connections

```python
import http.client

# Create an HTTP connection with keep-alive enabled
conn = http.client.HTTPConnection("example.com")

# Make multiple requests using the same connection
url1 = "/resource1"
conn.request("GET", url1)
response1 = conn.getresponse()
print(response1.status, response1.reason)

url2 = "/resource2"
conn.request("GET", url2)
response2 = conn.getresponse()
print(response2.status, response2.reason)

# Close the connection
conn.close()
```

These examples cover a range of functionalities available in the `http.client` module, from basic HTTP requests to handling redirects, exceptions, and large responses. Each example includes comments to explain key steps and is designed for clarity and educational purposes.
