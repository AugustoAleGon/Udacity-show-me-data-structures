## LRU CACHE ##

### Set key and value ###
In order to set a value we use a mixed between hash maps and Queue data structure. We need to check if we are under of max capacity once we reached that limit we need to be sure that we are deleting the right value that's why we need to use Queues to know which value is gonna be removed in the Hash Maps.

### Get method ###
Because we are creating a Cache Memory we need to know what is the lastest used value, that's where Queue comes out, we are gonna dequeue the lastest element and then enqueue the same element, the operation cost is O(1) because we are taking advantage of Queue operation. And we just use the hash map for retrieve the value.

### Big O Notation ###
The time complexity of each operation is O(1). Because we are getting the values from Hash Maps and we are using the Queues for sorting the elements. We made a trade off space for speed. Because we are storing each element in a HashMap and also in a Queue, so the space complexity is O(2n) that's basically O(n) store in memory.