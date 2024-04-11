class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []
        for i in s:
            # check i lies in [a....z] or [0...9]
            if 97<=ord(i)<=122 or 47<=ord(i)<=57:
                arr.append(i)
        l,r = 0,len(arr)-1
        while(l<r):
            if arr[l]!=arr[r]:
                return False 
            l+=1
            r-=1
        return True