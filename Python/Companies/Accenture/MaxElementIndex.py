# Statement: Function that finds index of maximum value of given array
# input: [1,2,7,5,6]
# output: 2

def findIndexOfMaxEle(arr):
    m,i = 0,0
    for idx,x in enumerate(arr):
        if m<x:
            m,i = x,idx
    return i
arr = [int(i) for i in input().split()]
print(findIndexOfMaxEle(arr)) 