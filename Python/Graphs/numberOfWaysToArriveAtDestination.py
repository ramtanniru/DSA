class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        minHeap = []
        mod = 10**9+7
        adj = [[float('inf') for i in range(n)] for j in range(n)]
        for s,d,c in roads:
            adj[s][d] = c
            adj[d][s] = c
        dist = [[float('inf'),0] for i in range(n)]
        minHeap.append((0,0))
        dist[0] = [0,1]
        while minHeap:
            cost,node = heapq.heappop(minHeap)
            for child,c in enumerate(adj[node]):
                if c+cost<dist[child][0]:
                    dist[child] = [c+cost,dist[node][1]]
                    heapq.heappush(minHeap,(c+cost,child))
                elif c+cost==dist[child][0]:
                    dist[child] = [c+cost,(dist[child][1]+dist[node][1])%mod]
        return dist[-1][1]%mod 
