# wsgiref — WSGI Utilities and Reference Implementation

**WSGI Utilities and Reference Implementation**
=====================================================

The `wsgiref` module provides utility functions for working with the Web Server Gateway Interface (WSGI) in Python.

### Module Contents

*   **`__init__.py`**: Initializes the module.
*   **`app_wsgi.py`**: A reference implementation of a WSGI application.
*   **`test_app.py`**: Tests the `AppWsgi` class.
*   **`test_wsgiref.py`**: Tests the `wsgiref` module as a whole.

### Functions

#### 1. `wsgiref.util.get_wsgi_app`

*   Returns a WSGI application from an object that implements the `wsgiref.util.wsgi_app` interface.
*   **Example:**
    ```python
from wsgiref import util

class MyWSGIApp:
    def __call__(self, environ, start_response):
        # implementation

app = MyWSGIApp()
wsgi_app = util.get_wsgi_app(app)
```

#### 2. `wsgiref.util.wsgi_app`

*   Defines the WSGI application interface.
*   **Example:**
    ```python
from wsgiref import util

class wsgi_app:
    def __call__(self, environ, start_response):
        # implementation
```

#### 3. `wsgiref.util.get_wsgi_server_class`

*   Returns the class of a WSGI server object that implements the `wsgiref.util.wsgi_server` interface.
*   **Example:**
    ```python
from wsgiref import util

class MyWSGIServer:
    def __call__(self, environ, start_response):
        # implementation

server = MyWSGIServer()
wsgi_server_class = util.get_wsgi_server_class(server)
```

#### 4. `wsgiref.util.wsgi_server`

*   Defines the WSGI server interface.
*   **Example:**
    ```python
from wsgiref import util

class wsgi_server:
    def __call__(self, environ, start_response):
        # implementation
```

### Classes

#### 1. `wsgiref.util.AppWsgi`

*   A reference implementation of a WSGI application.
*   **Example:**
    ```python
from wsgiref import util

class AppWsgi:
    def __call__(self, environ, start_response):
        # implementation
```

#### 2. `wsgiref.util.WSGIServeHTTPHandlerBase`

*   A base class for WSGI HTTP request handlers.
*   **Example:**
    ```python
from wsgiref import util

class WSGIServeHTTPHandlerBase:
    def __init__(self, *args, **kwargs):
        # implementation

    def do_GET(self, environ, start_response):
        # implementation
```

### Functions

#### 1. `wsgiref.test.util.get_app_with_environ`

*   Returns a WSGI application with the given environment variables.
*   **Example:**
    ```python
from wsgiref import test.util

app = util.get_app_with_environ({'PATH_INFO': '/'})(lambda environ, start_response: None)
```

#### 2. `wsgiref.test.util.get_app_with_headers`

*   Returns a WSGI application with the given request headers.
*   **Example:**
    ```python
from wsgiref import test.util

app = util.get_app_with_headers({'Content-Type': 'text/html'})(lambda environ, start_response: None)
```

### Classes

#### 1. `wsgiref.test.AppWsgiTestCase`

*   A base class for testing WSGI applications.
*   **Example:**
    ```python
from wsgiref import test

class AppWsgiTestCase(test.TestCase):
    def setUp(self):
        # implementation

    def test_app(self):
        # implementation
```

#### 2. `wsgiref.test.AppWSGIHandlerTest`

*   A base class for testing WSGI HTTP request handlers.
*   **Example:**
    ```python
from wsgiref import test

class AppWSGIHandlerTest(test.TestCase):
    def setUp(self):
        # implementation

    def test_handler(self):
        # implementation
```

### Functions

#### 1. `wsgiref.test.test_app`

*   Tests the `AppWsgi` class.
*   **Example:**
    ```python
from wsgiref import test

class TestAppWSGI(test.TestCase):
    def setUp(self):
        self.app = util.get_app_with_environ({'PATH_INFO': '/'})(lambda environ, start_response: None)

    def test_app(self):
        response = self.app(environ={'PATH_INFO': '/'}, start_response='200 OK')
        # implementation
```

#### 2. `wsgiref.test.test_wsgiref`

*   Tests the `wsgiref` module as a whole.
*   **Example:**
    ```python
from wsgiref import test

class TestWSGIREF(test.TestCase):
    def setUp(self):
        # implementation

    def test_module(self):
        # implementation
```

### Classes

#### 1. `wsgiref.test.WSGITestCase`

*   A base class for testing WSGI applications.
*   **Example:**
    ```python
from wsgiref import test

class WSGITestCase(test.TestCase):
    def setUp(self):
        # implementation

    def test_app(self):
        # implementation
```

#### 2. `wsgiref.test.WSGIHandlerTest`

*   A base class for testing WSGI HTTP request handlers.
*   **Example:**
    ```python
from wsgiref import test

class WSGIHandlerTest(test.TestCase):
    def setUp(self):
        # implementation

    def test_handler(self):
        # implementation
```

Note that this is not an exhaustive list of all functions and classes in the `wsgiref` module. The above examples are just a few illustrations of how to use the various components of the module.
