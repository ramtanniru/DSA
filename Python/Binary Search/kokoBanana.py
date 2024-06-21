class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        def canEat(n):
            hrs = 0
            for i in piles:
                hrs += i//n
                if i%n!=0:
                    hrs += 1
            if hrs<=h:
                return True
            return False
        res = max(piles)
        while l<=r:
            mid = (l+r)//2
            if canEat(mid):
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
    