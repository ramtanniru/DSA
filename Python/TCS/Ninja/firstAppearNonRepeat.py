# print first occuring non-repeating element in an array 
from collections import Counter
arr = [int(i) for i in input().split()]
d = Counter(arr)
for i in arr:
    if d[i]==1:
        print(i)
        break 