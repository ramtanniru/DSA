class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dist = [float('inf') for i in range(n)]
        adj = [[float('inf') for i in range(n)] for j in range(n)]
        for s,d,c in flights:
            adj[s][d] = c
        queue = deque([])
        queue.append((0,src,0))
        dist[src] = 0
        while queue:
            stops,node,cost = queue.popleft()
            for child,c in enumerate(adj[node]):
                if stops<=K and (cost+c<dist[child]):
                    dist[child] = cost+c
                    queue.append((stops+1,child,cost+c))
        return dist[dst] if dist[dst]!=float('inf') else -1 