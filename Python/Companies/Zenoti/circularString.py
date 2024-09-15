# Problem Statement: Circular String
# You are given two strings S1 and S2. Let us define X as a substring (which can also be a circular substring) of S2 such that none of the characters of S1 are present in X.

# A circular substring of a string refers to a substring that consists of some suffix of the string followed by some prefix of the string.
# Task:
# Determine the largest possible string S that can be formed by using all the characters of S1 and X. You can arrange the characters in any order. If there are multiple answers, print the lexicographically largest string among them.

# Note: Strings S1 and S2 consist of only lowercase alphabets. Also, it is guaranteed that you will be able to select a non-empty substring.

# Sample test cases:
# s1='abc', s2 = 'deabcfg' --> 'gfedcba'
# s1 = 'abc', s2 = 'aadebcc' --> 'edcba'

def solve(s1,s2):
    s1_set = set([i for i in s1])
    s2 = s2 + s2
    maxEle =''
    curr = []
    for c in s2:
        if c in s1_set:
            curr = []
        else:
            curr.append(c)
            if len(curr)>len(maxEle):
                maxEle = ''.join(curr)
            if len(curr)==len(maxEle):
                maxEle = max(maxEle,''.join(curr))
    return maxEle+s1
    
for i in range(int(input())):
    S1 = input()
    S2 = input()
    print(solve(S1,S2)) 