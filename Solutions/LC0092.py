# Complexity Analysis

#     Time Complexity:  O(N) considering the list consists of N nodes. 
#           We process each of the nodes at most once (we don't process the nodes after the nth node from the beginning).
#     Space Complexity: O(1) since we simply adjust some pointers in the original linked list 
#           and only use O(1) additional memory for achieving the final result.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # List is consist of three parts
        # 1. From beginning to the node before left (left-1) -> should be kept as is as the last node should be saved 
        # 2. between right - left +1 (reverse the nodes) take reference of the last element 
        # 3. after right+1 to the end keep as is and connect with the sublist 
        
        # if p == q return the same LinkedList 
        if left ==right: 
            return head 
        
        # Traverse nodes of the first part 
        previous , current = None, head 
        
        i = 0 
        
        while current is not None and i < left-1: 
            previous = current 
            current = current.next 
            i += 1 
        
        # we are interested in three parts of the LinkedList, the part before index 'p',
        # the part between 'p' and 'q', and the part after index 'q'
        last_node_of_first_part = previous 
        
        # after reversing the LinkedList 'current' will become the last node of the sub-list 
        last_node_of_sublist = current 
        
        next = None  # will be used to temporarily store the next node 
        
        # reset counter to move between right - left +1 
        i = 0 
        
        # Reversing the elements between right - left 
        while current is not None and i < right - left + 1: 
            next = current.next 
            current.next = previous 
            previous = current 
            current = next 
            i+=1 
            
        # connecting the first part with the reversed sublist 
        if last_node_of_first_part is not None: 
            last_node_of_first_part.next = previous 
        else: 
            head = previous 
        
        
        # connecting the last part 
        last_node_of_sublist.next = current 
        
        
        return head 
        
            