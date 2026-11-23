from heapq import heappush as insert
from heapq import heappop as delete
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __lt__(self, other):
        return (self._x ** 2 + self._y ** 2) > (other._x ** 2 + other._y ** 2)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x, y in points:
            insert(heap, Point(x, y))
            if len(heap) > k:
                delete(heap)

        res = []

        while heap:
            point = delete(heap)
            res.append([point._x, point._y])    


        return res    
