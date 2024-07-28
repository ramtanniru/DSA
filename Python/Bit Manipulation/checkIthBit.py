class Solution:
    def checkKthBit(self, n,k):
        return n&(1<<k)!=0 