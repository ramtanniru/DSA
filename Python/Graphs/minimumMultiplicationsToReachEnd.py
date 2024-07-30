from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        queue = deque([])
        dist = [float('inf') for i in range(100000)]
        queue.append((0,start))
        dist[start] = 0
        mod = 100000
        while queue:
            cost,node = queue.popleft()
            for c in arr:
                num = c*node%mod
                if 1+cost<dist[num]:
                    dist[num] = 1+cost
                    queue.append((1+cost,num))
        return -1 if dist[end]==float('inf') else dist[end] 