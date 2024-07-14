class Solution:
    def maximumPoints(self, points, n):
        dp = [[0 for i in range(3)] for j in range(n+1)]
        for i in range(n-1,-1,-1):
            dp[i][0] = max(dp[i+1][1],dp[i+1][2])+points[i][0]
            dp[i][1] = max(dp[i+1][0],dp[i+1][2])+points[i][1]
            dp[i][2] = max(dp[i+1][0],dp[i+1][1])+points[i][2]
        return max(dp[0]) 