from heapq import heappush as insert
from heapq import heappop as delete
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        insert(self.max_heap, -num)
        insert(self.min_heap, -delete(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            insert(self.max_heap, -delete(self.min_heap))

    def findMedian(self) -> float:
        if ( len(self.min_heap) + len(self.max_heap) ) % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        return -self.max_heap[0]
        
        