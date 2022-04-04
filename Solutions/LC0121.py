# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/
#     Time complexity: O(n)O(n)O(n). Only a single pass is needed.
#     Space complexity: O(1)O(1)O(1). Only two variables are used.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0 
        for i in range(len(prices)):
            if prices[i] < minPrice: 
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit: 
                maxProfit = prices[i]  - minPrice
        
        return maxProfit
                