class Solution:
    def bellman_ford(self, V, edges, S):
        dist = [10**8 for i in range(V)]
        dist[S] = 0
        # n-1 iterations 
        for i in range(V-1):
            for u,v,wt in edges:
                if dist[u]!=10**8 and dist[u]+wt<dist[v]:
                    dist[v] = dist[u]+wt
        # nth iteration to detect negative cycle 
        for u,v,wt in edges:
            if dist[u]!=10**8 and dist[u]+wt<dist[v]:
                return [-1]
        return dist 