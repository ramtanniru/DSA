
S = input()
i,s,e = 0,0,0
res = []

while i<len(S):
    if S[i]=='#':
        if s<=e:
            res.append(S[s:e+1])
        s = i+1
    else:
        e = i
    i += 1 
if s<=e:
    res.append(S[s:e+1])
print(res)

def recur(S,i=0,s=0,e=0,res = []):
    if i==len(S):
        if s<=e:
            res.append(S[s:e+1])
        return res
    if S[i]=='#':
        if s<=e:
            res.append(S[s:e+1])
        s = i+1
    else:
        e = i
    return recur(S,i+1,s,e,res)
        
print(recur(S)) 