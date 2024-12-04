# urllib.request - Extensible library for opening URLs

The `urllib.request` module in Python provides a robust set of tools for making HTTP requests and handling various protocols, including file:// and http/https. Below are comprehensive code examples that demonstrate common use cases for this module, including how to open URLs, handle responses, manage cookies, and make POST requests.

### 1. Opening a URL

```python
import urllib.request

# Example: Open a URL and print the response content
url = 'http://example.com'
response = urllib.request.urlopen(url)

# Read and decode the response content
content = response.read().decode('utf-8')

print(content)
```

### 2. Handling Cookies

```python
import urllib.request

# Example: Open a URL and handle cookies
req = urllib.request.Request('http://example.com')
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
response = opener.open(req)

# Read and decode the response content
content = response.read().decode('utf-8')

print(content)
```

### 3. Making a POST Request

```python
import urllib.request
import urllib.parse

# Example: Make a POST request with data
url = 'http://example.com/api/data'
data = {'key1': 'value1', 'key2': 'value2'}
encoded_data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, encoded_data)
response = urllib.request.urlopen(req)

# Read and decode the response content
content = response.read().decode('utf-8')

print(content)
```

### 4. Using a Timeout

```python
import urllib.request

# Example: Set a timeout for opening a URL
url = 'http://example.com'
try:
    with urllib.request.urlopen(url, timeout=5) as response:
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print(f"Server error: {e.reason}")
    elif hasattr(e, 'code'):
        print(f"HTTP error code: {e.code}")
```

### 5. Handling Redirects

```python
import urllib.request

# Example: Follow redirects when opening a URL
url = 'http://example.com/redirect'
response = urllib.request.urlopen(url)

# Read and decode the response content
content = response.read().decode('utf-8')

print(content)
```

### 6. Using a User-Agent

```python
import urllib.request

# Example: Use a custom user-agent when opening a URL
url = 'http://example.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
req = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(req)

# Read and decode the response content
content = response.read().decode('utf-8')

print(content)
```

### 7. Handling HTTP Errors

```python
import urllib.request

# Example: Handle HTTP errors when opening a URL
url = 'http://example.com/404'
try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.HTTPError as e:
    print(f"HTTP error code: {e.code}")
```

### 8. Writing to a Local File

```python
import urllib.request

# Example: Write the contents of a URL to a local file
url = 'http://example.com'
filename = 'output.txt'

with urllib.request.urlopen(url) as response:
    with open(filename, 'wb') as file:
        file.write(response.read())

print(f"Data written to {filename}")
```

### 9. Using Proxy

```python
import urllib.request

# Example: Use a proxy when opening a URL
proxy_url = 'http://127.0.0.1:8080'
proxies = {'http': proxy_url, 'https': proxy_url}
opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
response = opener.open('http://example.com')

# Read and decode the response content
content = response.read().decode('utf-8')

print(content)
```

### 10. Using HTTPS

```python
import urllib.request

# Example: Open a URL over HTTPS
url = 'https://example.com'
response = urllib.request.urlopen(url)

# Read and decode the response content
content = response.read().decode('utf-8')

print(content)
```

These examples cover various aspects of using `urllib.request`, providing a comprehensive guide to opening URLs, handling responses, managing cookies, making POST requests, and more. Each example includes comments to explain each step and is suitable for inclusion in official documentation.
