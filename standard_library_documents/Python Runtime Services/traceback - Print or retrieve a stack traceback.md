# traceback - Print or retrieve a stack traceback

Below are comprehensive code examples that demonstrate various functionalities of the `traceback` module in Python, along with clear explanations and comments:

```python
# Import the traceback module
import traceback

def example_function():
    # Simulate an exception for demonstration purposes
    try:
        result = 10 / 0
    except Exception as e:
        # Print a stack trace to the console
        traceback.print_exc()
        
        # Optionally, retrieve and print the traceback as a string
        tb_string = traceback.format_exc()
        print(tb_string)

def example_traceback():
    # Example of using traceback to catch and format an exception
    try:
        result = 10 / 0
    except Exception as e:
        # Use traceback.print_exception to print the traceback to the console
        traceback.print_exception(type(e), e, e.__traceback__)
        
        # Format the traceback into a string for further processing
        tb_string = traceback.format_exception(type(e), e, e.__traceback__)
        print(tb_string)

def example_traceback_with_frame_info():
    # Example of using traceback to extract frame information
    try:
        result = 10 / 0
    except Exception as e:
        # Use traceback.extract_tb to get the stack trace in list format
        tb_list = traceback.extract_tb(e.__traceback__)
        
        # Print each frame's filename, line number, function name, and code snippet
        for frame_info in tb_list:
            print(f"File: {frame_info.filename}, Line: {frame_info.lineno}, Function: {frame_info.function}")
            
        # Format the traceback into a string with more detailed information
        tb_string = traceback.format_exception(type(e), e, e.__traceback__)
        print(tb_string)

def example_traceback_with_tb_object():
    # Example of using traceback to work with the Traceback object directly
    try:
        result = 10 / 0
    except Exception as e:
        # Get the entire traceback object
        tb_obj = e.__traceback__
        
        # Print the traceback object's properties
        print(f"Traceback object: {tb_obj}")
        
        # Format the traceback into a string for further processing
        tb_string = traceback.format_exception(type(e), e, e.__traceback__)
        print(tb_string)

def example_traceback_with_file_object():
    # Example of using traceback to write to a file instead of console
    try:
        result = 10 / 0
    except Exception as e:
        # Open a file for writing the traceback
        with open("error_log.txt", "w") as log_file:
            # Use traceback.print_exception to write the traceback to the file
            traceback.print_exception(type(e), e, e.__traceback__, file=log_file)
            
            # Optionally, format the traceback into a string and print it for confirmation
            tb_string = traceback.format_exception(type(e), e, e.__traceback__)
            print(f"Formatted traceback written to 'error_log.txt':\n{tb_string}")

# Run example functions
example_function()
example_traceback()
example_traceback_with_frame_info()
example_traceback_with_tb_object()
example_traceback_with_file_object()
```

### Explanation:

1. **`example_function()`**:
   - Demonstrates how to print a stack trace using `traceback.print_exc()`, which prints the traceback to the console.

2. **`example_traceback()`**:
   - Uses `traceback.print_exception()` to print and format the traceback into a string, which can be useful for logging or further processing.

3. **`example_traceback_with_frame_info()`**:
   - Retrieves and prints detailed information about each frame in the stack trace using `traceback.extract_tb()`. This includes filename, line number, function name, and code snippet.

4. **`example_traceback_with_tb_object()`**:
   - Accesses and prints the entire traceback object using `e.__traceback__`, which can provide additional debugging information if needed.

5. **`example_traceback_with_file_object()`**:
   - Writes the traceback to a file instead of printing it to the console using `traceback.print_exception()`. This is useful for logging errors to a log file.

Each example includes comments that explain the purpose and functionality of each part of the code, making it easy to understand and modify as needed.
