class Solution:
    def rob(self, nums: List[int]) -> int:
        def gold(arr,idx):
            if idx==len(arr)-1:
                dp[idx] = arr[idx]
                return arr[idx]
            if idx>=len(arr):
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            dp[idx] = max(gold(arr,idx+1),arr[idx]+gold(arr,idx+2))
            return dp[idx]
        dp = [-1]*len(nums)
        gold(nums,0)
        print(dp)
        return max(dp)