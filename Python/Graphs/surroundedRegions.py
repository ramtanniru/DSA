class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(x,y):
            vis[x][y] = True

            for dx,dy in dir:
                r,c = x+dx,y+dy
                if 0<=r<len(board) and 0<=c<len(board[0]) and not vis[r][c] and board[r][c]!='X':
                    dfs(r,c)

        vis = [[False for i in range(len(board[0]))] for j in range(len(board))]
        dir = [(0,1),(1,0),(0,-1),(-1,0)]

        # 1st row
        for i in range(len(board[0])):
            if board[0][i]=='O' and not vis[0][i]:
                dfs(0,i)
        
        # 1st col
        for i in range(len(board)):
            if board[i][0]=='O' and not vis[i][0]:
                dfs(i,0)
        
        # last row
        for i in range(len(board[0])):
            if board[-1][i]=='O' and not vis[-1][i]:
                dfs(len(board)-1,i)
        
        # last col
        for i in range(len(board)):
            if board[i][-1]=='O' and not vis[i][-1]:
                dfs(i,len(board[0])-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if not vis[i][j]:
                    board[i][j] = 'X'