class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # dp[i][j] will store a set of all possible XOR values to reach cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Base case: starting cell
        dp[0][0].add(grid[0][0])
        
        # Fill the first row (can only come from the left)
        for j in range(1, n):
            for val in dp[0][j-1]:
                dp[0][j].add(val ^ grid[0][j])
                
        # Fill the first column (can only come from above)
        for i in range(1, m):
            for val in dp[i-1][0]:
                dp[i][0].add(val ^ grid[i][0])
                
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                # From top neighbor
                for val in dp[i-1][j]:
                    dp[i][j].add(val ^ grid[i][j])
                # From left neighbor
                for val in dp[i][j-1]:
                    dp[i][j].add(val ^ grid[i][j])
                    
        # The answer is the smallest XOR value achieved at the destination
        return min(dp[m-1][n-1])
