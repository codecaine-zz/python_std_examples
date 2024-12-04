# webbrowser — Convenient web-browser controller

**WebBrowser Module Code Generation**
=====================================

The `webbrowser` module provides an interface for controlling the current web browser on a system.

**Code Generation**
-----------------

```python
import webbrowser

# Open a URL in the default browser
def open_url(url):
    """
    Opens a URL in the default browser.
    
    Args:
        url (str): The URL to be opened.
    """
    webbrowser.open(url)

# Get the current URL
def get_current_url():
    """
    Returns the current URL of the browser.
    
    Returns:
        str: The current URL.
    """
    return webbrowser.get().home_page

# Open a new tab in the default browser
def open_new_tab(url):
    """
    Opens a new tab with the specified URL in the default browser.
    
    Args:
        url (str): The URL to be opened.
    """
    webbrowser.open_new_tab(url)

# Get all available browsers
def get_available_browsers():
    """
    Returns a list of all available browsers.
    
    Returns:
        list: A list of browser names.
    """
    return webbrowser.get().available_browsers

# Open a URL in a specific browser
def open_url_in_browser(browser_name, url):
    """
    Opens a URL in the specified browser.
    
    Args:
        browser_name (str): The name of the browser to be used.
        url (str): The URL to be opened.
    """
    for browser in webbrowser.get().browsers():
        if browser.name == browser_name:
            webbrowser.open(url)

# Open a new tab in a specific browser
def open_new_tab_in_browser(browser_name, url):
    """
    Opens a new tab with the specified URL in the specified browser.
    
    Args:
        browser_name (str): The name of the browser to be used.
        url (str): The URL to be opened.
    """
    for browser in webbrowser.get().browsers():
        if browser.name == browser_name:
            webbrowser.open_new_tab(url)

# Set a new homepage
def set_homepage(browser, url):
    """
    Sets a new homepage for the specified browser.
    
    Args:
        browser (str): The name of the browser to be used.
        url (str): The URL to be set as the new homepage.
    """
    for browser in webbrowser.get().browsers():
        if browser.name == browser_name:
            browser.set_home_page(url)
```

**Example Usage**
-----------------

```python
# Open a URL in the default browser
open_url("https://www.google.com")

# Get the current URL
print(get_current_url())

# Open a new tab in the default browser
open_new_tab("https://www.stackoverflow.com")

# Get all available browsers
print(get_available_browsers())

# Open a URL in Chrome
open_url_in_browser("Chrome", "https://www.google.com")

# Open a new tab in Firefox
open_new_tab_in_browser("Firefox", "https://www.github.com")
```

Note: The `browser_name` argument is case-sensitive and should match the exact name of the browser.
