# itertools - Functions creating iterators for efficient looping

Certainly! Below are comprehensive code examples for each function in the `itertools` module, along with comments explaining each step:

```python
import itertools

# 1. accumulate(iterable[, func])
# Returns an iterator that returns accumulated sums or results of a binary function.

numbers = [1, 2, 3, 4]
sum_iterator = itertools.accumulate(numbers)
print(list(sum_iterator))  # Output: [1, 3, 6, 10]

from operator import mul
product_iterator = itertools.accumulate(numbers, mul)
print(list(product_iterator))  # Output: [1, 2, 6, 24]


# 2. chain(*iterables)
# Returns a single iterable that concatenates the input iterables.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
chain_iterator = itertools.chain(list1, list2)
print(list(chain_iterator))  # Output: [1, 2, 3, 'a', 'b', 'c']


# 3. combinations(iterable, r)
# Returns an iterator that yields all possible combinations of the input iterable taken r at a time.

elements = ['A', 'B', 'C']
combinations_of_2 = itertools.combinations(elements, 2)
print(list(combinations_of_2))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]


# 4. combinations_with_replacement(iterable, r)
# Returns an iterator that yields all possible combinations of the input iterable taken r at a time,
# with replacement.

combinations_with_replacement_of_2 = itertools.combinations_with_replacement(elements, 2)
print(list(combinations_with_replacement_of_2))  # Output: [('A', 'A'), ('A', 'B'), ('A', 'C'), 
                                                  #       ('B', 'B'), ('B', 'C'), ('C', 'C')]


# 5. combinations(iterable, r)
# Returns an iterator that yields all possible permutations of the input iterable taken r at a time.

permutations_of_2 = itertools.permutations(elements, 2)
print(list(permutations_of_2))  # Output: [('A', 'B'), ('A', 'C'), ('A', 'B'), ('B', 'A'), 
                                      #       ('B', 'C'), ('C', 'A')]


# 6. cycle(iterable)
# Returns an iterator that endlessly repeats the items from the input iterable.

repeating_iterator = itertools.cycle(elements)
for _ in range(10):
    print(next(repeating_iterator))  # Output will repeat 'A', 'B', 'C' in sequence


# 7. combinations_with_replacement(iterable, r)
# Returns an iterator that yields all possible permutations of the input iterable taken r at a time,
# with replacement.

permutations_with_replacement_of_3 = itertools.permutations(elements, 3)
print(list(permutations_with_replacement_of_3))  # Output: [('A', 'B', 'C'), ('A', 'C', 'A'), 
                                                  #       ('A', 'C', 'B'), ('B', 'A', 'C'),
                                                  #       ('B', 'C', 'A'), ('B', 'C', 'B'),
                                                  #       ('C', 'A', 'B'), ('C', 'B', 'A'),
                                                  #       ('C', 'B', 'C')]


# 8. count(start=0, step=1)
# Returns an iterator that counts from start with the specified step size.

count_iterator = itertools.count(5, 2)
print(list(next(count_iterator) for _ in range(5)))  # Output: [5, 7, 9, 11, 13]


# 9. dropwhile(predicate, iterable)
# Returns an iterator that drops elements from the input iterable as long as the predicate is true,
# then yields remaining elements.

non_zero_elements = [0, 1, 2, 3]
drop_iterator = itertools.dropwhile(lambda x: x == 0, non_zero_elements)
print(list(drop_iterator))  # Output: [1, 2, 3]


# 10. filterfalse(predicate, iterable)
# Returns an iterator that filters out elements from the input iterable for which the predicate is true.

odd_numbers = [1, 2, 3, 4]
filtered_iterator = itertools.filterfalse(lambda x: x % 2 == 0, odd_numbers)
print(list(filtered_iterator))  # Output: [1, 3]


# 11. groupby(iterable[, key])
# Returns an iterator that groups elements of the input iterable based on a specified key.

students = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'C')]
for group_key, group in itertools.groupby(students):
    print(f"{group_key}: {list(group)}")
# Output:
# A: [('Alice', 'A'), ('Charlie', 'A')]
# B: [('Bob', 'B')]
# C: [('David', 'C')]


# 12. islice(iterable, stop)
# Returns an iterator that returns selected elements from the input iterable up to a specified count.

sliced_iterator = itertools.islice(range(10), 5)
print(list(sliced_iterator))  # Output: [0, 1, 2, 3, 4]


# 13. permutations(iterable, r=None)
# Returns an iterator that yields all possible permutations of the input iterable taken r at a time.
# If r is not specified, defaults to the length of the iterable.

permutations_of_all_elements = itertools.permutations(elements)
print(list(permutations_of_all_elements))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'A'),
                                                  #       ('B', 'C'), ('C', 'A')]


# 14. product(*iterables, repeat=1)
# Returns an iterator that produces the Cartesian product of input iterables.

elements = ['a', 'b']
repeated_product_iterator = itertools.product(elements, repeat=2)
print(list(repeated_product_iterator))  # Output: [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]


# 15. starmap(function, iterable)
# Returns an iterator that applies the specified function to corresponding elements from each input iterable.

numbers = [1, 2, 3]
squared_numbers = itertools.starmap(pow, [(x, 2) for x in numbers])
print(list(squared_numbers))  # Output: [1, 4, 9]


# 16. tee(iterable, n=2)
# Returns n independent iterators from a single iterable.

original_iterator = range(5)
iterator1, iterator2 = itertools.tee(original_iterator)

for i in iterator1:
    print(i)  # Output: 0, 1, 2, 3, 4

for i in iterator2:
    print(i)  # Output: 0, 1, 2, 3, 4


# 17. takewhile(predicate, iterable)
# Returns an iterator that yields elements from the input iterable as long as the predicate is true,
# then stops.

positive_numbers = [1, -2, 3, -4]
takewhile_iterator = itertools.takewhile(lambda x: x > 0, positive_numbers)
print(list(takewhile_iterator))  # Output: [1, 3]


# 18. zip_longest(*iterables, fillvalue=None)
# Returns an iterator that aggregates elements from each of the input iterables into tuples.

list1 = [1, 2]
list2 = ['a', 'b', 'c']
zipped_iterator = itertools.zip_longest(list1, list2, fillvalue='X')
print(list(zipped_iterator))  # Output: [(1, 'a'), (2, 'b'), ('X', 'c')]


# 19. chain.from_iterable(iterables)
# Similar to itertools.chain(), but takes an iterable of iterables instead.

list_of_lists = [[1, 2], [3, 4]]
chained_iterator = itertools.chain.from_iterable(list_of_lists)
print(list(chained_iterator))  # Output: [1, 2, 3, 4]


# 20. permutations(iterable, r=None)
# Returns an iterator that yields all possible permutations of the input iterable taken r at a time.
# If r is not specified, defaults to the length of the iterable.

permutations_of_all_elements = itertools.permutations(elements)
print(list(permutations_of_all_elements))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'A'),
                                                  #       ('B', 'C'), ('C', 'A')]
```

These examples cover a wide range of functionalities provided by the `itertools` module, demonstrating how to use each function effectively in Python.
