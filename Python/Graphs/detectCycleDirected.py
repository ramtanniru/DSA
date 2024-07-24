class Solution:
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        def dfs(node,path):
            vis[node] = True
            path.add(node)
            for child in adj[node]:
                if not vis[child]:
                    if dfs(child,path):
                        return True
                elif child in path:
                    return True
            path.remove(node)
            return False
        vis = [False for i in range(V)]
        for i in range(V):
            if not vis[i]:
                if dfs(i,set()):
                    return 1
        return 0 