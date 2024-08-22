class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        res = []
        nums.extend(nums)
        for i in nums[::-1]:
            if not stk:
                res.append(-1)
            else:
                while stk and stk[-1]<=i:
                    stk.pop()
                if stk:
                    res.append(stk[-1])
                else:
                    res.append(-1)
            stk.append(i)
        return res[::-1][:len(res)//2] 