class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time complexity : O(n) for filtering, reversing and comparing
        # Space complexity O(n)
        
#         filtered_chars = filter(lambda ch:ch.isalnum(), s) 
#         lowercase_filtered = map(lambda ch:ch.lower(),filtered_chars)
        
#         filtered_chars_list = list(lowercase_filtered)
#         reversed = filtered_chars_list[::-1]
#         return reversed==filtered_chars_list






        # approach 2 (two pointers):
        # time complexity : O(n) the length of n
        # space complexity : O(1) no extra space required 
        start,end = 0,len(s)-1
        while start < end: 
            while start < end and not s[start].isalnum():
                start+=1 
            while start< end and not s[end].isalnum(): 
                end-=1 
            if s[start].lower() != s[end].lower():
                return False 
            
            start+=1 
            end-=1 
            
        return True 