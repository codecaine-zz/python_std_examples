# heapq — Heap queue algorithm

Here's an example of how you can use the `heapq` module in Python:

```python
import heapq

# Create a heap and push elements onto it
def create_heap():
    # Create a list to serve as the heap
    heap = []
    
    # Push elements onto the heap
    for i in range(10):
        heapq.heappush(heap, i)
        
    print("Initial Heap:", heap)

# Create a heap and pop elements from it
def pop_from_heap():
    # Create a list to serve as the heap
    heap = []
    
    # Push elements onto the heap
    for i in range(10):
        heapq.heappush(heap, i)
        
    print("Initial Heap:", heap)
    
    # Pop an element from the heap
    popped_element = heapq.heappop(heap)
    print("Popped Element:", popped_element)

# Create a heap and peek at the top element without removing it
def peek_top_of_heap():
    # Create a list to serve as the heap
    heap = []
    
    # Push elements onto the heap
    for i in range(10):
        heapq.heappush(heap, i)
        
    print("Initial Heap:", heap)
    
    # Peek at the top element without removing it
    try:
        top_element = heapq._heapify_max(heap)  # Note: _heapify_max is used to peek max heap
        print("Top Element:", top_element)
    except IndexError:
        print("Heap is empty")

# Create a min-heap and convert it to a max-heap
def convert_to_max_heap():
    # Create a list to serve as the min-heap
    min_heap = [1, 3, 5, 7, 9]
    
    print("Initial Min-Heap:", min_heap)
    
    # Convert the min-heap to a max-heap
    max_heap = []
    for element in min_heap:
        heapq.heappush(max_heap, -element)  # Note: Negative values are used to simulate max heap
    
    print("Max Heap after Conversion:", max_heap)

# Create a heap from a list and then convert it back to the original list
def create_and_convert_heap():
    # Create a list to serve as the input data
    data = [1, 3, 5, 7, 9]
    
    print("Initial Data:", data)
    
    # Create a heap from the data
    heapq.heapify(data)
    
    print("Heap after Creation:", data)

# Example usage:
create_heap()
pop_from_heap()
peek_top_of_heap()
convert_to_max_heap()
create_and_convert_heap()
```

In this code:

1.  We create a heap using `heapq.heappush(heap, element)` and pop elements from it using `heapq.heappop(heap)`.
2.  We peek at the top element without removing it by using `_heapify_max` (which is used to create or modify a max-heap).
3.  We convert a min-heap to a max-heap by pushing negative values onto the heap.
4.  We create a heap from a list and then convert it back to the original list using `heapq.heapify(data)`.
