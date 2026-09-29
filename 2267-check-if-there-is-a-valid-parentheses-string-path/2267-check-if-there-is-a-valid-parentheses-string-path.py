class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # 1. Quick check: A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
            
        # 2. Quick check: Cannot start with ')' or end with '('
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        memo = {}
        
        def dfs(r, c, bal):
            # Update running balance based on current cell character
            if grid[r][c] == '(':
                bal += 1
            else:
                bal -= 1
                
            # If balance goes negative, the prefix path is already invalid
            if bal < 0:
                return False
                
            # Optimization: If the balance is greater than the remaining steps to the goal,
            # it is impossible to bring the balance back down to 0.
            remaining_steps = (m - 1 - r) + (n - 1 - c)
            if bal > remaining_steps:
                return False
                
            # Base case: reached the bottom-right destination
            if r == m - 1 and c == n - 1:
                return bal == 0
                
            state = (r, c, bal)
            if state in memo:
                return memo[state]
                
            # Move Down or Right
            res = False
            if r + 1 < m:
                res = res or dfs(r + 1, c, bal)
            if c + 1 < n:
                res = res or dfs(r, c + 1, bal)
                
            memo[state] = res
            return res
            
        return dfs(0, 0, 0)
