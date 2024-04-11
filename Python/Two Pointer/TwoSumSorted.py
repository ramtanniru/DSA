class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        while l<r:
            if nums[r]+nums[l]>target:
                r-=1
            elif nums[r]+nums[l]<target:
                l+=1
            else:
                return [l+1,r+1]