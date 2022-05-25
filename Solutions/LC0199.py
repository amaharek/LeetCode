# https://leetcode.com/problems/binary-tree-right-side-view/submissions/ 
# Time complexity O(N) since one has to visit each node. 
# space complexity O(D) to keep the queues, where DDD is a tree diameter. Let's use the last level to estimate the queue size.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []
        
        next_level = deque([root,])
        
        rightside = []
        
        while next_level: 
            #prepare for the next level 
            curr_level =  next_level
            next_level = deque()
            
            while curr_level:
                node = curr_level.popleft()
                
                #add child nodes of the current level 
                # in the queue for the next level 
                
                if node.left: 
                    next_level.append(node.left)
                    
                if node.right: 
                    next_level.append(node.right)
                    
            # The current level is finished 
            # Its last element is the rightmost one
            
            rightside.append(node.val)
        
        return rightside 
        