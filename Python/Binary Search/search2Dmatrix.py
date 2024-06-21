class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = []
        for i in matrix:
            li.extend(i)
        l,r = 0,len(li)-1
        while l<=r:
            mid = (l+r)//2
            if li[mid]==target:
                return True
            elif li[mid]<target:
                l = mid + 1
            else:
                r = mid - 1
        return False
    