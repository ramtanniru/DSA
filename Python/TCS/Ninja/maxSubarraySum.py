# print sum of subarray with maximum sum 
arr = [int(i) for i in input().split()]
k = int(input())
for i in range(1,len(arr)):
    arr[i] += arr[i-1]
maxSum = 0
i,j = 0,k-1
while j<len(arr):
    s = arr[j]-arr[i-1] if i>0 else arr[j]
    maxSum = max(maxSum,s)
    i += 1
    j += 1
print(maxSum) 