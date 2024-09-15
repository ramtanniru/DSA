# Statement: Function accepts an array A of size n implement the function to return the count of good integers in array A.
# An integer z is said to be good iff there exists two integers x and y such that x^3 + y^3 = z.
# input: [35,9,1]
# output: 2
def isCubicSumExist(A):
    def isGood(n):
        l,r = 0,int(n**(1/3))
        # binary search
        while l<=r:
            z = l**3 + r**3
            if z == n:
                return True
            elif z<n:
                l+=1
            elif z>n:
                r-=1
        return False
    cnt = 0
    for i in A:
        if isGood(i):
            cnt += 1
    return cnt

A = [int(i) for i in input().split()]
print(isCubicSumExist(A))