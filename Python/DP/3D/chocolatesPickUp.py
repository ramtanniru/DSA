class Solution:
    def solve(self, n, m, grid):
        def rec(i=0,j=0,k=len(grid[0])-1):
            if not 0<=j<len(grid[0]) or not 0<=k<len(grid[0]):
                return 0
            if i==len(grid)-1:
                if j==k:
                    return grid[i][j]
                return grid[i][j]+grid[i][k]
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            res = 0
            for d1 in range(-1,2):
                for d2 in range(-1,2):
                    if 0<=j+d1<len(grid[0]) and 0<=k+d2<len(grid[0]):
                        if j!=k:
                            res = max(res,grid[i][j]+grid[i][k]+rec(i+1,j+d1,k+d2))
                        else:
                            res = max(res,grid[i][j]+rec(i+1,j+d1,k+d2))
            dp[i][j][k] = res
            return dp[i][j][k]
        dp = [[[-1 for k in range(len(grid[0]))] for j in range(len(grid[0]))] for i in range(len(grid))]
        return rec() 