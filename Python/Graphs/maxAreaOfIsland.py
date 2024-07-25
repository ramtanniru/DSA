class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if not vis[i][j]:
                vis[i][j] = True
                if grid[i][j] == 0:
                    area = 0
                else:
                    area = 1
                for dx,dy in dir:
                    x,y = i+dx,j+dy
                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1:
                        area += dfs(x,y)
                return area 
            return 0 
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not vis[i][j] and grid[i][j]==1:
                    maxArea = max(maxArea,dfs(i,j))
        return maxArea 