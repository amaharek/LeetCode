# https://leetcode.com/problems/merge-sorted-array/
# Time complexity: O(n+m)
# Space complexity O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # iterating backwards: i to iterate m and j to iterate n 
        i, j = m-1, n-1
        
        
        for p in range(n+m-1,-1,-1):
            # if nums2 is empty 
            if j < 0 : 
                break
            if i >= 0 and nums1[i] >= nums2[j]: 
                nums1[p] = nums1[i]
                i-=1
            else: 
                nums1[p] = nums2[j]
                j-=1
