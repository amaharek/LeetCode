# https://leetcode.com/problems/top-k-frequent-elements/
# Time coplexity: O(N log k)  
# Space complexity : O (N + K)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time 
        
        if k == len(nums):
            return nums
        
        # 1. build hash map: character and how often it apears 
        # O(n) time 
        count = Counter(nums)
        
        # 2-3. build heap of top k frequent elements and 
        # convert it into an output array 
        # o(N log k) time 
        return heapq.nlargest(k,count.keys(),key=count.get)