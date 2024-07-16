class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maX = prices[-1]
        pr = 0
        for i in prices[::-1]:
            if i<maX:
                pr = max(pr,maX-i)
            else:
                maX = i
        return pr 