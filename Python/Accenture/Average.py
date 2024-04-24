# Statement: Function accepts a string str of length len. 
# Implement the function to calculate the word average of the ascii values of all of the letters in a word.
# input: source
# output: 109.50
def findAverageAscii(s):
    n = 0
    for i in s:
        n += ord(i)
    return round(n/len(s),2)
s = input()
print(findAverageAscii(s))