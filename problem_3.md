## Huffman Coding ##
For this complex problem, we are gonna analyze each used method in order to get the time/space complexity.

### Char Frequence ###
Create a dictionary that contains the frequence of each character. So we will need to iterate through all the sentece and store it in the dictionary so the time and space complexity will be O(n).

### Sort Char ###
Takes a dictionary and sort it by frequence and returns a tuple as an output. The time complexity of the sort function is O(n)*log(n) and the space complexity is O(n).

### Insert Element ###
Insert a new element in the sorted list, this is a helper method. Time complexity and space complexity O(n).

### Huffman Encoding ###
Creates the tree, using the helpers methods. This operation remove all the elements from the list and creates the huffman tree, the complexity of this operation is O(n), but one of the helpers methods has a bigger O notation. So the time complexity of encoding is O(n)*log(n).

### Encode Tree ###
Generates the binary code for each char in the huffman tree. The enconde tree iterates through the whole tree using the root key and assigned a string value.

### Huffman Decoding ###
Decode the data and the Huffman tree and returns the sentences that we encode in the previous function. We iterate through the whole tree using a recursive function. The complexity of this in time is O(n)