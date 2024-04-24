# Statement: Function accepts a string 's'. Implement the function to find the smallest English character,
# which is not present in the given string 's' and return the same.
# input: aidubudxd
# output: c
def findSmallestMissingCharacter(s):
    alphabets = [False]*26
    alpha = set()
    for i in s:
        if i not in alpha:
            alphabets[ord(i)-97] = True
            alpha.add(i)
    for i,x in enumerate(alphabets):
        if not x:
            return chr(i+97)
s = input()
print(findSmallestMissingCharacter(s))
