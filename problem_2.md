## Find Files ##

For finding files in a root directory, we are using a recursive method, because we need to explore each available path of the root.
As any recursive algorithm, there are some consequences, in terms of time complexity because each times there are multiples paths we are gonna dive until we finish all the possibles paths,  the complexity is O(n^2).
In terms of time complexity,the maximum number of stack frames are gonna be presented by the maximum depth of the recursion tree. If each function call takes O(m) space and the maximum depth of recursion is 'n' then the space complexity would be O(nm).