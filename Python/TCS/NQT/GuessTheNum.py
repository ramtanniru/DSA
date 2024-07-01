# Statement: Eq => X = (N*A) + Z , Z is divisor of N. If A and X are given then find possible combinations of N,Z.
# input: 25 2
# output: [(10,5),(12,1)]
def guessTheNum(X,A):
    ans = []
    for N in range(1,X):
        for Z in range(1,N):
            if N%Z==0 and X==(N*A)+Z:
                    ans.append((N,Z))
    return ans

if __name__=='__main__':
    X,A = map(int,input().split())
    print(guessTheNum(X,A)) 