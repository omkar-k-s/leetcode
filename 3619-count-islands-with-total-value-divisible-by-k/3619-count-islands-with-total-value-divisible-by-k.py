class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Accumulate the current cell's value
            current_sum = grid[r][c]
            # Mark the current cell as visited by setting it to 0
            grid[r][c] = 0 
            
            # Explore all 4 orthogonal directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # Check boundaries and if the neighboring cell is land (> 0)
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    current_sum += dfs(nr, nc)
                    
            return current_sum

        # Traverse the entire grid
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    # Find the total sum of the current island
                    total_value = dfs(r, c)
                    # Check if the sum is divisible by k
                    if total_value % k == 0:
                        island_count += 1
                        
        return island_count
