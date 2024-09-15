# Statement: Function that returns the element of the array having least absolute difference with the given number 'n'. 
# Note: n>=0
# input: 1 2 12 13 15 17 26 30 38 45 64 72   , n = 27
# output: 26

def leastDifference(arr,n):
    ele,diff = 0,n
    for i in arr:
        if abs(i-n)<diff:
            ele,diff = i,abs(i-n)
    return ele
arr = [int(i) for i in input().split()]
n = int(input())
print(leastDifference(arr,n))