class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            nonlocal vis
            if not vis[node]:
                vis[node] = True
                for i,x in enumerate(isConnected[node]):
                    if x==1:
                        dfs(i)
        cnt = 0
        n = len(isConnected)
        vis = [False for i in range(n)]
        i = 0
        while i<len(isConnected):
            if not vis[i]:
                cnt += 1
                dfs(i)
            i += 1
        return cnt 