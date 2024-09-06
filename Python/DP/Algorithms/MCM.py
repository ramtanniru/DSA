class Solution:
    def matrixMultiplication(self, N, arr):
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
        dp = [[-1 for i in range(N)] for j in range(N)]
        return mcm(1,N-1) 