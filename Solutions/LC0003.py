
# https://leetcode.com/problems/longest-substring-without-repeating-characters 
# Time complexity: O(2n) = O(n)
# Space complexity : O(min(m,n)) 
# We need O(k) space for the sliding window, where k is the size of the Set. 
# The size of the Set is upper bounded by the size of the string nnn and the size of the charset/alphabet mmm. 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128 
        
        left = right = 0 
        
        res = 0 
        # ord function returns a string represent the unicode of a character
        while right < len(s):
            r = s[right]
            chars[ord(r)] +=1 
            
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res
                        
            
        