# Print level of a binary tree with maximum sum off odd elements and nearest to root. 

class Solution:
    def nearestMaxOddSumLevel(self,arr):
        i = 0
        j = 0
        s = 0
        res = float('inf')
        while i<len(arr):
            cnt = 0
            for id in range(i,i+2**j):
                if id==len(arr): break
                if arr[id]%2!=0:
                    cnt += arr[id]
            if s<cnt:
                s = cnt
                res = j+1
            i += 2**j
            j += 1
        return res
    
arr = [int(i) for i in input().split()]
x = Solution()
print(x.nearestMaxOddSumLevel(arr))

