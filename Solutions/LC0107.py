# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/ 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Time complexity#

# The time complexity O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

# Space complexity#
# The space complexity is O(N) as we need to return a list containing the level order traversal. O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = deque()
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        
        while queue: 
            level_length = len(queue)
            currentLevel = [] 
            for i in range(level_length):
                currentNode = queue.popleft() 
                currentLevel.append(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right: 
                    queue.append(currentNode.right)
                    
            result.appendleft(currentLevel)
        return result
