# Statement: Find whether two arithmetic progression sequences has a match or not 
# sample input:
# 9
# 2 22 20 9
# output: has a match  
def find(l1,l2):
    i,j = 0,0
    n = len(l1)
    while i<n and j<n:
        if l1[i]>l2[j]:
            j+=1
        elif l1[i]<l2[j]:
            i+=1
        else:
            return True
    return False 

if __name__=="__main__":
    n = int(input()) # length of AP series
    # a1 -> first number in Arithmetic Progression series l1
    # a2 -> first number in Arithmetic Progression series l2
    # d1 -> common difference in Arithmetic Progression series l1
    # d2 -> common difference in Arithmetic Progression series l2
    a1,a2,d1,d2 = map(int,input().split())
    l1,l2 = [a1],[a2]
    for i in range(n):
        a1,a2 = a1+d1,a2+d2
        l1.append(a1)
        l2.append(a2)
    if find(l1,l2):
        print("Match found")
    else:
        print("Match not found")