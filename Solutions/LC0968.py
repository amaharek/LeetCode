# Complexity Analysis 
# Time Complexity: 
# As we are iterating through both the lists once, the time complexity of the above algorithm is O(N+M), 
# where ‘N’ and ‘M’ are the total number of intervals in the input arrays respectively.
# Space Complexity: 
# Ignoring the space needed for the result list, the algorithm runs in constant space O(1)


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j ,start,end= 0,0 ,0,1
        
        while i < len(firstList) and j < len(secondList):
            low = max(firstList[i][start],secondList[j][start]) # start point of intersection
            high = min(firstList[i][end],secondList[j][end])    # endpoint of intersection 
                
            if low <= high:
                result.append([low,high])
            
            # Remove interval with smallest endpoint
            if firstList[i][end] < secondList[j][end]:
                i += 1 
            else:
                j += 1 
                
        return result
        