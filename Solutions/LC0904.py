# https://leetcode.com/problems/fruit-into-baskets/
# Complexity Analysis 
# Time Complexity O(n)
# Space Complexity O(1)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start , windowSum = 0 ,0
        basket = {}
        maxlens = 0 
        
        for end in range(len(fruits)):
            right_fruit = fruits[end]
            if right_fruit not in basket: 
                basket[right_fruit] = 0 
            
            basket[right_fruit] +=1 
            
            while len(basket) > 2: 
                left_fruit = fruits[start] 
                basket[left_fruit] -=1
                
                if basket[left_fruit] == 0: 
                    del basket[left_fruit]
                    
                start+=1 
            maxlens = max(maxlens,end-start+1)
        
        return maxlens