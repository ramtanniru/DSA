class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
        while queue:
            li = queue.copy()
            for i,j in li:
                for dx,dy in dir:
                    if 0<=i+dx<len(grid) and 0<=j+dy<len(grid[0]) and grid[i+dx][j+dy]==1:
                        grid[i+dx][j+dy]=2
                        queue.append((i+dx,j+dy))
                queue.popleft()
            time += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        time -= 1
        if time<0:
            return 0
        return time 