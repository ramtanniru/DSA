class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        minHeap = []
        dist = [[float('inf') for i in range(len(heights[0]))] for j in range(len(heights))]
        dist[0][0] = 0
        minHeap.append((0,0,0))
        dist[0][0] = 0
        while minHeap:
            d,i,j = heapq.heappop(minHeap)
            for dx,dy in dir:
                x,y = i+dx,j+dy
                if 0<=x<len(heights) and 0<=y<len(heights[0]) and max(d,abs(heights[x][y]-heights[i][j]))<dist[x][y]:
                    dist[x][y] = max(d,abs(heights[x][y]-heights[i][j]))
                    heapq.heappush(minHeap,(max(d,dist[x][y]),x,y))
        return dist[-1][-1] 