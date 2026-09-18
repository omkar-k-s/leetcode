class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            # Outside grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Water or already visited
            if grid[r][c] == '0':
                return

            # Mark as visited
            grid[r][c] = '0'

            # Visit 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count