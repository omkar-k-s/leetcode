class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Step 1: Sort the array in non-decreasing order
        nums.sort()
        
        # Step 2: Collect all indices where the value equals target
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
                
        return result
