class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        squares=[x*x for x in nums]

        squares.sort()

        k=len(nums)//2

        return sum(squares[k:])-sum(squares[:k])
