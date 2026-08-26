class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # DP array initialized to 0
        dp = [0] * n
        dp[0] = 1  # Starting point

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # Obstacle blocks all paths
                elif j > 0:
                    dp[j] += dp[j - 1]  # Current + Left cell value

        return dp[n - 1]
