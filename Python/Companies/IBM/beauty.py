# For an array of integers, arr[n], its prefix sum array, psum[n],
# is constructed as psum[i] = sum(arr[0]...arr[i]) where 0 ≤ i < n.
# The beauty of psum[n] is psum[0] - psum[1] + psum[2] - psum[3] +... (-1)^n-1 psum[n-1].
# You can shuffle the array in any order, print maximum possible beauty of array.

def beauty(arr):
    arr.sort()
    temp = [i for i in arr]
    i = 1
    j = 0
    while i<len(arr) and j<len(arr):
        temp[i] = arr[j]
        i += 2
        j += 1
    i = 0
    while i<len(arr) and j<len(arr):
        temp[i] = arr[j]
        i += 2
        j += 1
    temp.reverse()
    res = temp[0]
    for i in range(1,len(temp)):
        temp[i] += temp[i-1]
        if i%2==0:
            res += temp[i]
        else:
            res -= temp[i]
    return res
            
arr = [3,4,5,1,1]
print(beauty(arr))