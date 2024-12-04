# collections - Container datatypes

### Collections Module Examples

The `collections` module in Python provides a collection of container data types that are implemented as subclasses of built-in types, often making them more efficient or convenient for specific use cases. Here are comprehensive examples of each data type available in the `collections` module:

---

#### 1. **Counter**

**Description:**
A dictionary subclass for counting hashable objects. Elements are stored as dictionary keys and their counts are stored as dictionary values.

**Example:**

```python
from collections import Counter

# Example with a list of words
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(words)
print(word_counts)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Example with a string
char_counts = Counter("hello world")
print(char_counts)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Example with a dictionary
dict_counts = Counter({'a': 1, 'b': 2, 'c': 1})
print(dict_counts)  # Output: Counter({'b': 2, 'a': 1, 'c': 1})
```

**Explanation:**
- The `Counter` class is used to count the occurrences of each element in a list or any iterable.
- It provides methods like `.most_common(n)` to get the n most common elements and their counts.

---

#### 2. **OrderedDict**

**Description:**
An ordered dictionary that remembers the order in which its contents are added. This is useful when you need to maintain the insertion order of keys.

**Example:**

```python
from collections import OrderedDict

# Example with an ordered dictionary
ordered_dict = OrderedDict()
ordered_dict['apple'] = 1
ordered_dict['banana'] = 2
ordered_dict['orange'] = 3
print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])

# Example with a dictionary and sorting
regular_dict = {'banana': 2, 'apple': 1, 'orange': 3}
ordered_dict = OrderedDict(sorted(regular_dict.items()))
print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])
```

**Explanation:**
- The `OrderedDict` class maintains the insertion order of its elements, which is not guaranteed by regular dictionaries.
- This can be useful in scenarios where maintaining order is important, such as caching or certain types of configurations.

---

#### 3. **defaultdict**

**Description:**
A dictionary subclass that calls a factory function to provide missing values.

**Example:**

```python
from collections import defaultdict

# Example with a defaultdict to count even and odd numbers
count_dict = defaultdict(list)
for number in range(10):
    if number % 2 == 0:
        count_dict['even'].append(number)
    else:
        count_dict['odd'].append(number)

print(count_dict)  # Output: defaultdict(<class 'list'>, {'even': [0, 2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]})

# Example with a defaultdict and a custom factory function
def default_factory():
    return "default value"

custom_dict = defaultdict(default_factory)
print(custom_dict["missing_key"])  # Output: default value
```

**Explanation:**
- The `defaultdict` class is used to initialize dictionary values automatically.
- In this example, it initializes a list for each key that does not already exist in the dictionary.

---

#### 4. **namedtuple**

**Description:**
A factory function returning a new tuple subclass with named fields.

**Example:**

```python
from collections import namedtuple

# Example with a named tuple to represent a point in 2D space
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(x=3, y=4)

print(p1)  # Output: Point(x=1, y=2)
print(p2)  # Output: Point(x=3, y=4)

# Example with a named tuple to represent a person
Person = namedtuple('Person', ['name', 'age'])
person = Person(name="Alice", age=30)

print(person)  # Output: Person(name='Alice', age=30)
print(person.name)  # Output: Alice
print(person.age)  # Output: 30
```

**Explanation:**
- The `namedtuple` function creates a subclass of tuple with named fields.
- This makes the tuple more readable and convenient for representing objects with specific attributes.

---

#### 5. **deque**

**Description:**
A double-ended queue (deque) which supports efficient appends and pops from both ends.

**Example:**

```python
from collections import deque

# Example with a deque to implement a simple stack
stack = deque()
stack.append(1)
stack.append(2)
stack.appendleft(3)

print(stack)  # Output: deque([3, 1, 2])
print(stack.pop())  # Output: 2
print(stack.popleft())  # Output: 3

# Example with a deque to implement a queue
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # Output: deque([1, 2, 3])
print(queue.popleft())  # Output: 1
print(queue)  # Output: deque([2, 3])
```

**Explanation:**
- The `deque` class is an optimized list for fast appends and pops from both ends.
- This is useful in scenarios where you need a dynamic array that supports efficient push and pop operations on both sides.

---

#### 6. **ChainMap**

**Description:**
A collection which provides a way to group multiple mappings as if they were one, but which does not actually merge them.

**Example:**

```python
from collections import ChainMap

# Example with chain maps for combining multiple dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

combined_dict = ChainMap(dict1, dict2)
print(combined_dict)  # Output: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

# Example with chain maps and updating values
dict1['a'] = 5
print(combined_dict)  # Output: ChainMap({'a': 5, 'b': 2}, {'b': 3, 'c': 4})
```

**Explanation:**
- The `ChainMap` class allows you to create a new dictionary that combines multiple dictionaries.
- It will prioritize the first dictionary when retrieving values for keys that exist in more than one.

---

#### 7. **UserDict**

**Description:**
A subclass of dict providing a base class for dictionary subclasses.

**Example:**

```python
from collections import UserDict

# Example with a user-defined dictionary subclass
class MyDict(UserDict):
    def __missing__(self, key):
        # Custom behavior when an item is missing
        return f"Key {key} not found"

my_dict = MyDict()
my_dict['name'] = 'Alice'
print(my_dict)  # Output: {'name': 'Alice'}
print(my_dict['age'])  # Output: Key age not found

# Example with a user-defined dictionary subclass and custom initialization
class MyDictWithInit(UserDict):
    def __init__(self, initial_data):
        super().__init__(initial_data)
        self.custom_attribute = 'custom_value'

my_dict_with_init = MyDictWithInit({'key1': 'value1'})
print(my_dict_with_init)  # Output: {'key1': 'value1'}
print(my_dict_with_init.custom_attribute)  # Output: custom_value
```

**Explanation:**
- The `UserDict` class allows you to create a custom dictionary subclass with additional behavior.
- It provides a method `__missing__` that can be overridden to customize the behavior when a key is missing.

---

#### 8. **UserList**

**Description:**
A subclass of list providing a base class for list subclasses.

**Example:**

```python
from collections import UserList

# Example with a user-defined list subclass
class MyList(UserList):
    def __init__(self, iterable=()):
        # Custom initialization behavior
        super().__init__(iterable)
        self.custom_attribute = 'hello'

my_list = MyList([1, 2, 3])
print(my_list)  # Output: [1, 2, 3]
print(my_list.custom_attribute)  # Output: hello

# Example with a user-defined list subclass and custom method
class MyListWithMethod(UserList):
    def custom_method(self):
        return sum(self)

my_list_with_method = MyListWithMethod([1, 2, 3])
print(my_list_with_method)  # Output: [1, 2, 3]
print(my_list_with_method.custom_method())  # Output: 6
```

**Explanation:**
- The `UserList` class allows you to create a custom list subclass with additional behavior.
- It provides a method `__init__` that can be overridden to customize initialization.

---

#### 9. **UserString**

**Description:**
A subclass of str providing a base class for string subclasses.

**Example:**

```python
from collections import UserString

# Example with a user-defined string subclass
class MyString(UserString):
    def __init__(self, data=''):
        # Custom initialization behavior
        super().__init__(data)
        self.custom_attribute = 'world'

my_string = MyString('hello')
print(my_string)  # Output: hello
print(my_string.custom_attribute)  # Output: world

# Example with a user-defined string subclass and custom method
class MyStringWithMethod(UserString):
    def custom_method(self):
        return self.data.upper()

my_string_with_method = MyStringWithMethod('hello')
print(my_string_with_method)  # Output: hello
print(my_string_with_method.custom_method())  # Output: HELLO
```

**Explanation:**
- The `UserString` class allows you to create a custom string subclass with additional behavior.
- It provides a method `__init__` that can be overridden to customize initialization.

---

These examples demonstrate various functionalities of the `collections` module, from basic counting to more advanced data structures like `OrderedDict` and `deque`. These classes are designed to improve performance and readability in Python applications.
