# You are given an array of disk sizes, and while iterating through the array, you need to form towers.
# A disk can only be placed on top of a tower if the disk below it is larger than the current disk.
# Otherwise, the disk must either start a new tower or be placed on an existing one.
# Find the minimum number of towers required to accommodate all the disks under this condition.
import bisect
def solve(n,arr):
    tow = []
    for i in arr:
        pos = bisect.bisect_right(tow,i)
        if pos<len(tow):
            tow[pos] = i
        else:
            tow.append(i)
    return tow
n = int(input())
arr = [int(i) for i in input().split()]