# Statement: Function accepts a string consists of binary digits separated with an alphabet as follows:
# 'A' = "&"
# 'B' = "|"
# "C" = "^"
# input: 1C0C1C1A0B1
# output: 1

def calculate(s):
    a = int(s[0])
    i = 1
    while i<len(s)-1:
        operand = s[i]
        b = int(s[i+1])
        if operand=="A":
            a = a&b
        elif operand=="B":
            a = a|b
        elif operand=="C":
            a = a^b
        i+=2
    return a
s = input()
print(calculate(s))