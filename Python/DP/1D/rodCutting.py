class Solution:
    def cutRod(self, price, n):
        dp = [0 for i in range(n+1)]
        for rods in range(1,len(dp)):
            for idx in range(len(price)):
                if rods>=idx+1:
                    dp[rods] = max(dp[rods],dp[rods-idx-1]+price[idx])
        return dp[-1] 