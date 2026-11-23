from heapq import heappush as insert
from heapq import heappop as delete
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for num in nums:
            insert(heap, num)
            if len(heap) > k:
                delete(heap)

        return heap[0]
