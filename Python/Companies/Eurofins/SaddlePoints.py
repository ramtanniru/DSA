def saddlePoints(mat,n):
    r = set()
    c = set()
    for i in range(n):
        maX = float('-inf')
        rows = []
        for j in range(n):
            if mat[i][j]>maX:
                maX = mat[i][j]
                rows = [(i+1,j+1)]
            elif mat[i][j]==maX:
                rows.append((i+1,j+1))
        for node in rows:
            r.add(node)
        miN = float('inf')
        cols = []
        for j in range(n):
            if mat[j][i]<miN:
                miN = mat[j][i]
                cols = [(j+1,i+1)]
            elif mat[j][i]==miN:
                cols.append((j+1,i+1))
        for node in cols:
            c.add(node)
    res = list(r.intersection(c))
    return res if res else -1

n = int(input())
mat = [[int(i) for i in input().split()] for i in range(n)]
print(saddlePoints(mat,n))