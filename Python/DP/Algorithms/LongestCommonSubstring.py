class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp =[[0 for i in range(m+1)] for j in range(n+1)]
        res = 0
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if S1[i-1]==S2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    res = max(res,dp[i][j])
                else:
                    dp[i][j] = 0
        return res 