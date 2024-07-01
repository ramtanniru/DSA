# check whether s2 is substring of s1 or not ? 
s1 = input()
s2 = input()

def isSubstring(s1,s2):
    n = len(s2)
    i,j = 0,n
    while j<len(s1):
        if s1[i:j]==s2:
            print(True)
            break
        i += 1
        j += 1
    print(False) 

def recursive(s1,s2,i=0,j=0):
    if j>=len(s1):
        return False
    if i==len(s2):
        return True
    if s1[j]==s2[i]:
        i += 1
        j += 1
    else:
        i = 0
        j += 1
    return recursive(s1,s2,i,j)

print(recursive(s1,s2))
    

