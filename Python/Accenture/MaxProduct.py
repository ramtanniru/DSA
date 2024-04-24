# Statement: find maximum product of two numbers a and b where a lies in range l1<=a<=r1 and b lies in l2<=b<=r2
# input: 1 3 -2 6
# output: 18

def findMaxProd(arr):
    l1,r1,l2,r2 = arr
    return max(l1*l2,r1*r2,l1*r2,r1*l2)
arr = [int(i) for i in input().split()]
print(findMaxProd(arr))