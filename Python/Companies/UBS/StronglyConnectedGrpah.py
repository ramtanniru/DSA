'''
## Problem:-
Given a tree like graph and a stronglyConnected array where each index i and arr[i] = 1 represents i+1 node as strongly connected.
Return an array containing max difference of strongly connected and weakly connected nodes.

# INPUT:
 -> From [1,1,1]
 -> To   [2,3,4]
 -> StronglyConnected = [0,0,1,0]

# OUTPUT:
 -> [0,-1,1,-1]

# EXPLANATION:
 absolute difference is calculated as abs( numOfStronglyConnected - numOfWeaklyConnected )
 -> For node(1) best path is 1->(3) and difference in this path is abs(1-1) = 0
 -> For node(2) best path is 2->1->(3) and difference in this path is abs(1-2) = -1
 -> For node(3) best path is (3) and difference in this path is abs(1) = 1
 -> For node(4) best path is 4->1->(3) and difference in this path is abs(1-2) = -1
'''

from collections import defaultdict
def solve(n,From,To,StronglyConnected):
    cost = [[float('inf') for i in range(n)] for j in range(n)]
    strong = [i for i,x in enumerate(StronglyConnected) if x==1]
    res = [0 for i in range(n)]
    for u,v in zip(From,To):
        u -= 1
        v -= 1
        cost[u][v] = 1
        cost[v][u] = 1
    for i in range(n):
        cost[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])
    for i in range(n):
        miN = float('inf')
        for s in strong:
            miN = min(miN,cost[i][s]-1)
        res[i] = miN
    return res

n = int(input())
From = [int(i) for i in input().split()]
To = [int(i) for i in input().split()]
StronglyConnected = [int(i) for i in input().split()]
print(solve(n,From,To,StronglyConnected))

'''

4
1 1 1
2 3 4
0 0 1 0

'''