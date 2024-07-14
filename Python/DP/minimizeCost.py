class Solution:
    def minimizeCost(self, height, n, k):
        dp = [0 for i in range(len(height))]
        for i in range(len(height)-2,-1,-1):
            miN = float('inf')
            j = i+1
            iteration = 0
            while j<len(height) and iteration<k:
                miN = min(miN,
                abs(height[i]-height[j]) + dp[j])
                j += 1
                iteration += 1
            dp[i] = miN
        return dp[0] 
    