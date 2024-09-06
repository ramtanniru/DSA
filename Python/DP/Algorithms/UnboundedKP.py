class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0 for i in range(W+1)]
        for i in range(1,len(dp)):
            for j in range(len(wt)):
                if wt[j]<=i:
                    dp[i] = max(dp[i],dp[i-wt[j]]+val[j])
        return dp[-1] 