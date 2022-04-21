# https://leetcode.com/problems/excel-sheet-column-number/solution/
# time complexity O(N)
# Space complexity O(1)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0 
        n = len(columnTitle)
        for i in range(n):
            result = result * 26 
            result += ((ord(columnTitle[i])) - ord('A')+1)
        return result 