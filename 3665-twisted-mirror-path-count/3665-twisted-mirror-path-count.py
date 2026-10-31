class Solution(object):
    def uniquePaths(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # Memoization tables
        # memo_reflect stores: (next_r, next_c) for a given mirror entry
        memo_reflect = {}
        # memo_dfs stores: number of unique paths from empty cell (r, c) to the destination
        memo_dfs = {}
        
        def reflect(r, c, direction):
            # If out of bounds, the path becomes invalid
            if not (0 <= r < m and 0 <= c < n):
                return None
            
            # If it lands on an empty cell, this is the final destination of the move
            if grid[r][c] == 0:
                return (r, c)
                
            # Memoize the reflection path through the mirrors
            state = (r, c, direction)
            if state in memo_reflect:
                return memo_reflect[state]
            
            if direction == 'right':
                # Turned down into the cell directly below the mirror
                res = reflect(r + 1, c, 'down')
            else:
                # Turned right into the cell directly to the right of the mirror
                res = reflect(r, c + 1, 'right')
                
            memo_reflect[state] = res
            return res

        def dfs(r, c):
            # Base case: reached the bottom-right corner
            if r == m - 1 and c == n - 1:
                return 1
                
            if (r, c) in memo_dfs:
                return memo_dfs[(r, c)]
            
            total_paths = 0
            
            # Option 1: Try to move right
            dest_right = reflect(r, c + 1, 'right')
            if dest_right:
                total_paths = (total_paths + dfs(dest_right[0], dest_right[1])) % MOD
                
            # Option 2: Try to move down
            dest_down = reflect(r + 1, c, 'down')
            if dest_down:
                total_paths = (total_paths + dfs(dest_down[0], dest_down[1])) % MOD
                
            memo_dfs[(r, c)] = total_paths
            return total_paths

        return dfs(0, 0)
