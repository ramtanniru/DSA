def boardGame(board):
    n = len(board)
    pos = [int(i) for i in range(1,n+1)]
    drums = 0
    while pos!=board:
        temp = [0]*n
        for i,x in enumerate(board):
            temp[x-1] = pos[i]
        
        pos = temp
        drums += 1
    return drums+1

if __name__=="__main__":
    board = [int(i) for i in input().split()]
    print(boardGame(board))

