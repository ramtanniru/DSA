class Solution:
	def setBit(self, n):
	    x = ~n
	    y = x^x-1
	    return n|y 