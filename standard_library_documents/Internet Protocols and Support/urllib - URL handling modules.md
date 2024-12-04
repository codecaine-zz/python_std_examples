# urllib — URL handling modules

**URllib Module Code Examples**
=====================================

The `urllib` module provides a way of accessing URLs in Python. Here are some examples of what can be done with this module:

### 1. Getting the Protocol and Authority from a URL

```python
import urllib.parse

# Define a URL
url = "https://www.example.com/path?query=param"

# Parse the URL into its components
parsed_url = urllib.parse.urlparse(url)

# Print the protocol and authority
print(f"Protocol: {parsed_url.scheme}")  # Output: https
print(f"Authority: {parsed_url.netloc}")  # Output: www.example.com
```

### 2. Parsing a URL without Authority

```python
import urllib.parse

# Define a URL without authority (i.e., just the path and query)
url = "/path/to/resource?query=param"

# Parse the URL into its components
parsed_url = urllib.parse.urlparse(url)

# Print the path and query
print(f"Path: {parsed_url.path}")  # Output: /path/to/resource
print(f"Query: {parsed_url.query}")  # Output: query=param
```

### 3. Unpacking a URL into its Components

```python
import urllib.parse

# Define a URL
url = "https://www.example.com/path?query=param"

# Parse the URL into its components and unpack them into variables
scheme, netloc, path, params, query, fragment = urllib.parse.urlparse(url)

print(f"Scheme: {scheme}")  # Output: https
print(f"Netloc: {netloc}")  # Output: www.example.com
print(f"path: {path}")    # Output: /path/to/resource
```

### 4. Encoding and Decoding URLs

```python
import urllib.parse

# Define a URL with query parameters
url = "https://www.example.com/path?query=param"

# Encode the query parameters
encoded_query = urllib.parse.urlencode({"param": "value"})

# Create a new URL with the encoded query parameters
new_url = f"{url}?{encoded_query}"

print(new_url)  # Output: https://www.example.com/path?query=param&param=value

# Decode the query parameters
decoded_query = urllib.parse.parse_qs(url)[0]

print(decoded_query["param"])  # Output: value
```

### 5. Creating a New URL from Components

```python
import urllib.parse

# Define components of a new URL
scheme = "http"
netloc = "example.com"
path = "/new/path"
query = "new=query"
fragment = "#anchor"

# Create a new URL from its components
new_url = f"{scheme}://{netloc}{path}?{query}{fragment}"

print(new_url)  # Output: http://example.com/new/path?new=query#anchor
```

### 6. Unpacking the Parse Result Object

```python
import urllib.parse

# Define a URL
url = "https://www.example.com/path?query=param"

# Parse the URL into its components
parsed_url = urllib.parse.urlparse(url)

# Unpack the parsed result object into variables
scheme, netloc, path, query, fragment = parsed_url

print(f"Scheme: {scheme}")  # Output: https
print(f"Netloc: {netloc}")  # Output: www.example.com
print(f"path: {path}")    # Output: /path/to/resource
```

### 7. Creating a Parse Result Object from Components

```python
import urllib.parse

# Define components of a new URL
scheme = "https"
netloc = "www.example.com"
path = "/new/path"
params = ""
query = "new=query"
fragment = "#anchor"

# Create a parse result object from its components
parsed_url = urllib.parse.urlparse(scheme, netloc, path, params, query, fragment)

print(parsed_url)  # Output: ParseResult(scheme='https', netloc='www.example.com', path='/new/path', params='', query='new=query', fragment='#anchor')
```

### 8. Creating a URL from a String

```python
import urllib.parse

# Define a string representation of a URL
url_str = "https://www.example.com/path?query=param"

# Create a parse result object from the string
parsed_url = urllib.parse.urlparse(url_str)

print(parsed_url)  # Output: ParseResult(scheme='https', netloc='www.example.com', path='/path/to/resource', params='', query='query=param', fragment='')
```

### 9. Creating a URL with a File Path

```python
import urllib.parse

# Define a file path
file_path = "/home/user/file.txt"

# Create a parse result object from the file path
parsed_url = urllib.parse.urlparse(file_path)

print(parsed_url)  # Output: ParseResult(scheme='', netloc='', path='/home/user/file.txt', params='', query='', fragment='')
```

### 10. Creating a URL with a Path

```python
import urllib.parse

# Define a file name
file_name = "example.txt"

# Create a parse result object from the file name
parsed_url = urllib.parse.urlparse(f"/{file_name}")

print(parsed_url)  # Output: ParseResult(scheme='', netloc='', path='/path/to/example.txt', params='', query='', fragment='')
```
