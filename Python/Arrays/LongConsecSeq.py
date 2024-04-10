class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        l = 0
        for i in nums:
            if i-1 not in nums:
                cnt = 1
                while i+1 in nums:
                    cnt+=1
                    i+=1
                l = max(cnt,l)
        return l