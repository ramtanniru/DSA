# Statement: Function returns number of odd length numbers in the range of [1,n].
# input: 15
# output: 9
import math
def numOfOddLength(n):
    cnt = 0
    for i in range(1,n):
        if (int(math.log(i,10)+1)%2)!=0:
            cnt += 1
    return cnt
n = int(input())
print(numOfOddLength(n))