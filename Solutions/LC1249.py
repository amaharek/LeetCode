# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/solution/
# Time complexity: O(n), where n is the length of the input string.

# There are 3 loops we need to analyze. We also need to check carefully for any library functions that are not constant time.

# The first loop iterates over the string, and for each character, either does nothing, pushes to a stack or adds to a set. Pushing to a stack and adding to a set are both O(1). Because we are processing each character with an O(1) operation, this overall loop is O(n).

# The second loop (hidden in library function calls for the Python code) pops each item from the stack and adds it to the set. Again, popping items from a stack is O(1), and there are at most nnn characters on the stack, and so it too is O(n).

# The third loop iterates over the string again, and puts characters into a StringBuilder/ list. Checking if an item is in a set and appending to the end of a String Builder or list is O(1). Again, this is O(n) overall.


# space complexity: O(n), where n is the length of the input string.
# We are using a stack, set, and string builder, each of which could have up to n characters in them, and so require up to O(n) space.
    
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexs_to_remove = set()
        
        stack = []
        
        for i, c in enumerate(s): 
            if c not in "()":
                continue 
            if c == "(":
                stack.append(i)
            elif not stack: 
                indexs_to_remove.add(i)
            else: 
                stack.pop() 
            
                
        indexs_to_remove = indexs_to_remove.union(set(stack)) 
        string_builder = [] 
        for i , c in enumerate(s):
            if i not in indexs_to_remove: 
                string_builder.append(c)
        return "".join(string_builder)