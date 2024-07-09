# count the numbers which have strictly smaller elements to its left in an array
def cnt(arr):
    maX = float('-inf')
    res = 0
    for i in arr:
        if i>maX:
            maX = i
            res += 1
    return res 
arr = [int(i) for i in input().split()]
print(cnt(arr)) 