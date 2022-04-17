# https://leetcode.com/problems/powx-n/discuss/738830/Python-recursive-O(log-n)-solution-explained
# https://leetcode.com/problems/powx-n/
# Time complexity : O(logn)
# Space complexity : O(log⁡n). For each computation, we need to store the result of x^n/2. We need to do the computation for O(log⁡n) times, so the space complexity is O(log⁡n). 

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(x) < 1e-40: 
            return 0 
        if n == 0: 
            return 1
        if n < 0: 
            return self.myPow(1/x, -n)
        half = self.myPow(x, n//2)
        
        if n % 2 == 0: 
            return half*half
        if n % 2 == 1: 
            return half*half*x