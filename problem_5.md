## Blockchain ##

The solution is implemented by creating a BlockChain class that is a Linked list, the linked list is immutable and take the data as an input. A linked list is the best approach to keep track of the previous block.

### Space Complexity: O(n) ###
In each block of the BlockChain Class we are storing the data, the timestamp, the hash and also the previous hash (except for the tail). This meants that the amount of data stored increases linearly with the number of nodes in the list.

### Time Complexity: O(n) ###
In time complexity we need to define the methods that we are using.
For Add() a new block into our BlockChain class we just move the pointer in case that our tail is None, so the time complexity is O(1)
For Searching a block we found that in our worst case we will need to search through the whole BlockChain Class, in this case the time complexity is O(n)


A linkend list is the best approach to keep track of the previous block. Retrieve the last block is O(1) and getting the first block would be O(n). The Space complexity is O(n) because we are storing each of the blocks in our blockchain class.
