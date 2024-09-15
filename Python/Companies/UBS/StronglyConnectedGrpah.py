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

class Solution:
    def __init__(self):
        self.res = []
    
    def getStronglyConnectedComponents(self,n,From,To,StronglyConnected):

        def maxSumSubarray(arr):

            for i,x in enumerate(arr):
                arr[i] = StronglyConnected[x-1]

            s = 0
            maxSum = -1
            for i in arr:
                s += i
                maxSum = max(maxSum,s)
                if s<0:
                    break
            return maxSum

        def dfs(node,s,path):
            if node not in s:
                s.add(node)
                path += [node]
                for child in adj[node]:
                    if child not in s:
                        dfs(child,s,path)
                        s.remove(child)
                        path.pop()
                print("Path",path)
                val = maxSumSubarray(path[:])
                self.res[path[0]] = max(self.res[path[0]],val)
                print(self.res)
            return

        adj = defaultdict(list)
        for i in range(len(From)):
            adj[From[i]].append(To[i])
            adj[To[i]].append(From[i])

        for i,x in enumerate(StronglyConnected):
            if x==0:
                StronglyConnected[i] = -1

        for i in range(n+1):
            self.res.append(-1)

        for i in range(n):
            dfs(i+1,set(),[])
        
        return self.res[1:]


if __name__ == "__main__":
    x = Solution()
    n = int(input("Enter number of nodes :"))
    From = [int(i) for i in input().split()]
    To = [int(i) for i in input().split()]
    StronglyConnected = [int(i) for i in input().split()]
    ans = x.getStronglyConnectedComponents(n,From,To,StronglyConnected)
    print(ans)

'''

4
1 1 1
2 3 4
0 0 1 0

'''