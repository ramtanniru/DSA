class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergeL = []
        i,j = 0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                mergeL.append(nums1[i])
                i += 1
            else:
                mergeL.append(nums2[j])
                j += 1
        while i<len(nums1):
            mergeL.append(nums1[i])
            i += 1
        while j<len(nums2):
            mergeL.append(nums2[j])
            j += 1
        
        if len(mergeL)%2!=0:
            return mergeL[len(mergeL)//2]
        return (mergeL[len(mergeL)//2]+mergeL[(len(mergeL)-1)//2])/2
    