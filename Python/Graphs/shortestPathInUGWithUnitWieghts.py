import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self, edges, n, m, src):
        minHeap= []
        adj = defaultdict(list)
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        dist = [float('inf') for i in range(n)]
        parent = [i for i in range(n)]
        heapq.heappush(minHeap,(0,src))
        dist[src] = 0
        while minHeap:
            d,node = heapq.heappop(minHeap)
            for child in adj[node]:
                if dist[child]>d+1:
                    dist[child] = d+1
                    parent[child] = node
                    heapq.heappush(minHeap,(d+1,child))
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i] = -1
        return dist 