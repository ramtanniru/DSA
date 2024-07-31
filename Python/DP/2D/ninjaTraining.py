class Solution:
    def maximumPoints(self, arr, n):
        # top-down memoisation
        def rec(idx,prev):
            if idx==len(arr):
                return 0
            if dp[idx][prev]!=-1:
                return dp[idx][prev]
            if prev==0:
                poss1 = arr[idx][1]+rec(idx+1,1)
                poss2 = arr[idx][2]+rec(idx+1,2)
            elif prev==1:
                poss1 = arr[idx][0]+rec(idx+1,0)
                poss2 = arr[idx][2]+rec(idx+1,2)
            else:
                poss1 = arr[idx][1]+rec(idx+1,1)
                poss2 = arr[idx][0]+rec(idx+1,0)
            dp[idx][prev] = max(poss1,poss2)
            return dp[idx][prev] 
        # tabulation
        dp = [[-1 for i in range(3)] for j in range(len(arr))]
        dp[0][0],dp[0][1],dp[0][2] = arr[0][0],arr[0][1],arr[0][2]
        for i in range(1,len(arr)):
            for j in range(3):
                if j==0:
                    poss1 = arr[i][j]+dp[i-1][1]
                    poss2 = arr[i][j]+dp[i-1][2]
                elif j==1:
                    poss1 = arr[i][j]+dp[i-1][0]
                    poss2 = arr[i][j]+dp[i-1][2]
                elif j==2:
                    poss1 = arr[i][j]+dp[i-1][1]
                    poss2 = arr[i][j]+dp[i-1][0]
                dp[i][j] = max(poss1,poss2)
        return max(dp[-1][0],dp[-1][1],dp[-1][2]) 