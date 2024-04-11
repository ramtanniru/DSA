class Solution:
    def trap(self, height: List[int]) -> int:
        # Method-1:
        vol = 0
        n = len(height)
        left = [height[0]]*n
        right = [height[-1]]*n
        for i in range(1,n):
            left[i] = max(left[i-1],height[i])
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],height[i])
        for i in range(n):
            vol += min(left[i],right[i])-height[i]
        return vol

        # Method-2:
        vol = 0
        n = len(height)

        # array is empty or having less than 3 buildings 
        if not height or n<3:
            return 0
        
        l,r = 0,n-1
        L,R = height[l],height[r]
        while l<r:
            if L<R:
                l+=1
                L = max(L,height[l])
                vol += L-height[l]
            else:
                r-=1
                R = max(R,height[r])
                vol += R-height[r]
        return vol