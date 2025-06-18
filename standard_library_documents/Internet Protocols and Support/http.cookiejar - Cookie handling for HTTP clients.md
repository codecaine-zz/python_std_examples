# http.cookiejar - Cookie handling for HTTP clients
## Table of Contents

1. [1. Basic Cookie Management](#1-basic-cookie-management)
2. [2. Parsing HTTP Responses for Cookies](#2-parsing-http-responses-for-cookies)
3. [3. Sending Cookies with HTTP Requests](#3-sending-cookies-with-http-requests)
4. [4. Handling Cookie Expiry](#4-handling-cookie-expiry)
5. [5. Handling Cookie Domain Scope](#5-handling-cookie-domain-scope)
6. [6. Handling Cookie Persistence](#6-handling-cookie-persistence)
7. [7. Handling Secure Cookies](#7-handling-secure-cookies)



The `http.cookiejar` module is part of Python's standard library and provides a way to handle cookies in HTTP requests. Cookies are used by websites to store user data, such as session IDs or preferences, between visits. This module allows you to manage cookie storage, parsing responses, and sending cookies with HTTP requests.

Below are comprehensive code examples for various functionalities provided by the `http.cookiejar` module:

### 1. Basic Cookie Management

```python
import http.cookiejar

# Create a CookieJar object
cookie_jar = http.cookiejar.CookieJar()

# Example of adding a cookie manually
cookie = http.cookiejar.Cookie(
    version=0,
    name='session_id',
    value='1234567890',
    domain='example.com',
    path='/',
    secure=True,
    expires=1632400000  # Unix timestamp for January 1, 2021
)

cookie_jar.set_cookie(cookie)

# Print all cookies in the CookieJar
for cookie in cookie_jar:
    print(f"Name: {cookie.name}, Value: {cookie.value}")

# Save cookies to a file
with open('cookies.txt', 'wb') as f:
    cookie_jar.save(file=f, ignore_discard=True, ignore_expires=False)

# Load cookies from a file
cookie_jar.clear()
cookie_jar.load('cookies.txt')

# Add another cookie from the loaded data
another_cookie = http.cookiejar.Cookie.from_string(
    "anotherCookieName=9876543210; expires=1635000000"
)
cookie_jar.set_cookie(another_cookie)

print("\nCookies after loading and adding another:")
for cookie in cookie_jar:
    print(f"Name: {cookie.name}, Value: {cookie.value}")
```

### 2. Parsing HTTP Responses for Cookies

```python
import http.cookiejar
import urllib.request

# Create a CookieJar object
cookie_jar = http.cookiejar.CookieJar()

# Open a URL and handle cookies
with urllib.request.urlopen('https://example.com') as response:
    # Parse the response headers to extract cookies
    cookie_jar.extract_cookies(response, 'https://example.com')

# Print all cookies extracted from the response
for cookie in cookie_jar:
    print(f"Name: {cookie.name}, Value: {cookie.value}")
```

### 3. Sending Cookies with HTTP Requests

```python
import http.cookiejar
import urllib.request

# Create a CookieJar object
cookie_jar = http.cookiejar.CookieJar()

# Open a URL and handle cookies
with urllib.request.urlopen('https://example.com') as response:
    # Parse the response headers to extract cookies
    cookie_jar.extract_cookies(response, 'https://example.com')

# Create an opener that uses our CookieJar
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

# Make a request using the custom opener
with opener.open('https://example.com/some_page') as response:
    print("Response from secured page:")
    print(response.read().decode())

# Note: The URL 'https://example.com' and '/some_page' should be replaced with actual URLs used in your application.
```

### 4. Handling Cookie Expiry

```python
import http.cookiejar
import time

# Create a CookieJar object
cookie_jar = http.cookiejar.CookieJar()

# Example of setting cookies with different expiry times
cookie1 = http.cookiejar.Cookie(
    version=0,
    name='session_id',
    value='1234567890',
    domain='example.com',
    path='/',
    secure=True,
    expires=int(time.time() + 3600)  # Expires in 1 hour
)

cookie2 = http.cookiejar.Cookie(
    version=0,
    name='session_id',
    value='9876543210',
    domain='example.com',
    path='/',
    secure=True,
    expires=int(time.time() - 3600)  # Expires in 1 hour ago
)

cookie_jar.set_cookie(cookie1)
cookie_jar.set_cookie(cookie2)

# Print all cookies, showing expiry times
for cookie in cookie_jar:
    print(f"Name: {cookie.name}, Value: {cookie.value}, Expires: {cookie.expires}")
```

### 5. Handling Cookie Domain Scope

```python
import http.cookiejar

# Create a CookieJar object
cookie_jar = http.cookiejar.CookieJar()

# Example of setting cookies with different domain scopes
cookie1 = http.cookiejar.Cookie(
    version=0,
    name='session_id',
    value='1234567890',
    domain='example.com',
    path='/',
    secure=True
)

cookie2 = http.cookiejar.Cookie(
    version=0,
    name='session_id',
    value='9876543210',
    domain='.example.com',  # Matches subdomains
    path='/',
    secure=True
)

cookie_jar.set_cookie(cookie1)
cookie_jar.set_cookie(cookie2)

# Print all cookies, showing domain scope
for cookie in cookie_jar:
    print(f"Name: {cookie.name}, Value: {cookie.value}, Domain: {cookie.domain}")
```

### 6. Handling Cookie Persistence

```python
import http.cookiejar
import os

# Create a CookieJar object
cookie_jar = http.cookiejar.MozillaCookieJar()  # Use Mozilla format for easier reading/writing

# Example of saving cookies in a file
with open('cookies.txt', 'wb') as f:
    cookie_jar.save(file=f, ignore_discard=True, ignore_expires=False)

# Load cookies from a file
cookie_jar.clear()
cookie_jar.load('cookies.txt')

# Print all cookies after loading
for cookie in cookie_jar:
    print(f"Name: {cookie.name}, Value: {cookie.value}")
```

### 7. Handling Secure Cookies

```python
import http.cookiejar

# Create a CookieJar object
cookie_jar = http.cookiejar.CookieJar()

# Example of setting secure cookies
secure_cookie = http.cookiejar.Cookie(
    version=0,
    name='session_id',
    value='1234567890',
    domain='example.com',
    path='/',
    secure=True
)

cookie_jar.set_cookie(secure_cookie)

# Print all cookies, showing secure flag
for cookie in cookie_jar:
    print(f"Name: {cookie.name}, Value: {cookie.value}, Secure: {cookie.secure}")
```

These examples cover the basic functionalities of the `http.cookiejar` module, including creating and managing cookies, parsing responses, sending cookies with requests, handling cookie expiry, domain scope, persistence, and secure cookies. Each example is self-contained and demonstrates a specific aspect of working with HTTP cookies in Python.
