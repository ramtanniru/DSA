class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        for i,x in enumerate(nums2):
            d[x] = i
        res = []
        for i in nums1:
            flag = True
            for j in range(d[i]+1,len(nums2)):
                if i<nums2[j]:
                    res.append(nums2[j])
                    flag = False
                    break
            if flag:
                res.append(-1)
        return res 
    