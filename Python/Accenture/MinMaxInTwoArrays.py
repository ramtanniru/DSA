# Statement: Count the numbers greater than k in arr1 be x and count of numbers lesser than k in arr2 be y.
# Then return maximum of x and y form the function.
# input: 
# output: 
def minMaxInTwoArrays(arr1,arr2,k):
    x,y = 0,0
    i,j = 0,0
    while i<len(arr1) or j<len(arr2):
        if i<len(arr1):
            if arr1[i]>k:
                x += 1
        if j<len(arr2):
            if arr2[j]<k:
                y += 1
        i += 1
        j += 1
    return max(x,y)
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
k = int(input())
print(minMaxInTwoArrays(arr1,arr2,k))