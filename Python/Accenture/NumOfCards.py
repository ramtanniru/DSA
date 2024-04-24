# Statement: Function should return number of cards required to build a pyramid pf level n.
# input: 2
# output: 7
# input: 3
# output: 15
# Method-1:
# def numOfCards(n):
#     dp = 0
#     for i in range(1,n+1):
#         dp += 3*i - 1
#     return dp
# Method-2:
def numOfCards(n):
    if n<=0:
        return 0
    return int((3*(n*(n+1))/2)-n)
n = int(input())
print(numOfCards(n))