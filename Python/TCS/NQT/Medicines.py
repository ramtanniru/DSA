# Statement: N number of patients and L number of medicines per day.
# Print number of days to provide medicines for all patients

import math
def numOfDays(n,l):
    return math.ceil(n/l)

if __name__ =="__main__":
    N = int(input())
    L = int(input())
    print(numOfDays(N,L))