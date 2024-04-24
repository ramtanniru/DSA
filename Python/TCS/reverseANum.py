# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

def reverseANum(n):
    sign = 1 if n>0 else -1
    n *= sign
    res = 0
    while n>0:
        res += (n%10)
        res *= 10
        n = n//10
    res = res//10
    return sign*res

if __name__=='__main__':
    n = int(input())
    print(reverseANum(n))
