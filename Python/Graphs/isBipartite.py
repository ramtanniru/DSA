class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node,color):
            vis[node] = color
            for child in graph[node]:
                if vis[child]==-1:
                    if not dfs(child,1-color):
                        return False
                elif vis[child]==color:
                    return False
            return True

        vis = [-1 for i in range(len(graph))]
        for i in range(len(graph)):
            if vis[i]==-1:
                if not dfs(i,0):
                    return False
        return True 