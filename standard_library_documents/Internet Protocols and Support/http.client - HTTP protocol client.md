# http.client — HTTP protocol client

Here's an example of how you can use the `http.client` module in Python:
```python
import http.client

# Create an HTTP connection
conn = http.client.HTTPSConnection("example.com")

try:
    # Send a GET request to the specified URL
    conn.request("GET", "/path/to/resource", None, {"User-Agent": "My Client/1.0"})

    # Get the response status code and reason phrase
    response_status = conn.getresponse().status
    response_reason = conn.getresponse().reason

    print(f"Status Code: {response_status}")
    print(f"Reason Phrase: {response_reason}")

except http.client.HTTPException as e:
    print(f"Error: {e}")

finally:
    # Close the HTTP connection
    conn.close()
```

**HTTP POST Request**
```python
import http.client

conn = http.client.HTTPSConnection("example.com")

try:
    # Send a POST request to the specified URL with data
    data = {"key": "value"}
    headers = {"Content-Type": "application/json"}
    conn.request("POST", "/path/to/resource", str(data), headers)

    response_status = conn.getresponse().status
    response_reason = conn.getresponse().reason

    print(f"Status Code: {response_status}")
    print(f"Reason Phrase: {response_reason}")

except http.client.HTTPException as e:
    print(f"Error: {e}")

finally:
    conn.close()
```

**HTTP PUT Request**
```python
import http.client

conn = http.client.HTTPSConnection("example.com")

try:
    # Send a PUT request to the specified URL with data
    data = {"key": "value"}
    headers = {"Content-Type": "application/json"}
    conn.request("PUT", "/path/to/resource", str(data), headers)

    response_status = conn.getresponse().status
    response_reason = conn.getresponse().reason

    print(f"Status Code: {response_status}")
    print(f"Reason Phrase: {response_reason}")

except http.client.HTTPException as e:
    print(f"Error: {e}")

finally:
    conn.close()
```

**HTTP DELETE Request**
```python
import http.client

conn = http.client.HTTPSConnection("example.com")

try:
    # Send a DELETE request to the specified URL
    headers = {"Content-Type": "application/json"}
    conn.request("DELETE", "/path/to/resource", None, headers)

    response_status = conn.getresponse().status
    response_reason = conn.getresponse().reason

    print(f"Status Code: {response_status}")
    print(f"Reason Phrase: {response_reason}")

except http.client.HTTPException as e:
    print(f"Error: {e}")

finally:
    conn.close()
```

**Sending a request with authentication**
```python
import http.client
from http.client import HTTPBasicAuthHandler

auth_handler = HTTPBasicAuthHandler(("username", "password"))
conn = http.client.HTTPSConnection("example.com", handlers=[auth_handler])

try:
    # Send a GET request to the specified URL
    conn.request("GET", "/path/to/resource")

    response_status = conn.getresponse().status
    response_reason = conn.getresponse().reason

    print(f"Status Code: {response_status}")
    print(f"Reason Phrase: {response_reason}")

except http.client.HTTPException as e:
    print(f"Error: {e}")

finally:
    conn.close()
```

**Sending a request with multiple authentication headers**
```python
import http.client
from http.client import HTTPBasicAuthHandler

auth_handler = HTTPBasicAuthHandler(("username", "password"))
headers = {"Authorization": "Bearer token"}
conn = http.client.HTTPSConnection("example.com", handlers=[auth_handler])

try:
    # Send a GET request to the specified URL
    conn.request("GET", "/path/to/resource", None, headers)

    response_status = conn.getresponse().status
    response_reason = conn.getresponse().reason

    print(f"Status Code: {response_status}")
    print(f"Reason Phrase: {response_reason}")

except http.client.HTTPException as e:
    print(f"Error: {e}")

finally:
    conn.close()
```

Note that the `http.client` module provides a basic implementation of HTTP protocol. It does not provide support for all the features and options available in modern web frameworks, such as SSL/TLS verification or header validation. For more complex use cases, you may want to consider using an established library like `requests`.
