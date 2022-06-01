# 1570. Dot Product of Two Sparse Vectors
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
# Let n be the length of the input array and L be the number of non-zero elements.
# Time complexity: O(n) for creating the hashmap; O(L) for calculating the doct product 
# Space complexity: O(L) for creating the Hash Map, as we only store elements that are non-zero. O(1)O(1)O(1) for calculating the dot product.


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros= {}
        for i,n in enumerate(nums): 
            if n!=0: 
                self.nonzeros[i] = n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0 
        for i,n in self.nonzeros.items(): 
            if i in vec.nonzeros:
                result+=n * vec.nonzeros[i]
        return result
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)