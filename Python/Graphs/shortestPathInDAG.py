from typing import List
import heapq
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = [[float('inf') for i in range(n)] for j in range(n)]
        minHeap = []
        for s,d,c in edges:
            adj[s][d] = c
        parent = [i for i in range(n)]
        dist = [float('inf') for i in range(n)]
        heapq.heappush(minHeap,(0,0))
        dist[0] = 0
        while minHeap:
            d,node = heapq.heappop(minHeap)
            for child,cost in enumerate(adj[node]):
                if cost!=float('inf'):
                    if dist[child]>d+cost:
                        dist[child] = d+cost
                        parent[child] = node
                        heapq.heappush(minHeap,(d+cost,child))
        for i in range(n):
            if dist[i]==float('inf'):
                dist[i] = -1
        return dist 