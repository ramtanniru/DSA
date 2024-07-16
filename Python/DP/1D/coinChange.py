class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Unbounded knapsack
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for i in range(1,len(dp)):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i],dp[i-c]+1)
        if dp[-1]==float('inf'):
            return -1
        return dp[-1] 