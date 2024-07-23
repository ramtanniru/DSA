from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		vis = [False for i in range(V)]
		def bfs(node):
		    queue = deque([(node,-1)])
		    nonlocal vis
		    vis[node] = True
		    while queue:
		        n,p = queue.pop()
		        for i in adj[n]:
		            if not vis[i]:
		                vis[i] = True
		                queue.append((i,n))
		            elif i!=p:
		                return True
		    return False
		    
		for i in range(V):
		    if not vis[i]:
		        if bfs(i):
		            return 1
		return 0 