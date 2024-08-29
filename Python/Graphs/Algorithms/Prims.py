from typing import List
import heapq
class Solution:
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        minHeap = []
        vis = [False for i in range(V)]
        s = 0
        minHeap.append((0,0,-1))
        while minHeap:
            cost,node,parent = heapq.heappop(minHeap)
            if not vis[node]:
                s += cost
                vis[node] = True
                for child,c in adj[node]:
                    if not vis[child]:
                        heapq.heappush(minHeap,(c,child,node))
        return s 