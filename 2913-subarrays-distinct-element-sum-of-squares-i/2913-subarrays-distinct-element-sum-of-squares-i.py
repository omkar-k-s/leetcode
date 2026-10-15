class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(nums)
        
        # Iterate through every possible starting index of a subarray
        for i in range(n):
            distinct_elements = set()
            # Expand the subarray to the right
            for j in range(i, n):
                distinct_elements.add(nums[j])
                # Add the square of the number of distinct elements
                total_sum += len(distinct_elements) ** 2
                
        return total_sum
