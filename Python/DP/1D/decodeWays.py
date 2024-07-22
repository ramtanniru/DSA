class Solution:
    def numDecodings(self, s: str) -> int:
        def rec(dp,idx=0,res=""):
            nonlocal s
            if idx==len(s):
                return 1
            if dp[idx]!=-1:
                return dp[idx]
            if s[idx]!='0':
                if idx<len(s)-1 and s[idx+1]=='0':
                        way1 = 0
                else:
                    way1 = rec(dp,idx+1,res+s[idx])
            else:
                return 0
            if idx<len(s)-1 and 0<int(s[idx:idx+2])<=26:
                way2 = rec(dp,idx+2,res+s[idx:idx+2])
            else:
                way2 = 0
            dp[idx] = way1+way2 
            return dp[idx]
        dp = [-1 for i in range(len(s)+1)]
        rec(dp) 
        if dp[0] == -1:
            return 0
        return dp[0] 