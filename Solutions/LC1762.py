# https://leetcode.com/problems/buildings-with-an-ocean-view
# Time complexity: O(N)
# Space complexity: O(1) No auxiliary space was used other than for the output array.

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # scan from right to left and keep the higest value 
        # if index is > highest value -> add 
        # else no ocean view 
        result = deque()
        tallest_building = 0
        for i in reversed(range(len(heights))):
            if heights[i] > tallest_building: 
                result.appendleft(i)
                tallest_building = heights[i]
            
        
        return result