
class Solution:
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = {}

        for x in nums:
            dp[x + 1] = dp.get(x, 0) + 1
            dp[x] = dp.get(x - 1, 0) + 1

        return max(dp.values())
