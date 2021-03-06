# https://leetcode.com/problems/lru-cache/solution/
# Time complexity: O(1) for put and get 
# space complexity: O(capacity) capacity at most = capacity +1 

from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        """
        :type key:int 
        :rtype: int 
        """
        if key not in self: 
            return -1 
        
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        """
        :type key:int
        :type value:int 
        :retype void
        """ 
        if key in self: 
            self.move_to_end(key)
        self[key] = value 
        if len(self) > self.capacity: 
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)