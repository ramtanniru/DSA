# Statement : Print unit digit of factorial of given number
# sample input : 5
# output: 2 since 5!=120 
def unitDigitOfFactorial(n):
    res = 1
    for i in range(1,n):
        res *= i+1
        if res%10==0:
            res = res//10
    return res%10

if __name__=="__main__":
    n = int(input())
    print(unitDigitOfFactorial(n))