import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :type rtype: int
        """
        # Sort arr2 to enable binary search
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find the insertion index for the lower bound (x - d)
            idx = bisect.bisect_left(arr2, x - d)
            
            # If the element at idx is within the range [x - d, x + d], 
            # it violates the condition.
            if idx < len(arr2) and arr2[idx] <= x + d:
                continue
                
            # If no element is within the range, increment the counter
            distance_value += 1
            
        return distance_value
