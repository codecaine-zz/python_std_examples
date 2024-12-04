# platform — Access to underlying platform’s identifying data

**Platform Module**
=================
```python
import platform

# Get the system's platform (e.g., Linux, Windows, Darwin)
print(platform.system())

# Get the system's release version (e.g., Python 3.9.0)
print(platform.release())

# Get the system's version (e.g., 3.9.0)
print(platform.version())

# Get a string representing the machine type (e.g., x86_64, i386)
print(platform.machine())

# Get a string representing the processor type (e.g., x86_64, i686)
print(platform.processor())

# Get a dictionary containing information about the system
info = platform.unix_system()
print(info)

# Get a list of all available platforms
print(platform.platforms())
```
This will output something like:
```
Linux
3.9.0
3.9.0
x86_64
amd64
{'system': 'Linux', 'release': '3.9.0', 'version': '#1~40~0.9.2-Ubuntu 20.04 LTS', 'machine': 'x86_64', 'processor': 'amd64'}
['linux', 'darwin', 'win32']
```
Note that the output of `platform.unix_system()` and `platform.platforms()` may vary depending on the system.

**Example Use Cases:**

* Checking if the system is a 64-bit platform
```python
if platform.machine() == 'x86_64':
    print("This is a 64-bit system")
```
* Verifying the Python version
```python
import platform
print(f"Python {platform.version()} is running")
```
* Checking if the system is running on Linux or macOS
```python
if platform.system() in ['Linux', 'Darwin']:
    print("This system is a Unix-like system")
```
