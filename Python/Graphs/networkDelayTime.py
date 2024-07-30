class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[float('inf') for i in range(n)] for j in range(n)]
        minHeap = []
        for s,d,c in times:
            adj[s-1][d-1] = c
        dist = [float('inf') for i in range(n)]
        minHeap.append((0,k-1))
        dist[k-1] = 0
        while minHeap:
            cost,node = heapq.heappop(minHeap)
            for child,c in enumerate(adj[node]):
                if c+cost<dist[child]:
                    dist[child] = c+cost
                    heapq.heappush(minHeap,(c+cost,child))
        res = max(dist)
        return -1 if res==float('inf') else res 