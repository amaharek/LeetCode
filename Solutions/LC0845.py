# https://leetcode.com/problems/longest-mountain-in-array/
# Time complexity: O(N)
# Space complexity: O(1)

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        
        ans = base = 0 
        
        while base < N:
            
            end = base
            
            #if base is a left-boundary
            if end + 1 < N and A[end] < A[end + 1]: 
                #set end to the peak of this potential mountain
                while end+1 < N and A[end] < A[end+1]:
                    end += 1
                #if end is really a peak..
                if end + 1 < N and A[end] > A[end + 1]: 
                    
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans
                   
            
            
            
            
            