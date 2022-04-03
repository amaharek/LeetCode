# Complexity Analysis
#   Time Complexity: O(N), where N is the length of A.
#   Space Complexity: O(N) if you take output into account and O(1) otherwise.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n 
        left = 0 
        right = n-1 
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -=1
            else: 
                square = nums[left]
                left +=1
                
            result[i] = square * square 
            
        return result 
            