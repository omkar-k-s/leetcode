class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the maximum value in the array
        max_val = max(nums)
        
        # Sum the differences between the max value and each element
        return sum(max_val - x for x in nums)
