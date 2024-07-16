class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        s = set(nums)
        def p(s,l=[]):
            if not s:
                self.res.append(l)
                return
            for i in s:
                p(s-{i},l+[i])
        p(s)
        return self.res 
