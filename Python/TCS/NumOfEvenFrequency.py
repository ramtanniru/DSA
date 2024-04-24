# Statement: Count characters that have even frequency and are consecutive.
# input: aaabbaccccdd
# output: 8

def count(s):
    i,j = 0,0
    cnt = 0
    while i<len(s) and j<len(s):
        if s[j]==s[i]:
            j+=1
        else:
            if (j-i)%2==0:
                cnt += (j-i)
            i = j
    if(j-i)%2==0:
        cnt+=(j-i)
    return cnt

if __name__=="__main__":
    s = input()
    print(count(s))