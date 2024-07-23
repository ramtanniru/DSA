from typing import List
from queue import Queue
from collections import deque
class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        if not adj:
            return []
        queue = deque([])
        queue.append(0)
        vis = [False for i in range(V)]
        vis[0] = True
        res = []
        while queue:
            temp = queue.popleft()
            for i in adj[temp]:
                if not vis[i]:
                    vis[i] = True
                    queue.append(i)
            res.append(temp)
        return res 