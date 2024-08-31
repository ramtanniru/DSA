class DisjointSet:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]
    
    def find(self,u):
        if self.parent[u]==u:
            return u
        temp = self.find(self.parent[u])
        self.parent[u] = temp
        return self.parent[u]
    
    def union(self,u,v):
        uPu = self.find(u)
        uPv = self.find(v)
        if uPu==uPv:
            return
        if self.size[uPu]<self.size[uPv]:
            self.parent[uPu] = uPv
            self.size[uPv] += self.size[uPu]
        else:
            self.parent[uPv] = uPu
            self.size[uPu] += self.size[uPv]

if __name__=='__main__':
    d1 = DisjointSet(8)
    d1.union(1,2)
    d1.union(2,3)
    d1.union(4,5)
    d1.union(6,7)
    d1.union(5,6)
    if d1.find(3)==d1.find(7): print("same")
    else: print('not same')
    d1.union(3,7)
    if d1.find(3)==d1.find(7): print("same")
    else: print('not same')


