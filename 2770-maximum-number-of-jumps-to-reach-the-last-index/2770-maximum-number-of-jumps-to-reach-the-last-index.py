class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        # dp[i] will store the maximum jumps to reach index i
        dp = [-1] * n
        dp[0] = 0  # Base case: 0 jumps to start at index 0
        
        # Traverse each index
        for i in range(n):
            # If the current index is unreachable, skip it
            if dp[i] == -1:
                continue
                
            # Check all possible forward jumps from index i
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
                    
        return dp[n - 1]
