# operator - Standard operators as functions
## Table of Contents

1. [1. Arithmetic Operations](#1-arithmetic-operations)
2. [2. Comparison Operations](#2-comparison-operations)
3. [3. Logical Operations](#3-logical-operations)
4. [4. Identity and Membership Operations](#4-identity-and-membership-operations)
5. [5. Function and Method Calls](#5-function-and-method-calls)
6. [6. Attribute Access and Item Retrieval](#6-attribute-access-and-item-retrieval)
7. [7. Callable Objects](#7-callable-objects)
8. [8. Operator Lookup](#8-operator-lookup)



The `operator` module in Python provides a convenient way to access operators as functions, which can be very useful for performing arithmetic operations, comparisons, and other operations in a more functional style. Below are comprehensive code examples for each functionality provided by the `operator` module.

### 1. Arithmetic Operations

```python
import operator

# Addition
result = operator.add(2, 3)
print("Addition:", result)  # Output: Addition: 5

# Subtraction
result = operator.sub(2, 3)
print("Subtraction:", result)  # Output: Subtraction: -1

# Multiplication
result = operator.mul(2, 3)
print("Multiplication:", result)  # Output: Multiplication: 6

# Division (floating-point division)
result = operator.truediv(5, 2)
print("Division (float):", result)  # Output: Division (float): 2.5

# Floor Division
result = operator.floordiv(5, 2)
print("Floor Division:", result)  # Output: Floor Division: 2

# Modulus
result = operator.mod(7, 3)
print("Modulus:", result)  # Output: Modulus: 1

# Exponentiation
result = operator.pow(2, 3)
print("Exponentiation:", result)  # Output: Exponentiation: 8
```

### 2. Comparison Operations

```python
import operator

# Equal to
result = operator.eq(5, 5)
print("Equal to:", result)  # Output: Equal to: True

# Not equal to
result = operator.ne(5, 5)
print("Not equal to:", result)  # Output: Not equal to: False

# Less than
result = operator.lt(3, 5)
print("Less than:", result)  # Output: Less than: True

# Greater than
result = operator.gt(5, 3)
print("Greater than:", result)  # Output: Greater than: True

# Less than or equal to
result = operator.le(5, 5)
print("Less than or equal to:", result)  # Output: Less than or equal to: True

# Greater than or equal to
result = operator.ge(5, 3)
print("Greater than or equal to:", result)  # Output: Greater than or equal to: True
```

### 3. Logical Operations

```python
import operator

# And
result = operator.and_(True, False)
print("And:", result)  # Output: And: False

# Or
result = operator.or_(True, False)
print("Or:", result)  # Output: Or: True

# Xor (exclusive or)
result = operator.xor(True, False)
print("Xor:", result)  # Output: Xor: True

# Not
result = operator.not_(True)
print("Not:", result)  # Output: Not: False
```

### 4. Identity and Membership Operations

```python
import operator

# Identity check (is)
a = [1, 2, 3]
b = [1, 2, 3]
c = [4, 5, 6]

result = operator.is_(a, b)
print("Identity check (is):", result)  # Output: Identity check (is): True

result = operator.is_not(a, c)
print("Identity check (is not):", result)  # Output: Identity check (is not): True

# Membership check in
result = operator.contains([1, 2, 3], 2)
print("Membership check in:", result)  # Output: Membership check in: True

result = operator.contains([1, 2, 3], 4)
print("Membership check in:", result)  # Output: Membership check in: False
```

### 5. Function and Method Calls

```python
import operator

def add(a, b):
    return a + b

# Call using operator.methodcaller
result = operator.methodcaller('add', 2, 3)(4)
print("Function call:", result)  # Output: Function call: 9

# Call using operator.methodcaller with multiple arguments
result = operator.methodcaller('split', 'hello world')([' ', '.'])
print("Method call (split):", result)  # Output: Method call (split): ['hello', 'world']
```

### 6. Attribute Access and Item Retrieval

```python
import operator

class MyClass:
    def __init__(self, value):
        self.value = value

# Attribute access using operator.attrgetter
obj = MyClass(10)
result = operator.attrgetter('value')(obj)
print("Attribute access:", result)  # Output: Attribute access: 10

# Item retrieval using operator.itemgetter
my_list = [1, 2, 3]
result = operator.itemgetter(1)(my_list)
print("Item retrieval:", result)  # Output: Item retrieval: 2
```

### 7. Callable Objects

```python
import operator

class MyCallable:
    def __call__(self, x):
        return x * 2

# Callable object usage with operator.methodcaller
callable_obj = MyCallable()
result = operator.methodcaller('__call__', 3)(callable_obj)
print("Callable object:", result)  # Output: Callable object: 6
```

### 8. Operator Lookup

```python
import operator

# Look up an operator by its name
add_operator = operator.getattr(operator, 'add')
result = add_operator(2, 3)
print("Operator lookup:", result)  # Output: Operator lookup: 5
```

These examples demonstrate the various functionalities provided by the `operator` module, covering arithmetic, comparison, logical, identity and membership checks, function and method calls, attribute access, item retrieval, callable objects, and operator lookup. Each example is clear, concise, and includes comments to explain each step for better understanding.
