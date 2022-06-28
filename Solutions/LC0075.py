# https://leetcode.com/problems/sort-colors
# Time complexity : O(N) since it's one pass along the array of length NNN.
# Space complexity : O(1) since it's a constant space solution.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Dutch National Flag problem solution
        """
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0 
        
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums)-1
        
        while curr <= p2: 
            if nums[curr] == 0: 
                nums[p0],nums[curr] = nums[curr], nums[p0]
                p0+=1 
                curr +=1 
            elif nums[curr] == 2: 
                nums[p2],nums[curr] = nums[curr], nums[p2]
                p2 -=1 
            else:
                curr +=1 
            