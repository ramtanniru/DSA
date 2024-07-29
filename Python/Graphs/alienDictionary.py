from collections import defaultdict
from collections import deque
class Solution:
    
    def topoSort(self, V, adj):
        # kahn's algorithm
        indegree = [0 for i in range(V)]
        for children in adj:
            for node in children:
                indegree[node] += 1
        queue = deque([])
        res = []
        for i,x in enumerate(indegree):
            if x==0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            res.append(node)
            for child in adj[node]:
                indegree[child] -= 1
                if indegree[child]==0:
                    queue.append(child)
        return res 
        
    def findOrder(self,alien, N, K):
        adj = [[] for i in range(K)]
        for i in range(N-1):
            s1 = alien[i]
            s2 = alien[i+1]
            for k in range(min(len(s1),len(s2))):
                if s1[k]!=s2[k]:
                    adj[ord(s1[k])-ord('a')].append(ord(s2[k])-ord('a'))
                    break
        res = self.topoSort(K,adj)
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(res)):
            res[i] = alpha[res[i]]
        return res 