from collections import Counter, deque
from heapq import heappush as insert
from heapq import heappop as delete
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        heap = []

        for count in counts.values():
            insert(heap, -count)

        queue = deque()

        time = 0

        while heap or queue:
            time += 1
            if not heap:
                time = queue[0][0]
            else:
                curr = delete(heap)
                curr += 1
                if curr != 0:
                    queue.append([time + n, curr])
            
            if queue and queue[0][0] == time:
                insert(heap, queue.popleft()[1])

        return time
