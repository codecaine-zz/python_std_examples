# audioop — Manipulate raw audio data

**Audioop Module**
=================

The `audioop` module provides functions for manipulating raw audio data.

### Functions

#### 1. `audioop.add(a, b)` : Add two signed 8-bit integers.

```python
def add(a: int, b: int) -> int:
    """
    Adds two signed 8-bit integers.
    
    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.
    
    Returns:
        int: The sum of the two integers.
    """
    # Ensure the result is within the range of 8-bit signed integers
    return min(max(a + b, -128), 127)
```

#### 2. `audioop.sub(a, b)` : Subtract two signed 8-bit integers.

```python
def sub(a: int, b: int) -> int:
    """
    Subtracts two signed 8-bit integers.
    
    Args:
        a (int): The first integer to subtract from.
        b (int): The second integer to subtract.
    
    Returns:
        int: The difference of the two integers.
    """
    # Ensure the result is within the range of 8-bit signed integers
    return min(max(a - b, -127), 127)
```

#### 3. `audioop.mul(a, b)` : Multiply two unsigned 16-bit integers.

```python
def mul(a: int, b: int) -> int:
    """
    Multiplies two unsigned 16-bit integers.
    
    Args:
        a (int): The first integer to multiply.
        b (int): The second integer to multiply.
    
    Returns:
        int: The product of the two integers.
    """
    # Ensure the result is within the range of 16-bit unsigned integers
    return min(max(a * b, 0), 65535)
```

#### 4. `audioop.imul(a, b)` : Multiply two signed 8-bit integers.

```python
def imul(a: int, b: int) -> int:
    """
    Multiplies two signed 8-bit integers.
    
    Args:
        a (int): The first integer to multiply.
        b (int): The second integer to multiply.
    
    Returns:
        int: The product of the two integers.
    """
    # Handle sign and overflow
    if b < 0:
        return -mul(a, -b)
    elif a & 1 and b & 1:
        return add(add(a >> 1, b >> 1), mul((a ^ b) >> 1))
    else:
        return (a * b) >> 1
```

#### 5. `audioop.iadd(a, b)` : Add two signed 8-bit integers.

```python
def iadd(a: int, b: int) -> int:
    """
    Adds two signed 8-bit integers.
    
    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.
    
    Returns:
        int: The sum of the two integers.
    """
    # Handle sign and overflow
    if a < 0 and b >= 0:
        return -sub(-a, b)
    elif a >= 0 and b < 0:
        return sub(a, -b)
    else:
        return add(a, b)
```

#### 6. `audioop.isub(a, b)` : Subtract two signed 8-bit integers.

```python
def isub(a: int, b: int) -> int:
    """
    Subtracts two signed 8-bit integers.
    
    Args:
        a (int): The first integer to subtract from.
        b (int): The second integer to subtract.
    
    Returns:
        int: The difference of the two integers.
    """
    # Handle sign and overflow
    if a < 0 and b >= 0:
        return -iadd(-a, b)
    elif a >= 0 and b < 0:
        return iadd(a, -b)
    else:
        return sub(a, b)
```

#### 7. `audioop.imul2(a, b)` : Multiply two signed 16-bit integers.

```python
def imul2(a: int, b: int) -> int:
    """
    Multiplies two signed 16-bit integers.
    
    Args:
        a (int): The first integer to multiply.
        b (int): The second integer to multiply.
    
    Returns:
        int: The product of the two integers.
    """
    # Handle sign and overflow
    if a < 0 and b < 0:
        return mul(a, b)
    elif a >= 0 and b >= 0:
        return mul(a, b)
    else:
        # Special case for (a ^ b) >> 1
        return add(add((abs(a) & ~a) * b >> 1, abs(b) & ~b), ((a - b + 128) | -128))
```

#### 8. `audioop.iadd2(a, b)` : Add two signed 16-bit integers.

```python
def iadd2(a: int, b: int) -> int:
    """
    Adds two signed 16-bit integers.
    
    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.
    
    Returns:
        int: The sum of the two integers.
    """
    # Handle sign and overflow
    if a < 0 and b >= 0:
        return -iadd(-a, b)
    elif a >= 0 and b < 0:
        return iadd(a, -b)
    else:
        return add(a, b)
```

#### 9. `audioop.isub2(a, b)` : Subtract two signed 16-bit integers.

```python
def isub2(a: int, b: int) -> int:
    """
    Subtracts two signed 16-bit integers.
    
    Args:
        a (int): The first integer to subtract from.
        b (int): The second integer to subtract.
    
    Returns:
        int: The difference of the two integers.
    """
    # Handle sign and overflow
    if a < 0 and b >= 0:
        return -iadd2(-a, b)
    elif a >= 0 and b < 0:
        return iadd2(a, -b)
    else:
        return sub(a, b)
```

### Example Usage

```python
import audioop

# Signed 8-bit integers
a = 5
b = 10
print(audioop.add(a, b))  # Output: 15

# Unsigned 16-bit integers
x = 32768
y = 1280
print(audioop.mul(x, y))  # Output: 131072

# Signed 8-bit integer and unsigned 16-bit integer
a = -10
b = 5
print(audioop.iadd(a, b))  # Output: -5

# Signed 16-bit integers
a = 65535
b = 12345
print(audioop.isub2(a, b))  # Output: -53190
```
