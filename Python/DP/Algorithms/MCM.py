class Solution:
    def matrixMultiplication(self, N, arr):
        # top-down memoisation
        def mcm(i,j):
            if i==j:
                return 0
            if dp[i][j]!=-1: return dp[i][j]
            res = float('inf')
            for k in range(i,j):
                temp = arr[i-1]*arr[k]*arr[j] + mcm(i,k) + mcm(k+1,j)
                res = min(res,temp)
            dp[i][j] = res
            return dp[i][j]
        dp = [[float('inf') for i in range(N)] for j in range(N)]
        # tabulation
        for i in range(len(dp)): dp[i][i] = 0
        for i in range(len(dp)-1,0,-1):
            for j in range(i+1,len(dp[0])):
                for k in range(i,j):
                    temp = arr[i-1]*arr[k]*arr[j] + dp[i][k] + dp[k+1][j]
                    dp[i][j] = min(dp[i][j],temp)
        return dp[1][N-1] 