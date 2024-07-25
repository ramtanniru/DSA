class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        li = []
        for i,j in points:
            dist = math.sqrt(i**2+j**2)
            li.append((-1*dist,i,j))
        
        # push first k elements
        for i in range(k):
            heapq.heappush(maxHeap,li[i])
        
        for i in range(k,len(li)):
            if maxHeap[0][0]<li[i][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap,li[i])

        res = []
        for dist,x,y in maxHeap:
            res.append([x,y])
        return res 