# http - HTTP modules

The `http` module is part of the Python Standard Library and provides a simple interface to make HTTP requests. Below are comprehensive code examples for various functionalities within the `http` module, along with explanations for each example.

### 1. Using the `requests` library

If you want to use more advanced features like handling cookies, sessions, or custom headers, consider using the `requests` library. Here's a basic example:

```python
# Importing the requests library
import requests

# Making a GET request to a URL
response = requests.get('https://api.example.com/data')

# Checking if the request was successful
if response.status_code == 200:
    # Printing the content of the response
    print(response.text)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

# Making a POST request with custom headers and parameters
headers = {'User-Agent': 'MyApp/1.0'}
data = {'key1': 'value1', 'key2': 'value2'}

response = requests.post('https://api.example.com/submit', headers=headers, data=data)

if response.status_code == 200:
    # Printing the content of the response
    print(response.text)
else:
    print(f"Failed to submit data. Status code: {response.status_code}")
```

### 2. Making GET Requests

```python
import http.client

# Creating a connection to an HTTP server
conn = http.client.HTTPConnection('www.example.com')

# Sending a GET request with parameters
params = urllib.parse.urlencode({'param1': 'value1', 'param2': 'value2'})
conn.request("GET", "/path?%s" % params)

# Reading the response from the server
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()

# Closing the connection
conn.close()

# Printing the content of the response
print(data.decode('utf-8'))
```

### 3. Making POST Requests

```python
import http.client

# Creating a connection to an HTTP server
conn = http.client.HTTPConnection('www.example.com')

# Sending a POST request with headers and data
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = urllib.parse.urlencode({'key1': 'value1', 'key2': 'value2'})
conn.request("POST", "/path", body=data, headers=headers)

# Reading the response from the server
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()

# Closing the connection
conn.close()

# Printing the content of the response
print(data.decode('utf-8'))
```

### 4. Handling Cookies

```python
import http.client

# Creating a connection to an HTTP server
conn = http.client.HTTPConnection('www.example.com')

# Sending a GET request with cookies
cookies = urllib.parse.urlencode({'cookie1': 'value1', 'cookie2': 'value2'})
headers = {'Cookie': cookies}
conn.request("GET", "/path", headers=headers)

# Reading the response from the server
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()

# Closing the connection
conn.close()

# Printing the content of the response
print(data.decode('utf-8'))
```

### 5. Handling Redirects

```python
import http.client

# Creating a connection to an HTTP server with follow redirects enabled
conn = http.client.HTTPConnection('www.example.com')

# Sending a GET request with follow_redirects set to True
headers = {'User-Agent': 'MyApp/1.0'}
conn.request("GET", "/path?redirect=1", headers=headers)

# Reading the response from the server
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()

# Closing the connection
conn.close()

# Printing the content of the response
print(data.decode('utf-8'))
```

### 6. Handling HTTP Exceptions

```python
import http.client

try:
    # Creating a connection to an HTTP server
    conn = http.client.HTTPConnection('www.example.com')

    # Sending a GET request with parameters
    params = urllib.parse.urlencode({'param1': 'value1', 'param2': 'value2'})
    conn.request("GET", "/path?%s" % params)

    # Reading the response from the server
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()

    # Closing the connection
    conn.close()

    # Printing the content of the response
    print(data.decode('utf-8'))

except http.client.HTTPException as e:
    print(f"An error occurred: {e}")
```

### 7. Making Requests with Timeout

```python
import http.client

try:
    # Creating a connection to an HTTP server with timeout set to 5 seconds
    conn = http.client.HTTPConnection('www.example.com')

    # Sending a GET request with parameters and timeout
    params = urllib.parse.urlencode({'param1': 'value1', 'param2': 'value2'})
    conn.request("GET", "/path?%s" % params, timeout=5)

    # Reading the response from the server
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()

    # Closing the connection
    conn.close()

    # Printing the content of the response
    print(data.decode('utf-8'))

except http.client.HTTPException as e:
    print(f"An error occurred: {e}")

except TimeoutError:
    print("The request timed out.")
```

These examples demonstrate different aspects of making HTTP requests using Python's `http` module. Each example includes comments to explain the purpose and functionality of each part of the code.
