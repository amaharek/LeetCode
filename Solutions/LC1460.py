class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #  Time and space complexity: O(n)       
        return collections.Counter(target) == collections.Counter(arr)