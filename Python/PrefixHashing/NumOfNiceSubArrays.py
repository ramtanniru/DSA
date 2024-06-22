class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i] = 0
            else:
                nums[i] = 1
        # converting the list into 0 and 1
        # eg: [1,2,3,4,5] to [1,0,1,0,1]
        # count subarrays to sum equal to k using prefix hashing
        cnt = 0
        pre = 0
        preArr = defaultdict(int)
        preArr[0] = 1
        for i in nums:
            pre += i
            if pre-k in preArr:
                cnt += preArr[pre-k]
            preArr[pre] += 1
        return cnt