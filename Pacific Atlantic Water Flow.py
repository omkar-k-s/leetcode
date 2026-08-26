class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr < 0 or nr >= m or
                    nc < 0 or nc >= n):
                    continue

                if (nr, nc) in visited:
                    continue

                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visited)

        # Pacific Ocean: top row and left column
        for c in range(n):
            dfs(0, c, pacific)

        for r in range(m):
            dfs(r, 0, pacific)

        # Atlantic Ocean: bottom row and right column
        for c in range(n):
            dfs(m - 1, c, atlantic)

        for r in range(m):
            dfs(r, n - 1, atlantic)

        # Cells that can reach both oceans
        result = []

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result