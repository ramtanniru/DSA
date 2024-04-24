# Statement: Sort the string using key 
# sample input: apple eapl
# output: eappl

from collections import Counter
def sortUseKey(s,k):
    d = dict(Counter(s))
    res = ""
    for i in k:
        res += i*d[i]
    return res 

if __name__=='__main__':
    s = input()
    key = input()
    print(sortUseKey(s,key))