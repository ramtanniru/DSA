def gcd(m,n):
    if m==n:
        return n
    if m>n:
        return gcd(n,m-n)
    else:
        return gcd(m,n-m)
a,b = map(int,input().split())
print(gcd(a,b))