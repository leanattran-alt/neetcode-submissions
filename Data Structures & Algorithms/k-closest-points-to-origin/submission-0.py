import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(minHeap, (distance, x, y))
        
        result = []

        for _ in range(k):
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])

        return result
        