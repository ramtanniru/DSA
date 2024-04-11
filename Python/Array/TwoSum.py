class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        for i,x in enumerate(n):
            s = target-x
            if s in n[i+1:]:
                return [i,i+1+n[i+1:].index(s)]