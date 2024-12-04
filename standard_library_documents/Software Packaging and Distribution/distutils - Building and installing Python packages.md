# distutils - Building and installing Python packages

The `distutils` module is an older package that is now considered deprecated. It is used to build and install Python packages, but it has been largely replaced by newer tools such as `setuptools` and `wheel`. However, I will provide code examples for using the original `distutils` to illustrate how you might have built and installed a simple Python package in earlier versions of Python.

### Example 1: Creating a Simple Package with Distutils

#### Step 1: Create a Directory for Your Package
First, create a directory where your package files will be stored. For example:
```bash
mkdir my_package
cd my_package
```

#### Step 2: Initialize the Package
Create an `__init__.py` file to mark this directory as a Python package:
```python
# __init__.py
from .module1 import Module1
from .module2 import Module2
```

#### Step 3: Create Your Modules
Create two modules within your package. For example, create `module1.py` and `module2.py` with some basic functionality:
```python
# module1.py
def greet(name):
    return f"Hello, {name}!"

# module2.py
def add_numbers(a, b):
    return a + b
```

#### Step 4: Create a Setup Script
Create a `setup.py` file to specify how your package should be built and installed:
```python
# setup.py
from setuptools import setup

setup(
    name='my_package',
    version='0.1',
    packages=['my_package'],
)
```

#### Step 5: Build the Package
To build the package, use the following command in the terminal:
```bash
python setup.py sdist bdist_wheel
```

This will create a `.tar.gz` distribution and a wheel file in the `dist/` directory.

#### Step 6: Install the Package
To install the package locally, run:
```bash
pip install dist/my_package-0.1-py3-none-any.whl
```

Or, if you have built a local source distribution (`my_package-0.1.tar.gz`), use:
```bash
pip install my_package-0.1.tar.gz
```

### Example 2: Building and Installing Using `setuptools` (Recommended)

#### Step 1: Install `setuptools`
If you haven't already, you need to install `setuptools`. You can do this using pip:
```bash
pip install setuptools
```

#### Step 2: Use `setup.py` with `setuptools`
Ensure your `setup.py` file uses `setuptools` by adding the necessary import statement at the beginning:
```python
# setup.py
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
)
```

#### Step 3: Build and Install Using `setuptools`
Use the following command to build and install your package:
```bash
python setup.py bdist_wheel
pip install dist/my_package-0.1-py3-none-any.whl
```

or if you have a source distribution:
```bash
python setup.py sdist bdist_wheel
pip install my_package-0.1.tar.gz
```

### Notes
- **Deprecated**: As mentioned, `distutils` is deprecated and may not be supported in future Python versions.
- **Setuptools**: The newer tools (`setuptools`, `wheel`) are recommended for creating and distributing Python packages due to their robustness and ease of use.
- **Dependencies**: If your package has dependencies, you should specify them in the `setup.py` file using the `install_requires` parameter.

These examples demonstrate how to create and install a simple Python package using both `distutils` and `setuptools`. For production environments, it's advisable to use `setuptools` for better support and features.
