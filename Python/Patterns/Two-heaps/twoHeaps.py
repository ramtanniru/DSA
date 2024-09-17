class MedianFinder:
    def __init__(self):
        self.max = []
        self.min = []
    def addNum(self, num: int) -> None:
        if not self.max or -self.max[0]>=num:
            heapq.heappush(self.max,-num)
        else:
            heapq.heappush(self.min,num)
        # balance
        if len(self.max)<len(self.min):
            temp = heapq.heappop(self.min)
            heapq.heappush(self.max,-temp)
        elif len(self.max)-len(self.min)>1:
            temp = -heapq.heappop(self.max)
            heapq.heappush(self.min,temp)
    def findMedian(self) -> float:
        if len(self.max)!=len(self.min):
            return -self.max[0]
        return ((-self.max[0])+self.min[0])/2 