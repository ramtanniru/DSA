class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Method-1:
        d = dict()
        for i in nums: 
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if d[i]>1:
                return True
        return False

        # Method-2:
        return len(nums)!=len(set(nums))