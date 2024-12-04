# warnings — Warning control

Here's an example of how you can use the warnings module in Python:

```python
# Importing the warnings module
import warnings

# Issues: These are issues that are considered to be errors or need special attention.

# Filter warnings: You can filter out specific types of warnings based on their category.
with warnings.catch_warnings():
    # Ignore specific categories of warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=UserWarning)

    # Now, any new warnings will be raised
    import numpy as np

# New warnings are now being raised
try:
    import older_numpy  # This imports an older version of NumPy that has been deprecated.
except ImportError:
    print("Error: Older version of NumPy not found.")

# Category and message for a warning to be displayed:
warnings.warn("You're running an old version of Python.", UserWarning)

# Suppressing warnings: You can also suppress specific warnings by passing their category directly into the warn function.

with warnings.catch_warnings():
    # Suppress specific warnings
    warnings.filterwarnings("error", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=FutureWarning)

    # Now, any new warnings will be suppressed and raise an error
    import os

# Suppressing warnings on the fly:
def do_something():
    with warnings.catch_warnings(record=True):
        # Warning that will not be raised
        1 / 0
        
        # A warning that will be raised
        import numpy as np

# Suppressing warnings for a function or block of code:
try:
    import older_numpy  # This imports an older version of NumPy that has been deprecated.
except ImportError:
    with warnings.catch_warnings():
        # Ignore specific categories of warnings
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        
        # Now, any new warnings will be raised
        import numpy as np

# How to handle different warning types using a context manager:

with warnings.catch_warnings():
    # Suppress specific warnings
    warnings.filterwarnings("error", category=DeprecationWarning)

    try:
        # This is where you want to put your code.
        with warnings.catch_warnings(record=True):
            import numpy as np
    except Warning as w:
        print(w.message)
```

Here are some common usage scenarios for the warnings module:

1.  **Ignoring specific categories of warnings:** 

    ```python
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
```

2.  **Suppressing warnings on a per-call basis:**

    ```python
with warnings.catch_warnings():
    warnings.simplefilter('error')
    with warnings.catch_warnings(record=True):
        import numpy as np
```

3.  **Ignoring all warnings in a function or block of code:**

    ```python
try:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        import numpy as np
except Warning:
    print("Warning message")
```

4.  **Suppressing specific categories of warnings for an entire module:**

    You can use the `warnings.simplefilter()` function to suppress specific warning types in your own code, like so:

    ```python
import warnings

warnings.simplefilter('ignore', DeprecationWarning)

# Now you're running on a modified version of Python with all deprecated features disabled.
```

5.  **Suppressing warnings for an entire file or module:**

    You can also use `warnings.catch_warnings()` to suppress specific warning types in your own code, like so:

    ```python
import warnings

try:
    import older_numpy  # This imports an older version of NumPy that has been deprecated.
except ImportError:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        
        import numpy as np
```

6.  **Suppressing warnings in a specific block of code:**

    You can also use `try`/`except` blocks to suppress specific warning types, like so:

    ```python
try:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=FutureWarning)
        import os
except Warning as w:
    print(w.message)
```

7.  **Suppressing all warnings:**

    You can use the `warnings.simplefilter()` function to suppress specific warning types globally, like so:

    ```python
import warnings

warnings.simplefilter('ignore', DeprecationWarning)

# Now you're running on a modified version of Python with all deprecated features disabled.
```
