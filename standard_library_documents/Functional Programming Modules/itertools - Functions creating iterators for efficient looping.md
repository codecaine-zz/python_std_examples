# itertools — Functions creating iterators for efficient looping

Here are some examples of using the `itertools` module in Python 3.12:

**1. Counting**

```python
import itertools

# Create an iterator that counts from 0
counter = itertools.count(5)

print(next(counter))  # prints: 5
print(next(counter))  # prints: 6
```

**2. Cycles**

```python
import itertools

# Create a cycle of numbers from 1 to 3, repeating when exhausted
cycle = itertools.cycle([1, 2, 3])

for _ in range(7):
    print(next(cycle))  # prints: 1, 2, 3, 1, 2, 3, 1

# Create a cycle of strings
string_cycle = itertools.cycle('abcdef')

for _ in range(10):
    print(next(string_cycle))
```

**3. Accumulate**

```python
import itertools

numbers = [1, 2, 3]

# Use accumulate to calculate the cumulative sum
print(list(itertools.accumulate(numbers)))  # prints: [1, 3, 6]
```

**4. Combinations**

```python
import itertools

numbers = [1, 2, 3]

# Create combinations of length 2 from the numbers list
combinations = list(itertools.combinations(numbers, 2))
print(combinations)  # prints: [(1, 2), (1, 3), (2, 3)]

# Create combinations with repetition allowed
combination_with_repetition = list(itertools.combinations_with_replacement(numbers, 2))
print(combination_with_repetition)  # prints: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```

**5. Product**

```python
import itertools

numbers = [1, 2]

# Create the Cartesian product of two lists
product = list(itertools.product(numbers, numbers))
print(product)  # prints: [(1, 1), (1, 2), (2, 1), (2, 2)]
```

**6. Groupby**

```python
import itertools

students = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 21},
    {'name': 'Charlie', 'age': 20},
    {'name': 'David', 'age': 22}
]

# Group students by age
for age, group in itertools.groupby(students, key=lambda x: x['age']):
    print(f"Age {age}:")
    for student in group:
        print(student['name'])
```

**7. Permutations**

```python
import itertools

numbers = [1, 2, 3]

# Create permutations of a list
permutations = list(itertools.permutations(numbers))
print(permutations)  # prints: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# Create permutations with repetition allowed
permutations_with_repetition = list(itertools.permutations(numbers, 3))
print(permutations_with_repetition)  # prints: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

**8. Chain**

```python
import itertools

# Create a chain of iterators
iterator_1 = [1, 2, 3]
iterator_2 = ['a', 'b', 'c']

chain = itertools.chain(iterator_1, iterator_2)
print(list(chain))  # prints: [1, 2, 3, 'a', 'b', 'c']
```

**9. Accumulate with an initial value**

```python
import itertools

numbers = [1, 2, 3]

# Use accumulate to calculate the cumulative sum with an initial value of 0
print(list(itertools.accumulate(numbers, initial=0)))  # prints: [0, 1, 3, 6]
```

**10. Tee**

```python
import itertools

numbers = [1, 2, 3]

# Create two independent iterators from the same list
iterator_1, iterator_2 = itertools.tee(numbers)
print(list(iterator_1))  # prints: [1, 2, 3]
print(list(iterator_2))  # prints: [1, 2, 3]

# Modify one of the iterators
for _ in range(3):
    print(next(iterator_1))
```

These examples demonstrate various functions provided by the `itertools` module, including creating iterators for efficient looping, combining multiple iterables into a single iterable, and performing various operations on iterables.
