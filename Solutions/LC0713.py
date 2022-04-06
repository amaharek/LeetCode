# https://leetcode.com/problems/subarray-product-less-than-k/submissions/
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1: 
            return 0 
        
        left,prod,ans = 0,1,0
        
        for right, val in enumerate(nums):
            prod *= val 
            
            while prod >=k: 
                prod /= nums[left]
                left += 1 
            ans += right - left + 1 
        return ans  