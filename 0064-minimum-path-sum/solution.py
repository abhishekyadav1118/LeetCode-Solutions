class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        m = len(grid)

        # Initialize the first row (can only come from the left)
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # Fill the rest of the grid
        for i in range(1, m):
            # Remember to also accumulate the first column of each row!
            grid[i][0] += grid[i - 1][0]

            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
