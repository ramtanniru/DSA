def isSafe(board,r,c):
    for i in range(c):
        if board[r][i]==1:
            return False
    i,j = r,c
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i,j = r,c
    while i<len(board) and j>=0:
        if board[i][j]==1:
            return False
        i+=1
        j-=1
    return True

def solveNQueens(board,c):
    if c==len(board):
        return True
    for i in range(n):
        if isSafe(board,i,c):
            board[i][c]=1
            if solveNQueens(board,c+1):
                return True
        board[i][c]=0
    return False

n = int(input())
board = [[0]*n for i in range(n)]
if solveNQueens(board,0):
    for i in board:
        print(*i)