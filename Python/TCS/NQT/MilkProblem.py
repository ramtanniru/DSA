# Statement: A litre Plastic milk bottle costs R1, Glass milk bottle costs R2.
# You can resale empty glass milk bottle with R3 rupees. If you have N rupees return maximum number of litres can be bought
# input: 10 11 9 8
# output: 2

# Recursion 
def calculateUsingRecursion(N,R1,R2,R3):
    l = 0
    if N<R1 and N<R2:
        return l
    if R1>=(R2-R3) and N>=R2:
        bottles = N//R2
        N = (N%R2) + (bottles*R3)
        l = bottles + calculateUsingRecursion(N,R1,R2,R3)
    else:
        bottles = N//R1
        N = N%R1
        l = bottles + calculateUsingRecursion(N,R1,R2,R3)
    return l 

if __name__=='__main__':
    n,r1,r2,r3 = map(int,input().split())
    print(calculateUsingRecursion(n,r1,r2,r3))