class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        i,j = 0,1
        while j<len(prices):
            if prices[j]>prices[i]:
                ans = max(ans,prices[j]-prices[i])
                j += 1
            else:
                i += 1
                j = i+1
        return ans