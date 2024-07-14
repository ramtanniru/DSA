class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(obstacleGrid[0])+1)] for j in range(len(obstacleGrid)+1)]
        dp[-1][-2] = 1
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[0])-2,-1,-1):
                if obstacleGrid[i][j]!=1:
                    dp[i][j] = dp[i+1][j]+dp[i][j+1]
        return dp[0][0] 