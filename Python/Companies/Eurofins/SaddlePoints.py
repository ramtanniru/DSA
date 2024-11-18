def saddlePoints(mat,n):
    r = set()
    c = set()
    for i in range(n):
        miN = float('inf')
        rows = []
        for j in range(n):
            if mat[i][j]<miN:
                miN = mat[i][j]
                rows = [(i,j)]
            elif mat[i][j]==miN:
                rows.append((i,j))
        for node in rows:
            r.add(node)
        maX = float('-inf')
        cols = []
        for j in range(n):
            if mat[j][i]>maX:
                maX = mat[j][i]
                cols = [(j,i)]
            elif mat[j][i]==maX:
                cols.append((j,i))
        for node in cols:
            c.add(node)
    res = list(r.intersection(c))
    return res if res else -1

n = int(input())
mat = [[int(i) for i in input().split()] for i in range(n)]
print(saddlePoints(mat,n))