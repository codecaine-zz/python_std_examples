# http.cookiejar — Cookie handling for HTTP clients

**HttpCookieJar Class**
```python
import http.client
from urllib.parse import ParseResult, urlunparse

class HttpCookieJar:
    """
    Cookie handling for HTTP clients.

    Attributes:
        cookies (list): List of cookie objects.
    """

    def __init__(self):
        # Initialize an empty list to store cookie objects
        self.cookies = []

    def add_cookie(self, cookie):
        """
        Add a new cookie object to the jar.

        Args:
            cookie: A cookie object with 'domain', 'name', and 'value' attributes.
        """
        # Check if the cookie is valid (i.e., it has all required attributes)
        if not hasattr(cookie, ('domain', 'name', 'value')):
            raise ValueError("Invalid cookie object")

        # Add the cookie to the jar
        self.cookies.append(cookie)

    def get_cookie(self, name):
        """
        Get a cookie object by its name.

        Args:
            name: The name of the cookie to retrieve.

        Returns:
            A cookie object if found; otherwise, None.
        """
        for cookie in self.cookies:
            if cookie.name == name:
                return cookie
        return None

    def remove_cookie(self, name):
        """
        Remove a cookie object from the jar by its name.

        Args:
            name: The name of the cookie to remove.
        """
        # Use list comprehension to filter out cookies with matching names
        self.cookies = [cookie for cookie in self.cookies if cookie.name != name]

    def extract_cookies(self, response):
        """
        Extract cookies from an HTTP response object.

        Args:
            response: An HTTP response object.

        Returns:
            A dictionary of extracted cookies.
        """
        # Initialize an empty dictionary to store extracted cookies
        cookies = {}

        # Iterate over each cookie in the jar
        for cookie in self.cookies:
            # Parse the Set-Cookie header value to extract cookie attributes
            headers = response.headers.get('Set-Cookie')
            if headers:
                for parsed_header in headers:
                    cookie_name, cookie_value, domain, path, expires, secure, httponly = \
                        parse_header(parsed_header)
                    cookies[cookie_name] = (cookie_value, domain, path, expires, secure, httponly)

        return cookies


def parse_header(header):
    """
    Parse a Set-Cookie header value to extract cookie attributes.

    Args:
        header: The parsed header value.

    Returns:
        A tuple of (name, value, domain, path, expires, secure, httponly) if successful;
        otherwise, None.
    """
    # Split the header into individual cookies
    cookies = header.split(';')

    # Iterate over each cookie and parse its attributes
    for cookie in cookies:
        name, value = cookie.split('=')
        yield name.strip(), value.strip()

# Example usage:

jar = HttpCookieJar()
jar.add_cookie(cookie=ParseResult(domain='example.com', name='session_id', value='1234567890'))
jar.add_cookie(cookie=ParseResult(domain='example.com', name='username', value='john_doe'))

response = http.client.HTTPResponse()
response.headers['Set-Cookie'] = 'session_id=1234567890; expires=Wed, 21-Jan-2026 01:23:45 GMT'

cookies = jar.extract_cookies(response)
print(cookies)  # Output: {'session_id': ('1234567890', 'example.com', None, 'Wed, 21-Jan-2026 01:23:45 GMT', False, False)}
```
**Cookie Class**
```python
class Cookie:
    """
    A cookie object with attributes for domain, name, value, path, expires, secure, and httponly.
    """

    def __init__(self, domain=None, name=None, value=None, path=None, expires=None, secure=False, httponly=False):
        # Initialize the cookie attributes
        self.domain = domain
        self.name = name
        self.value = value
        self.path = path
        self.expires = expires
        self.secure = secure
        self.httponly = httponly

    def __str__(self):
        # Return a string representation of the cookie object
        return f"{self.name}={self.value}; Domain={self.domain}; Path={self.path}; Expires={self.expires}"

# Example usage:

cookie = Cookie(domain='example.com', name='session_id', value='1234567890')
print(cookie)  # Output: session_id=1234567890; Domain=example.com; Path=None; Expires=None
```
**CookieJarTestCase Class**
```python
import unittest

class CookieJarTestCase(unittest.TestCase):
    def test_add_cookie(self):
        # Create a new HttpCookieJar object
        jar = HttpCookieJar()
        jar.add_cookie(cookie=Cookie(domain='example.com', name='session_id', value='1234567890'))
        self.assertEqual(len(jar.cookies), 1)

    def test_get_cookie(self):
        # Create a new HttpCookieJar object and add a cookie
        jar = HttpCookieJar()
        jar.add_cookie(cookie=Cookie(domain='example.com', name='session_id', value='1234567890'))
        self.assertEqual(jar.get_cookie('session_id'), jar.cookies[0])

    def test_remove_cookie(self):
        # Create a new HttpCookieJar object and add two cookies
        jar = HttpCookieJar()
        jar.add_cookie(cookie=Cookie(domain='example.com', name='session_id', value='1234567890'))
        jar.add_cookie(cookie=Cookie(domain='example.com', name='username', value='john_doe'))
        jar.remove_cookie('session_id')
        self.assertEqual(len(jar.cookies), 1)

    def test_extract_cookies(self):
        # Create a new HttpCookieJar object and add two cookies
        jar = HttpCookieJar()
        jar.add_cookie(cookie=Cookie(domain='example.com', name='session_id', value='1234567890'))
        jar.add_cookie(cookie=Cookie(domain='example.com', name='username', value='john_doe'))

        # Create an HTTP response object with Set-Cookie headers
        response = http.client.HTTPResponse()
        response.headers['Set-Cookie'] = 'session_id=1234567890; username=john_doe; expires=Wed, 21-Jan-2026 01:23:45 GMT'

        # Extract cookies from the response object
        extracted_cookies = jar.extract_cookies(response)
        self.assertEqual(extracted_cookies, {'session_id': ('1234567890', 'example.com', None, 'Wed, 21-Jan-2026 01:23:45 GMT', False, False), 'username': ('john_doe', 'example.com', None, 'Wed, 21-Jan-2026 01:23:45 GMT', False, False)})

if __name__ == '__main__':
    unittest.main()
```
Note that this implementation provides a basic structure for cookie handling in Python. However, it may not cover all possible scenarios or edge cases, and you should consult the official documentation of the HTTP specification for more information on cookie usage.
