class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def rec(idx=0,s=0):
            if idx==len(nums):
                return s==total-s
            if dp[idx][s]!=-1:
                return dp[idx][s]
            if s==total-s:
                return True
            if s>total-s:
                return False
            notTake = rec(idx+1,s)
            take = rec(idx+1,s+nums[idx])
            dp[idx][s] = take or notTake
            return dp[idx][s]
        total = sum(nums)
        dp = [[-1 for i in range(total+1)] for j in range(len(nums))]
        if total&1:
            return False
        return rec() 