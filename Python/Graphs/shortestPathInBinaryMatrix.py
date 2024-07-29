class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dir = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
        dist = [[float('inf') for i in range(len(grid))] for j in range(len(grid))]
        dist[0][0] = 1
        queue = []
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        if len(grid)==1:
            return 1
        queue.append((1,(0,0)))
        while queue:
            d,coord = queue.pop(0)
            i,j = coord[0],coord[1]
            for dx,dy in dir:
                x,y = i+dx,j+dy
                if 0<=x<len(grid) and 0<=y<len(grid) and grid[x][y]==0 and 1+d<dist[x][y]:
                    if x==len(grid)-1 and y==len(grid)-1:
                        return 1+d
                    grid[i][j] = 1
                    dist[x][y] = 1+d
                    queue.append((1+d,(x,y)))
        return -1 
                