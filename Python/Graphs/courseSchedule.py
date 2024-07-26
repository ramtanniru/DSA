class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node,s):
            vis[node] = True
            s.add(node)
            for child in adj[node]:
                if not vis[child]:
                    if dfs(child,s):
                        return True
                elif child in s:
                    return True
            s.remove(node)
            return False
        adj = defaultdict(list)
        for s,d in prerequisites:
            adj[s].append(d)
        vis = [False for i in range(numCourses)]
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i,set()):
                    return False
        return True 