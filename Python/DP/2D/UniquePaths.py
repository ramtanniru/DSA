class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        dp[-1][-2] = 1
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[0])-2,-1,-1):
                dp[i][j] = dp[i+1][j]+dp[i][j+1]
        return dp[0][0] 