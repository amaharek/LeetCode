# https://leetcode.com/problems/path-sum-ii/solution/ 

# Time complexity:  O(N^2) where N is the total number of nodes in the tree 
# The algorithm traverse every node once O(N) 
# For eveery leaf, O(N) operations of copying over thee currentPath 

# Space complexity: If we ignore the space required for the allPaths list, the space complexity of the above algorithm will be O(N) in the worst case. 
# This space will be used to store the recursion stack. The worst-case will happen when the given tree is a linked list (i.e., every node has only one child).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_paths_recursive(self, currentNode, targetSum, currentPath, allPaths): 
        if currentNode is None: 
            return 
        
        currentPath.append(currentNode.val)
        
        if currentNode.val == targetSum and currentNode.left is None and currentNode.right is None: 
            allPaths.append(list(currentPath)) 
        else: 
            #traverse the left sub-tree 
            self.find_paths_recursive(currentNode.left,targetSum-currentNode.val,currentPath,allPaths)
            
            #traverse the right sub-tree 
            self.find_paths_recursive(currentNode.right,targetSum-currentNode.val,currentPath,allPaths)
        
        # del the currentNode from the Path as we are going back up 
        del currentPath[-1]
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allPaths = []
        self.find_paths_recursive(root,targetSum,[],allPaths)
        return allPaths
        