class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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