# Ram wants to travel a grid and collect gold he can move only right or down.
# Now he has a previlege to double one of gold element found in his path. Print maximum gold found at end of his path.

# input:

# 3 3
# 1 3 1
# 1 5 1
# 4 2 1

# output: 17

# path is 1->3->5->2->1 and maximum element in this path is 5. after doubling it path is 1->3->10->2->1.
# Now sum is 17.

class Solution:
    def __init__(self) -> None:
        self.res = float('-inf')
    def findMaximumGold(self,grid) -> int:
        def findMax(a,b):
            if a[0]>b[0]:
                return a
            return b
        dp = [[(0,0) for i in range(len(grid[0])+1)] for j in range(len(grid)+1)]
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[0])-2,-1,-1):
                temp = findMax(dp[i+1][j],dp[i][j+1])
                dp[i][j] = (grid[i][j]+temp[0],max(grid[i][j],temp[1]))
        return dp[0][0][0]+dp[0][0][1]

m,n = map(int,input().split())
grid = [[int(i) for i in input().split()] for j in range(m)]
x = Solution()
print(x.findMaximumGold(grid)) 