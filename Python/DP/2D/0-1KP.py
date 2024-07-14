class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, pr, n):
        dp = [[0 for i in range(W+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-wt[i-1]] + pr[i-1])
        return dp[-1][-1] 