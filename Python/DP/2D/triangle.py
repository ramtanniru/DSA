class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for i in range(len(triangle)+1)] for j in range(len(triangle)+1)]
        for i in range(len(dp)-2,-1,-1):
            for j in range(i,-1,-1):
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0] 