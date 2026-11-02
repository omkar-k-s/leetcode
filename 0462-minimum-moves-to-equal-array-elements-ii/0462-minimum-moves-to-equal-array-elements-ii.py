class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Sort the array to easily find the median
        nums.sort()
        
        # Step 2: Find the median element
        median = nums[len(nums) // 2]
        
        # Step 3: Calculate the total moves required to bring each element to the median
        moves = 0
        for num in nums:
            moves += abs(num - median)
            
        return moves
