class Solution:
    def topoSort(self, V, adj):
        def dfs(node):
            if not vis[node]:
                vis[node] = True
                for child in adj[node]:
                    dfs(child)
                stk.append(node)
        vis = [False for i in range(V)]
        stk = []
        for i in range(V):
            if not vis[i]:
                dfs(i)
        return stk[::-1] 