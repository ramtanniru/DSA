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