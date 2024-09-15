# Statement: Function to round off the given number 'n' to multiple of 10 according to following rules:
# -> if unit digit of n is <=4, then round off n to smaller nearest number to n which is multiple of 10.
# -> if unit digit of n is >=5, then round off n to largest nearest number to n which is multiplt of 10.
# Return the round off value.
# Nearest number: a number is nearest another number if they have least difference between them.
# Distance between two numbers is thenumber of integers between them.
# input: 434
# output: 430

def nearestMultipleOfTen(n):
    if n%10<=4:
        n -= n%10
    else:
        n += 10 - n%10
    return n
n = int(input())
print(nearestMultipleOfTen(n))