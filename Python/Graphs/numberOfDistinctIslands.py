import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        def dfs(x,y,i,j,v):
            grid[x][y] = -1
            v.append((x-i,y-j))
            for dx,dy in dir:
                if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]) and grid[x+dx][y+dy]==1:
                    dfs(x+dx,y+dy,i,j,v)
        if not grid:
            return 0
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        s = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    v = []
                    dfs(i,j,i,j,v)
                    s.add(tuple(v))
        return len(s) 