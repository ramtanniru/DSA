class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic decreasing deque
        queue = deque([])
        res = []
        for i,x in enumerate(nums[:k]):
            if not queue:
                queue.append((i,x))
            else:
                while queue and queue[-1][1]<x:
                    queue.pop()
                queue.append((i,x))
        res.append(queue[0][1])
        for i in range(k,len(nums)):
            if not queue:
                queue.append((i,nums[i]))
            else:
                if i-queue[0][0]>=k:
                    queue.popleft()
                while queue and queue[-1][1]<nums[i]:
                    queue.pop()
                queue.append((i,nums[i]))
            res.append(queue[0][1])
        return res 
    