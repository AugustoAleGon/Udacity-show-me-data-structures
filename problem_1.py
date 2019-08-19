class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    
    def enqueue(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        self.num_elements -= 1
        return node

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.data = Queue()
        self.cache = {}
        self.size = capacity
    
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            self.reorder_cache()
            return self.cache.get(key)
        return -1
        
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.size == 0:
            return None
        if self.full_capacity():
            # We need to remove the oldest element
            remove_value = self.data.dequeue()
            self.data.enqueue(key, value)
            self.cache.pop(remove_value.key)
        else:
            self.data.enqueue(key, value)
            self.cache[key] = value
    
    def reorder_cache(self):
        new_tail = self.data.dequeue()
        self.data.enqueue(new_tail.key, new_tail.value)
    
    def full_capacity(self):
        return len(self.cache) == self.size
    
    def to_array(self):
        cache_array = []
        pointer = self.data.head
        while pointer != None:
            cache_array.append(pointer.value)
            pointer = pointer.next
        return cache_array

def test_results(tests):
    for test in tests:
        if test == False:
            print("Failed!")
            return
    print("Passed!")

def test_cache_5():
    print("Test LRU Cache with size of 5")
    our_cache = LRU_Cache(5)
    result = []
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    result.append(our_cache.to_array() == [1, 2, 3, 4])

    our_cache.get(1)       # returns 1
    result.append(our_cache.to_array() == [2, 3, 4, 1])
    our_cache.get(2)       # returns 2
    result.append(our_cache.to_array() == [3, 4, 1, 2])

    result.append(our_cache.get(9) == -1)      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    result.append(our_cache.to_array() == [3, 4, 1, 2, 5])
    our_cache.set(6, 6)
    result.append(our_cache.to_array() == [4, 1, 2, 5, 6])

    our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    test_results(result)

def test_cache_6():
    print("Test LRU with size of 6")
    our_cache = LRU_Cache(6)
    result = []
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    result.append(our_cache.to_array() == [1,2,3,4])

    our_cache.get(1)
    result.append(our_cache.to_array() == [2, 3, 4, 1])

    result.append(our_cache.get(123) == -1)
    
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    result.append(our_cache.to_array() == [2, 3, 4, 1, 5, 6])
    
    our_cache.set(7, 7)
    result.append(our_cache.to_array() == [3, 4, 1, 5, 6, 7])
    test_results(result)

def test_empty():
    print("Test LRU with zero size")
    our_cache = LRU_Cache(0)
    result = []
    our_cache.set(10, 1)
    our_cache.set(8, 2)
    our_cache.set(101, 3)
    our_cache.set(5, 17)
    result.append(our_cache.to_array() == [])
    test_results(result)

test_cache_5()
test_cache_6()
test_empty()