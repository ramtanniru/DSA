class Solution:
    def search(self, pat, txt):
        s = pat+'#'+txt
        pi = [0]*len(s)
        res = []
        for i in range(1,len(s)):
            j = pi[i-1]
            while j>0 and s[i]!=s[j]:
                j = pi[j-1]
            if s[i]==s[j]:
                j += 1
            pi[i] = j
            if pi[i]==len(pat):
                res.append(i-len(pat)*2)
        return res