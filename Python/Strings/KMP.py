class Solution:
    def kmp(self,a,b):
        s = b+'#'+a
        n = len(s)
        pi = [0]*n
        for i in range(1,n):
            j = pi[i-1]
            while j>0 and s[i]!=s[j]:
                j = pi[j-1]
            if s[i]==s[j]:
                j += 1
            pi[i] = j
            if pi[i]==len(b):
                return i-2*len(b)
        return -1