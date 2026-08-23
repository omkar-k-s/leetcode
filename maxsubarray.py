class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                current_max, current_min = current_min, current_max

            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            result = max(result, current_max)

        return result