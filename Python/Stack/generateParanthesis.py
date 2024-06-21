class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(s='(',op=1,cl=0):
            if op==n and cl==n:
                res.append(s)
                return
            if op<n:
                bt(s+'(',op+1,cl)
            if cl<n and cl<op:
                bt(s+')',op,cl+1)
            return
        bt()
        return res
            