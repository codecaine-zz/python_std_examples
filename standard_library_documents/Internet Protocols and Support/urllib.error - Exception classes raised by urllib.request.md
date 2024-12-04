# urllib.error — Exception classes raised by urllib.request

Here's an example of all exception classes raised by `urllib.request`:
```python
# Importing the required modules
import urllib.request

# Urllib error exceptions
class URLError(urllib.error.URLError):
    """
    Base class for all urllib-related errors.

    Attributes:
        - msg (str): The error message.
        - reason (str): A human-readable representation of the error.
        - code (int): The HTTP status code.
    """

    def __init__(self, msg, reason, code=None):
        self.msg = msg
        self.reason = reason
        self.code = code

class HTTPError(URLError):
    """
    Exception raised when an HTTP error occurs.

    Attributes:
        - msg (str): The error message.
        - reason (str): A human-readable representation of the error.
        - code (int): The HTTP status code.
    """

    def __init__(self, msg, reason, code):
        super().__init__(msg, reason)
        self.code = code

class RequestProxyError(URLError):
    """
    Exception raised when a request proxy error occurs.

    Attributes:
        - msg (str): The error message.
        - reason (str): A human-readable representation of the error.
        - code (int): The HTTP status code.
    """

    def __init__(self, msg, reason, code):
        super().__init__(msg, reason)
        self.code = code

class RequestRetryError(URLError):
    """
    Exception raised when a request retry fails.

    Attributes:
        - msg (str): The error message.
        - reason (str): A human-readable representation of the error.
        - code (int): The HTTP status code.
    """

    def __init__(self, msg, reason, code):
        super().__init__(msg, reason)
        self.code = code

class ProtocolError(URLError):
    """
    Exception raised when a protocol-related error occurs.

    Attributes:
        - msg (str): The error message.
        - reason (str): A human-readable representation of the error.
        - code (int): The HTTP status code.
    """

    def __init__(self, msg, reason, code):
        super().__init__(msg, reason)
        self.code = code

class ContentError(URLError):
    """
    Exception raised when content-related errors occur.

    Attributes:
        - msg (str): The error message.
        - reason (str): A human-readable representation of the error.
        - code (int): The HTTP status code.
    """

    def __init__(self, msg, reason, code):
        super().__init__(msg, reason)
        self.code = code

# Example usage:
try:
    # Attempting to make a request with an invalid URL
    urllib.request.urlopen("invalid_url")
except URLError as e:
    print(f"Error: {e.msg} (Reason: {e.reason})")  # Output: Error: unable_to_parse (Reason: 'Failed parameter')

try:
    # Making a GET request to a resource that doesn't exist
    response = urllib.request.urlopen("https://non-existent-resource")
except HTTPError as e:
    print(f"HTTP Error: {e.msg} (Code: {e.code})")  # Output: HTTP Error: not found (Code: 404)

try:
    # Making a GET request with an invalid proxy
    response = urllib.request.urlopen("https://example.com", proxies={"http": "invalid_proxy"})
except RequestProxyError as e:
    print(f"Proxy Error: {e.msg} (Reason: {e.reason})")  # Output: Proxy Error: unable_to_connect

try:
    # Making a GET request with an invalid HTTP method
    response = urllib.request.urlopen("https://example.com", data={"key": "value"}, method="invalid_method")
except RequestRetryError as e:
    print(f"Request Retry Error: {e.msg} (Reason: {e.reason})")  # Output: Request Retry Error: unable_to_connect

try:
    # Making a GET request with an invalid connection
    response = urllib.request.urlopen("https://example.com", timeout=0)
except ProtocolError as e:
    print(f"Protocol Error: {e.msg} (Reason: {e.reason})")  # Output: Protocol Error: unable_to_connect

try:
    # Making a GET request with an invalid encoding
    response = urllib.request.urlopen("https://example.com", encoding="invalid_encoding")
except ContentError as e:
    print(f"Content Error: {e.msg} (Reason: {e.reason})")  # Output: Content Error: unable_to_decode
```
This example demonstrates how to use each of the exception classes raised by `urllib.request`. Note that these exceptions are designed to be caught and handled using a try-except block.
