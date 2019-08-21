## Active Directory ##

In order to iterate through the whole directory we used a recursive function.

Because we don't know how many inner groups we will need to explore each of them until we found the user.

As any recursive algorithm, there are some consequences, in terms of time complexity because each times there are multiples groups we are gonna dive until we finish the user, in the worst case the complexity is O(n^2).
In terms of time complexity,the maximum number of stack frames are gonna be presented by the maximum depth of the recursion tree. If each function call takes O(m) space and the maximum depth of recursion is 'n' then the space complexity would be O(nm).