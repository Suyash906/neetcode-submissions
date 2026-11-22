from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        heap = []
        for num, count in num_to_count.items():
            heappush(heap, (count, num))

            if len(heap) > k:
                _ = heappop(heap)

        res = []
        while heap:
            res.append(heappop(heap)[1])

        return res
        

