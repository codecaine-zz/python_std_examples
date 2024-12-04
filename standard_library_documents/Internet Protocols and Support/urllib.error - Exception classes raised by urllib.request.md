# urllib.error - Exception classes raised by urllib.request

The `urllib.error` module contains a set of exception classes that are raised by the `urllib.request` module when an error occurs during HTTP request processing, such as failed connections or invalid responses. Below are comprehensive code examples for each exception class in this module:

```python
import urllib.request

# Example 1: URLError
try:
    # Attempt to open a URL that does not exist (this will raise an error)
    response = urllib.request.urlopen("https://nonexistent-url.com")
except urllib.error.URLError as e:
    print(f"URLError occurred: {e.reason}")

# Explanation:
# URLError is raised when there was an error during the actual HTTP request.
# It can be caused by network issues, invalid URLs, or other problems with the connection.

# Example 2: HTTPError
try:
    # Attempt to open a URL that returns an error status code (e.g., 404 Not Found)
    response = urllib.request.urlopen("https://www.example.com/does-not-exist")
except urllib.error.HTTPError as e:
    print(f"HTTPError occurred with status {e.code}: {e.reason}")

# Explanation:
# HTTPError is raised when the server responds with an error status code.
# It contains information about the specific error, including the status code and a reason message.

# Example 3: ContentTooLongError
try:
    # Attempt to open a URL that returns a very large response (e.g., over a specified limit)
    response = urllib.request.urlopen("https://example.com/large-file")
except urllib.error.ContentTooLongError as e:
    print(f"ContentTooLongError occurred with length {e.length}: {e.message}")

# Explanation:
# ContentTooLongError is raised when the server sends back a response that exceeds a specified maximum size.
# It provides details about the content length and an optional message.

# Example 4: ReadTimeoutError
try:
    # Attempt to open a URL with a read timeout (e.g., more than 5 seconds)
    urllib.request.urlopen("https://example.com", timeout=5)
except urllib.error.ReadTimeoutError as e:
    print(f"ReadTimeoutError occurred after {e.timeout} seconds: {e.reason}")

# Explanation:
# ReadTimeoutError is raised when the connection to the server times out before the request can complete.
# It includes the timeout duration and a reason message.

# Example 5: FTPError
try:
    # Attempt to open an FTP URL (this will raise an error)
    urllib.request.urlopen("ftp://example.com")
except urllib.error.FTPError as e:
    print(f"FTPError occurred: {e.reason}")

# Explanation:
# FTPError is raised when there was an error during the FTP request.
# It can be caused by network issues or invalid FTP URLs.

# Example 6: SocketError
try:
    # Attempt to open a URL that requires a proxy (this will raise an error)
    proxy = urllib.request.ProxyHandler({'http': 'http://proxy.example.com'})
    opener = urllib.request.build_opener(proxy)
    response = opener.open("http://example.com")
except urllib.error.SocketError as e:
    print(f"SocketError occurred: {e.strerror}")

# Explanation:
# SocketError is raised when there was an error establishing a socket connection.
# It includes the error message, which can be useful for debugging network issues.

# Example 7: IncompleteRead
try:
    # Attempt to open a URL and read only part of the content (this will raise an error)
    response = urllib.request.urlopen("https://example.com/large-file")
    data = response.read(1024)  # Read only 1024 bytes
except urllib.error.IncompleteRead as e:
    print(f"IncompleteRead occurred: {e.partial} out of {e.length} expected")

# Explanation:
# IncompleteRead is raised when the server sends a partial response, and the client expects a full one.
# It includes the amount of data read so far and the total expected length.

# Example 8: HTTPError with custom message
try:
    # Attempt to open a URL that returns an error status code (e.g., 403 Forbidden)
    response = urllib.request.urlopen("https://www.example.com/forbidden")
except urllib.error.HTTPError as e:
    print(f"HTTPError occurred with status {e.code}: {e.reason}")
    custom_message = "Access denied"
    if str(e) != custom_message:
        raise urllib.error.HTTPError(e.url, e.code, custom_message, None, e.hdrs)

# Explanation:
# Custom error messages can be added to HTTPError by creating a new exception instance.
# This allows for more detailed error handling and logging.

# Example 9: URLError with custom message
try:
    # Attempt to open a URL that does not exist (this will raise an error)
    response = urllib.request.urlopen("https://nonexistent-url.com")
except urllib.error.URLError as e:
    print(f"URLError occurred: {e.reason}")
    custom_message = "URL not found"
    if str(e) != custom_message:
        raise urllib.error.URLError(custom_message)

# Explanation:
# Custom error messages can be added to URLError by creating a new exception instance.
# This allows for more detailed error handling and logging.

# Example 10: ContentTooLongError with custom message
try:
    # Attempt to open a URL that returns a very large response (e.g., over a specified limit)
    response = urllib.request.urlopen("https://example.com/large-file")
except urllib.error.ContentTooLongError as e:
    print(f"ContentTooLongError occurred with length {e.length}: {e.message}")
    custom_message = "File too large"
    if str(e) != custom_message:
        raise urllib.error.ContentTooLongError(e.url, e.code, custom_message, None, e.hdrs)

# Explanation:
# Custom error messages can be added to ContentTooLongError by creating a new exception instance.
# This allows for more detailed error handling and logging.

```

These examples demonstrate how to handle various exceptions that might occur when using the `urllib.request` module. Each example includes comments explaining the purpose of the code, what exceptions are handled, and how custom messages can be added to improve error reporting. These examples are suitable for inclusion in official documentation or as a reference guide for developers working with Python's standard library networking utilities.
