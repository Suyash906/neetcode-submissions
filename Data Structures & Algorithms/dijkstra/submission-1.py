from collections import defaultdict
from heapq import heappush as insert
from heapq import heappop as delete
class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        if n == 0 or not edges:return {}

        graph = defaultdict(list)
        distance = {i:float('inf') for i in range(n)}
        for start, end, weight in edges:
            graph[start].append(Edge(end, weight))

        
        heap = []
        insert(heap, (src,0))
        distance[src] = 0

        while heap:
            node, curr_weight = delete(heap)

            if curr_weight > distance[node]:continue

            distance[node] = curr_weight
            for neighbour in graph[node]:
                new_distance = curr_weight + neighbour.weight
                insert(heap, (neighbour.node, new_distance))


        for node, shortest_distance in distance.items():
            if shortest_distance == float('inf'):
                distance[node] = -1


        return distance