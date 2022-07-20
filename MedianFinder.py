class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.min_heap,num)
        elif not self.max_heap:
            if num < self.min_heap[0]:
                heapq.heappush(self.max_heap,-num)
            else:
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap,num)
        elif (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            if num < -self.max_heap[0]:
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap,-num)
            else:
                heapq.heappush(self.min_heap,num)
        else:
            if num < self.min_heap[0]:
                heapq.heappush(self.max_heap,-num)
            else:
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap,num)
    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            return self.min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
