# https://leetcode.com/problems/subarray-product-less-than-k/submissions/
# Time complexity: O(n)
# Space complexity: O(1)
# nums = [10,5,2,6], k = 100
# 10 -> prod=10, ans = 0-0+1 = 1 
# 5 -> prod=50,ans=1+1-0+1 = 3 
# 2 -> prod = 100 -> while loop -> prod = 100/10 = 10, left=1 -> ans = 3+2-1+1 = 5 
# 6 -> prod = 10 * 6 = 60 , ans = 5 + 3-1+1 = 8 

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1: 
            return 0 
        prod = 1 
        
        ans = left = 0
        
        for right, val in enumerate(nums):
            prod *= val 
            
            while prod >=k: 
                prod /= nums[left]
                left += 1 
            ans += right - left + 1 
        return ans 