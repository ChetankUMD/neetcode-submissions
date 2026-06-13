class MedianFinder:

    def __init__(self):
        self.largeHeap = []
        self.smallHeap = []

    def addNum(self, num: int) -> None:
        if self.largeHeap and num > self.largeHeap[0]:
            heapq.heappush(self.largeHeap, num)
        else:
            heapq.heappush(self.smallHeap, -1*num)
        if len(self.smallHeap)>len(self.largeHeap)+1:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        if len(self.smallHeap)+1<len(self.largeHeap):
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * val)

    def findMedian(self) -> float:
        if len(self.largeHeap)>len(self.smallHeap):
            return self.largeHeap[0]
        elif len(self.largeHeap)<len(self.smallHeap):
            return -1 *self.smallHeap[0]
        else:
            return (self.largeHeap[0] + (-1 * self.smallHeap[0])) / 2.0
        