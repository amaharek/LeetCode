# Using hashmap 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = {}
        for ind, num in enumerate(nums):
            if target - num in hist: 
                return [hist[target-num],ind]
            hist[num] = ind