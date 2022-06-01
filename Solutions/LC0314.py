# https://leetcode.com/problems/binary-tree-vertical-order-traversal
# Time complexity: O(N) where N is the number of nodes in the tree 
# BFS O(N) for traversing the tree 
# Space complexity: O(N) for the hashtable O(N) and O(N) for the queue 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: 
            return []
        
        columnTable = defaultdict(list)
        min_column = max_column = 0 
        queue = deque([(root, 0)])
        
        while queue: 
            node,column = queue.popleft()
            
            if node is not None: 
                columnTable[column].append(node.val)
                min_column = min(min_column,column)
                max_column = max(max_column,column)
                
                queue.append((node.left,column-1))
                queue.append((node.right,column+1))
        return [columnTable[x] for x in range(min_column,max_column+1)]