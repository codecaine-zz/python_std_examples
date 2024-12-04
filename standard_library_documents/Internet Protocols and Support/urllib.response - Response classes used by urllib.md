# urllib.response — Response classes used by urllib

Here's an example of how you can use the `Response` class from the `urllib` module.

```python
import urllib.request
from urllib.parse import urljoin, urlparse
from urllib.error import HTTPError, URLError

# Creating a URL object
url = "http://example.com"

# Using urljoin to join a relative URL with a base URL
relative_url = "/path/to/resource"
base_url = urljoin(url, relative_url)
print(base_url)  # Output: http://example.com/path/to/resource

# Parsing a URL using urlparse
parsed_url = urlparse(url)
print(parsed_url.scheme)  # Output: http
print(parsed_url.netloc)  # Output: example.com
print(parsed_url.path)    # Output: /path/to/resource

# Creating an HTTP request object
request = urllib.request.Request(url, data=b"Hello, World!", headers={"Content-Type": "text/plain"})

# Sending the request and getting a response
response = urllib.request.urlopen(request)

# Checking if the request was successful
if response.status == 200:
    print("Request successful")
else:
    print(f"Request failed with status code {response.status}")

# Getting the headers of the response
headers = response.headers
for key, value in headers.items():
    print(f"{key}: {value}")

# Getting the content of the response
content = response.read()
print(content.decode("utf-8"))

# Checking if the request was an exception (e.g. due to a network error)
try:
    response.raise_for_status()  # Raise an HTTPError for 4xx/5xx status codes
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e}")
except urllib.error.URLError as e:
    print(f"URL Error: {e}")

# Closing the response object to free up system resources
response.close()
```

Here's an example of a class that demonstrates some of these features:

```python
import urllib.request

class MyURLEncoder:
    def __init__(self, url):
        self.url = url

    def get_absolute_url(self):
        return urllib.request.urljoin(self.url, "/path/to/resource")

    def parse_url(self):
        parsed_url = urllib.request.urlparse(self.url)
        print(f"S scheme: {parsed_url.scheme}")
        print(f"Netloc: {parsed_url.netloc}")
        print(f"Path: {parsed_url.path}")

    def send_request(self):
        request = urllib.request.Request(self.url, data=b"Hello, World!", headers={"Content-Type": "text/plain"})
        response = urllib.request.urlopen(request)
        return response

# Example usage:
encoder = MyURLEncoder("http://example.com")
print(encoder.get_absolute_url())
encoder.parse_url()
response = encoder.send_request()
if response.status == 200:
    print("Request successful")
else:
    print(f"Request failed with status code {response.status}")
```

Here's an example of a class that demonstrates error handling:

```python
import urllib.request

class MyURLErrorHandler:
    def __init__(self, url):
        self.url = url

    def handle_response(self, response):
        try:
            response.raise_for_status()
        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e}")
        except urllib.error.URLError as e:
            print(f"URL Error: {e}")

# Example usage:
handler = MyURLErrorHandler("http://example.com")
response = handler.handle_response(urllib.request.urlopen("http://example.com"))
if response.status == 200:
    print("Request successful")
else:
    print(f"Request failed with status code {response.status}")
```

Note that in all cases, error handling is key. You should always check the status of a request and handle any exceptions that may occur.

Also note that `urllib` is not as powerful or flexible as other libraries for making HTTP requests, like `requests`. However, it's often useful when you need to manually create HTTP requests and responses.
