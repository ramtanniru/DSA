# Find minimum number of boats required to transport people. You are given an array of people weights and weight limit for a boat.

def solve(n,arr,k):
    boats = 0
    i,j = 0,n-1
    while i<=j:
        curr = 0
        while i<=j and curr+arr[j]<=k:
            curr += arr[j]
            j -= 1
        while i<=j and curr+arr[i]<=k:
            curr += arr[i]
            i += 1
        boats += 1
    return boats
n = int(input())
arr = [int(i) for i in input().split()]
k = int(input())