# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Complexity analysis

#     Time complexity : O(n). Assume that nnn is the list's length, the time complexity is O(n).

#     Space complexity : O(1).

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous,current,nextTemp = None, head, None
        
        while current is not None: 
            nextTemp = current.next
            current.next = previous 
            previous = current
            current = nextTemp
        return previous

        
        
        
        