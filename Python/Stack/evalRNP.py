class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        op = set(['+','-','/','*'])
        for i in tokens:
            if i not in op:
                stk.append(int(i))
            else:
                a = stk.pop(-1)
                b = stk.pop(-1)
                sign = -1 if a*b<0 else 1
                if i=='/' and a!=0:
                    c = sign * math.floor(abs(b)/abs(a))
                elif i=='*':
                    c = a*b
                elif i=='+':
                    c = a+b
                elif i=='-':
                    c = b-a
                stk.append(c)
        return stk[-1]