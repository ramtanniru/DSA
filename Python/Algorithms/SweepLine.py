class Solution:
    def findMaxDeparture(self,intervals):
        maX = 0
        for arr,dep in intervals:
            maX = max(maX,dep)
        return maX
    def sweepLine(self,intervals):
        maxLen = self.findMaxDeparture(intervals)
        cache = [0]*(maxLen+2)
        ans = 0
        platforms = 0
        for arr,dep in intervals:
            cache[arr] += 1
            cache[dep+1] -= 1
        for i in range(maxLen+2):
            platforms += cache[i]
            ans = max(ans,platforms)
        return ans