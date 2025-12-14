class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        dp[0][0] = 1

        for r in range(1, rows):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r - 1][0]

        for c in range(1, cols):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c - 1]

        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[rows - 1][cols - 1]


sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
