# Problem Statement:
# You are given a number N as a string of digits and an integer K.
#  Your task is to find the largest number that can be obtained by removing exactly K digits from N.
#  You cannot change the order of the remaining digits.

# Input Format:
# The first line contains an integer T, the number of test cases.
# For each test case:
# The first line contains an integer K, the number of digits to remove.
# The second line contains a string N, the number from which the digits are to be removed.
# Output Format:
# For each test case, print the largest possible number that can be obtained after removing exactly K digits from N.

# Test cases:
# N = 123456, K = 2: We need to remove 2 digits. The largest number we can get by removing 2 digits is 3456.
# N = 7654321, K = 3: We need to remove 3 digits. The largest number we can get by removing 3 digits is 7654.
# N = 10234, K = 1: We need to remove 1 digit. The largest number we can get by removing 1 digit is 234.
# N = 9823, K = 2: We need to remove 2 digits. The largest number we can get by removing 2 digits is 98.
# N = 11111, K = 3: We need to remove 3 digits. The largest number we can get is 11.
def solve(N, K):
    window = len(N)-K
    i,j = 0,window
    maX = 0
    while j<len(N):
        maX = max(maX,int(N[i:j]))
        i += 1
        j += 1
    return maX
    
for i in range(int(input())):
    K = int(input())
    N = input()
    print(solve(N,K))