# print next greater element of the elements in the array 
def nextGreater(arr):
    res = []
    stk = [arr[-1]]
    for i in range(len(arr)-2,-1,-1):
        if stk[-1]>arr[i]:
            res.append(stk[-1])
            stk.append(arr[i])
        else:
            while stk and stk[-1]<=arr[i]:
                stk.pop()
            res.append(stk[-1])
            stk.append(arr[i])
    res = res[::-1]
    res.append(-1)
    return res 

            
arr = [int(i) for i in input().split()]
print(nextGreater(arr)) 