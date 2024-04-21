def subsetsOfArray(a,i):
    if i==len(a)-1:
        return [[a[i]],[]]
    l = subsetsOfArray(a,i+1)
    res = []
    res.extend(l)
    for j in l:
        res.append([a[i]])
        res[-1].extend(j)
    return res
a = [i for i in input().split()]
print(subsetsOfArray(a,0))