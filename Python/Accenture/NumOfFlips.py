# Statement: Find the number of bits to be flipped in the elements of given array to get 0 when all elements are operated by '&'.
# input: 4 4 4
# output: 1
def numOfFlips(a):
    cnt = 0
    if a:
        i = a[0]
        j = 1
        while j<len(a):
            i = i&a[j]
            j += 1
        for k in "{0:b}".format(i):
            if k=='1':
                cnt += 1
    return cnt
a = [int(i) for i in input().split()]
print(numOfFlips(a))