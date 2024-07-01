# max equilibrium index of an array 
arr = [int(i) for i in input().split()]
n = len(arr)
pre = [0]*n
post = [0]*n 
pre[0] = arr[0]
post[-1] = arr[-1]
for i in range(1,n):
    pre[i] += pre[i-1] + arr[i]
for i in range(n-2,-1,-1):
    post[i] += post[i+1] + arr[i]
for i in range(n):
    if pre[i]==post[i]:
        print(i)
        break 