# Cyclic Sort 
# Complexity Analysis
#     Time complexity : O(n log(n))
#     The only elements of the algorithm that have asymptotically nonconstant time complexity are the main for loop (which runs in O(n) time), and the sort invocation (which runs in O(nlogn) time for Python and Java). Therefore, the runtime is dominated by sort, and the entire runtime is O(nlgn).
#     Space complexity : O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if nums[-1] != len(nums): 
            return len(nums)
        elif nums[0] != 0:
            return 0 
        
        for i in range(1,len(nums)):
            expected = nums[i-1] + 1
            if nums[i] != expected:
                return expected
        return nums




# Hashset
# Complexity Analysis
#     Time complexity : O(n)
#       Because the set allows for O(1) containment queries, the main loop runs in O(n) time. 
#       Creating num_set costs O(n) time, as each set insertion runs in amortized O(1) time, so the overall runtime is O(n+n)=O(n)
#     Space complexity : O(n)

class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    