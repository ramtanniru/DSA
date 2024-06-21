arr = [1,4,5,7,8]
l,r = 0,len(arr)-1
search = 3
while l<r:
    mid = (l+r)//2
    if arr[mid]==search:
        print(mid)
        break
    elif arr[mid] > search:
        r = mid
    else: 
        l = mid
print(l+1)
    