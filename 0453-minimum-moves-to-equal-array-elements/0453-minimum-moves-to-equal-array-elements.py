class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the minimum element in the array
        min_val = min(nums)
        
        # Calculate the total moves needed by summing up the differences
        return sum(num - min_val for num in nums)
