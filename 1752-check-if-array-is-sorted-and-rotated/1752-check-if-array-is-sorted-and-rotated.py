class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n = len(nums)
        
        for i in range(n):
            # Check if current element is greater than the next element (circularly)
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                
            # Optimization: If we find more than 1 drop, it's immediately invalid
            if count > 1:
                return False
                
        return True
