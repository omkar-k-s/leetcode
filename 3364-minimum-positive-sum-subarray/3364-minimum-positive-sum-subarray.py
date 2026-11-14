class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        min_sum = float('inf')

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                length = j - i + 1

                # Check if length is within [l, r] and sum is strictly positive
                if l <= length <= r and curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)

        return min_sum if min_sum != float('inf') else -1
