class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for i in range(len(grid[0])+1)] for j in range(len(grid)+1)]
        dp[-1][-2] = 0
        dp[-2][-1] = 0
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[0])-2,-1,-1):
                dp[i][j] = min(dp[i+1][j],dp[i][j+1])+grid[i][j]
        return dp[0][0] 