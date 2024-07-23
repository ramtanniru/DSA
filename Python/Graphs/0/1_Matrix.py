class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque([])
        vis = [[False for i in range(len(mat[0]))] for j in range(len(mat))]
        res = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j,0))
                    vis[i][j] = True
        while queue:
            x,y,dist = queue.popleft()
            res[x][y] = dist
            for dx,dy in dir:
                r,c = x+dx,y+dy
                if 0<=r<len(mat) and 0<=c<len(mat[0]) and not vis[r][c]:
                    vis[r][c] = True
                    queue.append((r,c,1+dist))
        return res 