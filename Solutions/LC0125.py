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
        i,j = 0,len(s)-1
        while i < j: 
            while i < j and not s[i].isalnum():
                i+=1 
            while i< j and not s[j].isalnum(): 
                j-=1 
            if s[i].lower() != s[j].lower():
                return False 
            
            i+=1 
            j-=1 
            
        return True 