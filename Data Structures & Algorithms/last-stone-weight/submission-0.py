import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if y != x:
                heapq.heappush(maxHeap, -(y - x))

        return -maxHeap[0] if maxHeap else 0
        