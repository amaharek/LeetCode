# https://leetcode.com/problems/product-of-array-except-self/submissions/
# Time complexity: O(N) for traversing the list two times O(N) + O(N)
# Space complexity: O(1) since we don't use additional array for computations. 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Length of the input array 
        length = len(nums)
        
        # Initialize the answer array (output)
        answer = [0] * length 
        
        # left -> right 
        # answer[i] should contain the product of all elements to the left except answer[i] 
        # Note: for the element at index '0', there are no elements to the left so answer[0] = 1
        answer[0] = 1 
        for i in range(1,length): 
            item = nums[i]
            answer[i] = answer[i-1] * nums[i-1]
        
        
        # Right -> Left 
        # R contain the product of all elements to the right
        # R at last element should equal 1 
        R = 1
        for i in reversed(range(length)): 
            answer[i] = answer[i] * R 
            R *= nums[i]
        
        return answer 