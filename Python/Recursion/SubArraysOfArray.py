def possibleSubArraysOfArray(array):
    if len(array)==0:
        return -1
    i,j = 0,0
    while i<len(array) and j<len(array):
        j+=1
        print(array[i:j])
    return possibleSubArraysOfArray(array[1:])
arr = [i for i in input().split()]
print(possibleSubArraysOfArray(arr))