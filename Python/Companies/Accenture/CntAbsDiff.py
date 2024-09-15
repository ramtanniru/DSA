# Statement: Function that returns count of elements in an array having absolute difference with n <= k.
# input: 12 3 14 56 77 13
#         13 2
# output: 3
def cntAbsDiff(arr,n,k):
    cnt = 0
    for i in arr:
        if abs(n-i)<=k:
            cnt += 1
    return cnt
arr = [int(i) for i in input().split()]
n,k = map(int,input().split())
print(cntAbsDiff(arr,n,k))