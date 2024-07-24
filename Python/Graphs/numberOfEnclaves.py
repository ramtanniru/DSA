class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(x,y):
            vis[x][y] = True
            for dx,dy in dir:
                r,c = x+dx,y+dy
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and not vis[r][c] and grid[r][c]!=0:
                    dfs(r,c)

        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        cnt = 0

        # first row
        for i in range(len(grid[0])):
            if not vis[0][i] and grid[0][i]==1:
                dfs(0,i)
        
        # last row
        for i in range(len(grid[0])):
            if not vis[len(grid)-1][i] and grid[len(grid)-1][i]==1:
                dfs(len(grid)-1,i)
        
        # first col
        for i in range(len(grid)):
            if not vis[i][0] and grid[i][0]==1:
                dfs(i,0)
        
        # last col
        for i in range(len(grid)):
            if not vis[i][len(grid[0])-1] and grid[i][len(grid[0])-1]==1:
                dfs(i,len(grid[0])-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and not vis[i][j]:
                    cnt += 1
        return cnt 