class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {"{":"}","(":")","[":"]"}
        for i in s:
            if i in d:
                stk.append(d[i])
            else:
                if stk:
                    if stk[-1]==i:
                        stk.pop(-1)
                    else:
                        return False
                else:
                    return False
        return len(stk)==0
            