class Solution:
    def climbStairs(self, n: int) -> int:
        l = [1]*(n+1)
        for i in range(2,n+1):
            l[i] = l[i-1] + l[i-2]
        return l[-1]