# Method-1:
def fib(n):
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]

n = int(input())
dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 1
fib(n)
print(dp)

# Method-2:
def f(n):
    if n not in d:
        d[n] = f(n-1) + f(n-2)
    return d[n]
d = {0:0,1:1}
f(int(input()))
print(list(d.values()))