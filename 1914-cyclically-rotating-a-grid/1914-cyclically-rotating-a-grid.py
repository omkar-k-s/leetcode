class Solution(object):
    def rotateGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):
            elements = []

            top = layer
            bottom = m - 1 - layer
            left = layer
            right = n - 1 - layer

            # Top row
            for j in range(left, right + 1):
                elements.append(grid[top][j])

            # Right column
            for i in range(top + 1, bottom + 1):
                elements.append(grid[i][right])

            # Bottom row
            for j in range(right - 1, left - 1, -1):
                elements.append(grid[bottom][j])

            # Left column
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])

            # Counter-clockwise rotation
            k1 = k % len(elements)
            elements = elements[k1:] + elements[:k1]

            index = 0

            # Top row
            for j in range(left, right + 1):
                grid[top][j] = elements[index]
                index += 1

            # Right column
            for i in range(top + 1, bottom + 1):
                grid[i][right] = elements[index]
                index += 1

            # Bottom row
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = elements[index]
                index += 1

            # Left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = elements[index]
                index += 1

        return grid