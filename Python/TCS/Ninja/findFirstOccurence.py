# find first occurence of target in sorted array 
arr = [int(i) for i in input().split()]
target = int(input())
l,r = 0,len(arr)-1
res = -1
while l<=r:
    mid = (l+r)//2
    if arr[mid]==target:
        res = mid
        r = mid - 1   
    elif arr[mid]<target:
        l = mid + 1
    else:
        r = mid - 1
print(res)
def recursion(arr,target,l=0,r=len(arr)-1,res = -1):
    if l>r:
        return res
    mid = (l+r)//2
    if arr[mid]==target:
        res = mid
        r = mid - 1
    elif arr[mid]<target:
        l = mid + 1
    else:
        r = mid - 1
    return recursion(arr,target,l,r,res)
print(recursion(arr,target)) 
    