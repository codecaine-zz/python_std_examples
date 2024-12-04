# http.cookies - HTTP state management

The `http.cookies` module in Python provides a way to handle cookies sent by a client's browser, which are used for maintaining user sessions or storing data across multiple requests. Below are comprehensive and well-documented code examples for various functionalities of the `http.cookies` module.

### Example 1: Creating a Simple Cookie

```python
from http.cookies import SimpleCookie

# Create an instance of SimpleCookie to handle cookies
cookie = SimpleCookie()

# Set a cookie with a name, value, and expiration time
cookie['session_id'] = 'abc123'
cookie['session_id']['expires'] = 60 * 60 * 24  # Expires in one day

# Print the cookie as a string
print(cookie.output())
```

### Example 2: Parsing a Cookie String

```python
from http.cookies import SimpleCookie

# A sample cookie string from a browser
cookie_string = 'session_id=abc123; expires=Wed, 01 Jan 2099 00:00:00 GMT'

# Parse the cookie string into a dictionary of cookies
cookies = SimpleCookie(cookie_string)

# Access and print the value of the session_id cookie
print(cookies['session_id'].value)
```

### Example 3: Setting Multiple Cookies

```python
from http.cookies import SimpleCookie

# Create an instance of SimpleCookie to handle multiple cookies
cookie = SimpleCookie()

# Set multiple cookies with different names, values, and domains
cookie['user'] = 'john_doe'
cookie['user']['domain'] = '.example.com'

cookie['age'] = 30
cookie['age']['path'] = '/admin'

print(cookie.output())
```

### Example 4: Handling Cookie Expiry

```python
from http.cookies import SimpleCookie, CookieError

# Create an instance of SimpleCookie to handle cookies with expiration
cookie = SimpleCookie()

# Set a cookie with a name, value, and a specific expiry date
try:
    cookie['session_id'] = 'abc123'
    cookie['session_id']['expires'] = 60 * 60 * 24  # Expires in one day

    # Attempt to retrieve the expired cookie
    print(cookie['session_id'].value)
except CookieError as e:
    print(f"Cookie error: {e}")
```

### Example 5: Setting Cookies with Secure and HttpOnly Flags

```python
from http.cookies import SimpleCookie

# Create an instance of SimpleCookie to handle cookies with security flags
cookie = SimpleCookie()

# Set a cookie with secure flag (HTTPS only)
cookie['secure_cookie'] = 'value'
cookie['secure_cookie']['secure'] = True

# Set a cookie with HttpOnly flag (not accessible via JavaScript)
cookie['http_only_cookie'] = 'secret'
cookie['http_only_cookie']['httponly'] = True

print(cookie.output())
```

### Example 6: Encoding and Decoding Cookies

```python
from http.cookies import SimpleCookie, CookieError

# Create an instance of SimpleCookie to handle cookies for encoding/decoding
cookie = SimpleCookie()

# Set a cookie with a value containing special characters
cookie['special_chars'] = 'Hello, World!'
print(cookie.output())

# Decode the encoded cookie string back into a dictionary
decoded_cookie = SimpleCookie()
try:
    decoded_cookie.load(cookie.output())
    print(decoded_cookie['special_chars'].value)
except CookieError as e:
    print(f"Decoding error: {e}")
```

### Example 7: Using Cookies in HTTP Responses

```python
from http.cookies import SimpleCookie, Morsel

# Create an instance of SimpleCookie to handle cookies for HTTP responses
response_cookie = SimpleCookie()

# Set a cookie with a name, value, and domain for use in an HTTP response
response_cookie['session_id'] = 'abc123'
response_cookie['session_id']['domain'] = '.example.com'

# Add the cookie to the response headers
headers = {'Set-Cookie': response_cookie.output(header='', sep='')}
print(headers)
```

### Example 8: Using Cookies in HTTP Requests

```python
from http.cookies import SimpleCookie, Morsel

# Create an instance of SimpleCookie to handle cookies for HTTP requests
request_cookies = SimpleCookie()

# Set a cookie with a name, value, and domain for use in an HTTP request
request_cookies['session_id'] = 'abc123'
request_cookies['session_id']['domain'] = '.example.com'

# Decode the cookie string from the HTTP request header into a dictionary
try:
    decoded_request_cookies = SimpleCookie()
    decoded_request_cookies.load(request_cookies.output(header='', sep=''))
    print(decoded_request_cookies['session_id'].value)
except CookieError as e:
    print(f"Decoding error: {e}")
```

### Example 9: Handling SameSite Attribute

```python
from http.cookies import SimpleCookie, Morsel

# Create an instance of SimpleCookie to handle cookies with SameSite attribute
cookie = SimpleCookie()

# Set a cookie with SameSite=Lax attribute (recommended for cross-site requests)
cookie['lax_cookie'] = 'value'
cookie['lax_cookie']['samesite'] = 'Lax'

# Print the cookie with the SameSite attribute
print(cookie.output())
```

### Example 10: Setting Cookies in a Web Server Response

```python
from http.cookies import SimpleCookie, Morsel

# Create an instance of SimpleCookie to handle cookies for web server responses
response_cookie = SimpleCookie()

# Set a cookie with a name, value, and domain for use in a web server response
response_cookie['session_id'] = 'abc123'
response_cookie['session_id']['domain'] = '.example.com'

# Add the cookie to the response headers
headers = {'Set-Cookie': response_cookie.output(header='', sep='')}
print(headers)
```

These examples cover various aspects of using the `http.cookies` module, including creating and parsing cookies, setting multiple cookies with different attributes, handling expiry dates, and managing security flags. Each example includes comments to explain the purpose and functionality of each part of the code.
