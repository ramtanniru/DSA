class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        res = []
        vis = [False for i in range(V)]
        def dfs(node):
            nonlocal res,vis
            if not vis[node]:
                vis[node] = True
                res.append(node)
                for n in adj[node]:
                    dfs(n)
        dfs(0)
        return res 