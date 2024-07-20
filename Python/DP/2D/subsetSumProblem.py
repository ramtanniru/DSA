class Solution:
    def isSubsetSum (self, N, arr, sum):
        def rec(idx,n,dp):
            if n==0:
                return True
            if idx==0:
                return n==arr[idx]
            if dp[idx][n]!=-1: return dp[idx][n]
            notTake = rec(idx-1,n,dp)
            take = False
            if n>=arr[idx]:
                take = rec(idx-1,n-arr[idx],dp)
            dp[idx][n] = take or notTake
            return dp[idx][n]
        dp = [[-1 for i in range(sum+1)] for j in range(N)]
        return rec(N-1,sum,dp) 