class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def rec(idx,amount,dp):
            if idx==0:
                if amount%coins[idx]==0:
                    return 1
                return 0
            if dp[idx][amount]!=-1: return dp[idx][amount]
            notTake = rec(idx-1,amount,dp)
            take = 0
            if coins[idx]<=amount:
                take = rec(idx,amount-coins[idx],dp)
            dp[idx][amount] = take+notTake
            return dp[idx][amount] 
        dp = [[-1 for i in range(amount+1)] for j in range(len(coins))]
        return rec(len(coins)-1,amount,dp) 