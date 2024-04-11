class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n,p,z = [],[],[]
        res = set()
        # dividing the numbers into neg, zero, pos
        for i in nums:
            if i<0:
                n.append(i)
            elif i>0:
                p.append(i)
            else:
                z.append(i)
        n.sort()
        p.sort()
        N,P = set(n),set(p)

        # adding elements if it has one zero like [-1,0,1]
        if z:
            for i in n:
                if -1*i in P:
                    res.add((i,0,-1*i))
        
        # addding [0,0,0] if it has three or more zeroes
        if len(z)>=3:
            res.add((0,0,0))

        # checking every pair in neg and checking for existence of corresponding pos
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if -1*(n[i]+n[j]) in P:
                    res.add((n[i],n[j],-1*(n[i]+n[j])))
        
        # checking every pair in pos and checking for existence of corresponding pos
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if -1*(p[i]+p[j]) in N:
                    res.add((-1*(p[i]+p[j]),p[i],p[j]))
        
        return res
