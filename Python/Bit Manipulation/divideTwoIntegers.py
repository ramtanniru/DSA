class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 0
        if dividend==divisor:
            return 1
        if dividend==0:
            return 0
        if (dividend>=0 and divisor>0) or (dividend<=0 and divisor<0):
            sign = 1
        n,d = abs(dividend),abs(divisor)
        ans = 0
        while n>=d:
            cnt = 0
            while d<<(cnt+1)<n:
                cnt+=1
            n -= d<<cnt
            ans += 1<<cnt
        if sign and ans==2**31:
            return (2**31)-1
        return ans if sign else -ans 