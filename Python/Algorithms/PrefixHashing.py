# Given an array of integers arr and an integer k,
# return the total number of subarrays whose sum equals to k.
from collections import defaultdict
class Solution:
    def subarraySum(arr,k) -> int:
        cnt = 0
        sum = 0
        cache = defaultdict(int)
        cache[0] = 1
        for i in arr:
            sum += i
            if sum-k in cache:
                cnt += cache[sum-k]
            cache[sum] += 1
        return cnt