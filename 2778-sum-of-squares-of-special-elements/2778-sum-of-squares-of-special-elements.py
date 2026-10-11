class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = 0
        
        # Iterate through 1-indexed positions
        for i in range(1, n + 1):
            # Check if i divides n
            if n % i == 0:
                # Map 1-indexed 'i' back to 0-indexed 'i - 1'
                total_sum += nums[i - 1] ** 2
                
        return total_sum
