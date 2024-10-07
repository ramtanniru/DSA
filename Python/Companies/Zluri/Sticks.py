# You are given an array of stick lengths. You can either decrease or 
# increase the length of a stick by spending an amount equal to the change in its length.
# Find the minimum amount required to equalize all the heights.

def solve(n,arr):
    arr.sort()
    med = arr[n//2]
    s = sum([abs(i-med) for i in arr])
    return s
n = int(input())
arr = [int(i) for i in input().split()]
