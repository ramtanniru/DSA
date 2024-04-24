class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def powerSet(arr,i):
            if i==len(arr)-1:
                return [[arr[i]],[]]
            subPowerSet = powerSet(arr,i+1)
            res = []
            res.extend(subPowerSet)
            for j in subPowerSet:
                res.append([arr[i]])
                res[-1].extend(j)
            return res
        return powerSet(nums,0)