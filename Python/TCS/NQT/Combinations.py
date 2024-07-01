# Statement: N number of pencils and M number of erasers in a shop. Kiran wants to buy P pencils and E erasers find the number of ways he can select pencils and erasers.
# input: 3 1 2 1
# output: 3
def factorial(n):
    res = 1
    for i in range(2,n+1):
        res *= i 
    return res

def combination(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))

def possibleCombination(N,M,P,E):
    return int(combination(N,P)*combination(M,E))

if __name__=='__main__':
    N,M,P,E = map(int,input().split())
    print(possibleCombination(N,M,P,E))