class Solution:
    def topoSort(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node):
            if not vis[node]:
                vis[node] = True
                for child in adj[node]:
                    dfs(child)
                stk.append(node)
        adj = defaultdict(list)
        for s,d in prerequisites:
            adj[s].append(d)
        vis = [False for i in range(numCourses)]
        stk = []
        for i in range(numCourses):
            if not vis[i]:
                dfs(i)
        return stk

    def detectCycle(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
                    return True
        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if self.detectCycle(numCourses,prerequisites):
            return []
        return self.topoSort(numCourses,prerequisites) 