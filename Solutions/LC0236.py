# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ 
# Time complexity: O(N) N is the number of nodes in the binary tree
# Space complexity: O(N) amount of space utilized by the recursion stack would be N


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        :type root:TreeNode 
        :type p:TreeNode 
        :type q:TreeNode 
        :rtype TreeNode 
        """
        def recurse_tree(current_node):
            
            # if reached the end of a branch, return False.
            if not current_node: 
                return False 
            
            # Left Recursion 
            left = recurse_tree(current_node.left)
            
            # Right Recursion 
            right = recurse_tree(current_node.right)
            
            # If the current node is one of p or q 
            mid = current_node == p or current_node ==q 
            
            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node 
            
            # Return True if either of the three bool values is True.
            return mid or left or right 
        recurse_tree(root)
        
        return self.ans