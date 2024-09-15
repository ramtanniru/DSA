# Statement: Function accepts a mathematical expression 'expr' as a parameter. Implement the function to evaluate the given expression.
# input: 22+15-2*7/3
# output: 33
def evaluateExpression(s):
    return int(eval(s))
s = input()
print(evaluateExpression(s))