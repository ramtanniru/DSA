from collections  import deque
arr = [int(i) for i in input().split()]
d = deque(arr)
k = int(input())
k %= len(arr)
while k>0:
    x = d.popleft()
    d.append(x)
    k -= 1
print(list(d))