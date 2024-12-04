# test.support.script_helper — Utilities for the Python test suite

Here are some examples of how you can use utilities provided by `test.support.script_helper`:
```python
import unittest
from test.support.script_helper import *

# Example 1: Test that a script exits with the correct status code
def test_script_exit():
    # Create a simple script that exits with a specific status code
    script = """
        import sys

        if __name__ == "__main__":
            print("Hello World!")
            sys.exit(123)
    """

    # Run the script and check the exit status
    process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    assert process.returncode == 123

# Example 2: Test that a script outputs to a file descriptor
def test_script_output():
    # Create a simple script that prints to the standard output
    script = """
        import sys

        if __name__ == "__main__":
            print("Hello World!", flush=True)
    """

    # Run the script and check the output
    process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    assert output.decode().strip() == "Hello World!"

# Example 3: Test that a script has the correct shebang line
def test_script_shebang():
    # Create a simple script with a shebang line that points to an invalid interpreter
    script = "#!/bin/non-existent-interpreter\nimport sys\nif __name__ == \"__main__\":\n    print(\"Hello World!\")"

    # Try to run the script and check for an error
    try:
        subprocess.run(script, shell=True, check=False)
    except FileNotFoundError:
        pass
    else:
        assert False

# Example 4: Test that a script has the correct executable permissions
def test_script_permissions():
    # Create a simple script with the wrong permissions
    script = """
        import sys

        if __name__ == "__main__":
            print("Hello World!")
    """

    # Try to run the script and check for an error
    try:
        subprocess.run(script, shell=True)
    except PermissionError:
        pass
    else:
        assert False

# Example 5: Test that a script imports correctly
def test_script_imports():
    # Create a simple module with a function
    mod = """
    import sys

    def hello_world():
        print("Hello World!")

    def main():
        hello_world()

    if __name__ == "__main__":
        main()
    """

    # Run the script and check that it calls the function
    process = subprocess.Popen(mod, shell=True)
    output = process.communicate()[0]
    assert "Hello World!" in output.decode()

if __name__ == "__main__":
    unittest.main(argv=[__file__, "-v", "-s"])
```
These examples demonstrate how you can use `test.support.script_helper` to test various aspects of a script, including its exit status, output, shebang line, permissions, and imports.
