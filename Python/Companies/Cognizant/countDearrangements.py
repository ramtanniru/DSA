# count dearrangements of size n
n = int(input())
def sol(n):
    if n==1 or n==2:
        return n-1
    a,b = 0,1
    for i in range(3,n+1):
        cur = (i-1)*(a+b)
        a = b
        b = cur
    return b
print(sol(n))