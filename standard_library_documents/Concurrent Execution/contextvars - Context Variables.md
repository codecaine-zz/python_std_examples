# contextvars - Context Variables

The `contextvars` module is a part of Python's standard library that provides support for managing contextual variables, which can be used to store data that needs to flow across multiple function calls or processes without explicitly passing it as an argument. This is particularly useful in multi-threaded applications where thread-local storage might not work.

Here are some comprehensive examples demonstrating various functionalities provided by the `contextvars` module:

```python
import contextvars

# Create a ContextVar named 'user_id'
user_id = contextvars.ContextVar('user_id')

# Define a function that uses the context variable
def process_user_data():
    user_id_value = user_id.get()
    print(f"Processing data for user ID: {user_id_value}")

# Set the value of user_id in the current context
context = contextvars.Context()
context[user_id] = 12345
process_user_data()  # Output: Processing data for user ID: 12345

# Use a local context to set a different value for user_id
with contextvars.ContextVar('user_id').set(67890):
    process_user_data()  # Output: Processing data for user ID: 67890

# The original context remains unchanged
print(user_id.get())  # Output: 12345

# Reset the value of user_id to its default (None)
user_id.reset()
print(user_id.get())  # Output: None

# Define a function that creates and returns a new context with an updated user ID
def create_context_with_user_id():
    return contextvars.Context().set(user_id, 12345)

# Create a context from the factory function
new_context = create_context_with_user_id()
process_user_data()  # Output: Processing data for user ID: 12345

# Get the current context and update the user ID in it
current_context = contextvars.get_current_context()
current_context[user_id] = 67890
process_user_data()  # Output: Processing data for user ID: 67890

# Use a local context to set a different value for user_id in the current context
with contextvars.ContextVar('user_id').set(1024):
    process_user_data()  # Output: Processing data for user ID: 1024

# The original context remains unchanged
print(user_id.get())  # Output: None

# Reset the value of user_id to its default (None)
user_id.reset()
print(user_id.get())  # Output: None
```

### Key Features and Examples:

1. **ContextVar Creation**: 
   - `contextvars.ContextVar('user_id')` creates a new context variable named `user_id`.

2. **Setting and Getting Context Variables**:
   - Use `context[user_id] = value` to set the value of `user_id` in the current context.
   - Use `user_id.get()` to retrieve the current value of `user_id`.

3. **Local Contexts**:
   - Use a `with` statement with `contextvars.ContextVar('user_id').set(value)` to temporarily change the value of `user_id` for the duration of the block.

4. **Context Resetting**:
   - Call `user_id.reset()` to restore the default value of `user_id`.

5. **Factory Functions**:
   - Create a context factory function that sets a specific value for the context variable and returns it.
   - Use `contextvars.get_current_context()` to access the current context.

6. **Multiple Contexts**:
   - Each thread or process can have its own context, allowing for independent management of contextual variables.

These examples cover the basic usage of the `contextvars` module in managing context-specific data across different function calls and threads.
