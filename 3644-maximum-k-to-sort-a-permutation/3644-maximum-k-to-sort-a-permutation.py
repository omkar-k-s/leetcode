
class Solution(object):
    def sortPermutation(self, nums):
        ans = -1

        for i, v in enumerate(nums):
            if i != v:
                ans &= v

        return max(ans, 0)
