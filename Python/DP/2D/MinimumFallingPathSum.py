class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = [[float('inf') for i in range(len(A)+2)] for j in range(len(A)+1)]
        for i in range(len(dp[0])-2,0,-1):
            dp[-2][i] = A[-1][i-1]
        for i in range(len(dp)-3,-1,-1):
            for j in range(len(dp[0])-2,0,-1):
                dp[i][j] = min(dp[i+1][j],dp[i+1][j-1],dp[i+1][j+1]) + A[i][j-1]
        return min(dp[0]) 