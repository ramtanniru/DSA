# check whether s2 is isSubsequence of s1 or not ? 
def isSubsequence(s1,s2,i=0,j=0):
    if j>=len(s1):
        return False
    if i==len(s2):
        return True
    if s1[j]==s2[i]:
        i += 1
        j += 1
    else:
        j += 1
    return isSubsequence(s1,s2,i,j)
s1 = input()
s2 = input()
print(isSubsequence(s1,s2))