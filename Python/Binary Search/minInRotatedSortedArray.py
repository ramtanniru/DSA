class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        mi = float('inf')
        while l<=r:
            if nums[l]<nums[r]:
                mi = min(nums[l],mi)
            mid = (l+r)//2
            mi = min(nums[mid],mi)
            if nums[mid]>=nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return mi 
    