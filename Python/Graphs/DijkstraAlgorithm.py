from typing import List
import heapq
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        adjMat = [[float('inf') for i in range(V)] for j in range(V)]
        minHeap = []
        for s in range(len(adj)):
            for d,c in adj[s]:
                adjMat[s][d] = c
        parent = [i for i in range(V)]
        dist = [float('inf') for i in range(V)]
        heapq.heappush(minHeap,(0,S))
        dist[S] = 0
        while minHeap:
            d,node = heapq.heappop(minHeap)
            for child,cost in enumerate(adjMat[node]):
                if cost!=float('inf'):
                    if dist[child]>d+cost:
                        dist[child] = d+cost
                        parent[child] = node
                        heapq.heappush(minHeap,(d+cost,child))
        for i in range(V):
            if dist[i]==float('inf'):
                dist[i] = -1
        return dist 