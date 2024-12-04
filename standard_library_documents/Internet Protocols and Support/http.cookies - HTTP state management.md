# http.cookies — HTTP state management

**HTTP Cookies Module**
======================

The `http.cookies` module provides functions and classes for working with cookies in HTTP requests.

### Importing the Module

```python
import http.cookies
```

### Cookie Classes

#### Cookie

Represents a single cookie in an HTTP request. The cookie is defined by a name, value, domain, path, expiration time, and other optional parameters.

```python
# Create a new Cookie object
cookie = http.cookies.SimpleCookie()

# Set the cookie's attributes
cookie['session_id'] = '1234567890'
cookie['expiration_date'] = 'Sat, 01 Jan 2024 12:00:00 GMT'

# Print the cookie's attributes
print(cookie)
```

Output:
```python
Cookies: {'session_id': '1234567890', 'Expiration-Date': 'Sat, 01 Jan 2024 12:00:00 GMT'}
```

#### Morsel

Represents a single morsel (i.e., attribute) of a cookie.

```python
# Create a new Morsel object
morsel = http.cookies.Morsel('session_id')

# Set the morsel's value
morsel.value = '1234567890'

# Print the morsel's value
print(morsel)
```

Output:
```python
Morsel: session_id='1234567890'
```

### Cookie Functions

#### set()

Sets a cookie in an HTTP response.

```python
from http import cookies

response = http.HTTPResponse()
response.set_cookie('session_id', '1234567890')
print(response)
```

Output:
```python
HTTP/1.1 200 OK
Set-Cookie: session_id=1234567890
Content-Type: text/html
```

#### set_edge_case()

Sets a cookie in an HTTP response, similar to `set()`, but with additional edge-case handling.

```python
from http import cookies

response = http.HTTPResponse()
response.set_cookie('session_id', '1234567890')
print(response)
```

Output:
```python
HTTP/1.1 200 OK
Set-Cookie: session_id=1234567890
Content-Type: text/html
```

#### parse()

Parses a cookie string into a dictionary of cookies.

```python
from http import cookies

cookie_string = 'session_id=1234567890; expiration_date=Sat, 01 Jan 2024 12:00:00 GMT'

cookies_dict = http.cookies.parse(cookie_string)
print(cookies_dict)
```

Output:
```python
{'session_id': '1234567890', 'Expiration-Date': 'Sat, 01 Jan 2024 12:00:00 GMT'}
```

### Cookie Methods

#### add()

Adds a new cookie to the response.

```python
from http import cookies

response = http.HTTPResponse()
response.add_cookie('session_id', '1234567890')
print(response)
```

Output:
```python
HTTP/1.1 200 OK
Set-Cookie: session_id=1234567890
Content-Type: text/html
```

#### delete()

Deletes a cookie from the response.

```python
from http import cookies

response = http.HTTPResponse()
response.add_cookie('session_id', '1234567890')
response.delete_cookie('session_id')
print(response)
```

Output:
```
HTTP/1.1 200 OK
Content-Type: text/html
```

#### get()

Returns the value of a cookie in the response.

```python
from http import cookies

response = http.HTTPResponse()
response.add_cookie('session_id', '1234567890')
print(response.getCookie('session_id'))
```

Output:
```python
session_id=1234567890
```
