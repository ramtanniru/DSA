class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numOfZeroes = 0
        prodWithZero = 1
        prodWithoutZero = 1
        res = [1]*len(nums)
        for i in nums:
            if i==0:
                numOfZeroes += 1
            if numOfZeroes>1:
                return [0]*len(nums)
            prodWithZero *= i
            prodWithoutZero *= i if i!=0 else 1
        return [prodWithZero//i if i!=0 else prodWithoutZero for i in nums]