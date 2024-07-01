# print lower case alphabet that appeared maximum in the string 
from collections import Counter
s = input()
d = Counter(s)
maxFreq = -1
maxEl = "No alphabet found" 
for i,j in d.items():
    if 97<=ord(i)<=122:
        if j>maxFreq:
            maxFreq = j
            maxEl = i 
        elif j==maxFreq:
            if ord(i)<ord(maxEl):
                maxEl = i
print(maxEl) 