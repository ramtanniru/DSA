class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if not vis[i][j]:
                vis[i][j] = True
                for dx,dy in dir:
                    x,y = i+dx,j+dy
                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='1':
                        dfs(x,y)
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        numOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not vis[i][j] and grid[i][j]=='1':
                    numOfIslands += 1
                    dfs(i,j)
        return numOfIslands 