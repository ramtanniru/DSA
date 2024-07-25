class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,-1*i)
        while len(heap)>1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if y!=x:
                heapq.heappush(heap,y-x)
        return 0 if not heap else -1*heap[0] 