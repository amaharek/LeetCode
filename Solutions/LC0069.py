# https://leetcode.com/problems/sqrtx/solution/
# Complexity Analysis 
# Time complexity O(log N)
# Space Complexity O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: 
            return x 
        
        left, right = 2, x//2 
        
        while left <= right: 
            pivot = left + (right - left ) // 2 
            num = pivot * pivot 
            
            if num > x: 
                right = pivot - 1 
            elif num < x: 
                left = pivot + 1 
            else: 
                return pivot 
            
        return right 


        
#         Newton's Method O(log(N)) time complexity, O(1) space complexity  
#         https://en.wikipedia.org/wiki/Newton%27s_method#Square_root 
#         x0 = x
#         x1 = (x0 + x / x0) / 2
#         while abs(x0 - x1) >= 1:
#             x0 = x1
#             x1 = (x0 + x / x0) / 2        
            
#         return int(x1)