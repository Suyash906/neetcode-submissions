from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone)

        while len(heap) > 1:
            stone_1 = -1 * heappop(heap)
            stone_2 = -1 *heappop(heap)

            heappush(heap, -(stone_1 - stone_2))

        return -heap[0]