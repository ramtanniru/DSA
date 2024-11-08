# Imagine you are exploring a massive amusement park with n different attraction, each more exciting than the last. However these attractions come with a twist, after enjoying a ride at one attraction, you are automatically transported to a different one. Sometimes, a ride may even bring you back to the same place.

# For each attraction i (where 1<=i<=N), the ride takes you to attraction A[i]. Here's how the park is structured.
# - A[i] represents the next attraction connected to attraction.
# - It's possible that a ride from attraction 'i' takes you back to itself, i.e, A[i] = i.

# As an adventurous visitor, you are curious to find out how long it takes before you find yourself at a ride you've already experienced. Your task is to compute, for each attraction, how many rides it will take before you revisit an attraction you've already been to.

# Constraints:
# 1<N<2*10^5
# 1<A<N

# Give me python code

# Sample test case:
# n = 3
# A = [2,3,2]
# Output: [ 3 ,2, 2] 
def solve(arr,n):
    def dfs(node):
        nonlocal vis,stack,res
        if vis[node]:
            return res[node]
        vis[node] = True
        stack[node] = True
        nextNode = arr[node] - 1
        if node==2: print(res,"first")
        if res[nextNode] != -1:
            res[node] = 1 + res[nextNode]
        else:
            res[node] = 1 + dfs(nextNode)
        if node==2: print(res,"last")
        return res[node]

    vis = [False]*n
    stack = [False]*n
    res = [-1]*n
    for i in range(n):
        if not vis[i]:
            dfs(i)
    return res

n = int(input())
arr = [int(i) for i in input().split()]
print(*solve(arr,n))