from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [float('inf')] * n
        dist[src] = 0

        minHeap = [(0, src)]

        while minHeap:
            d, u = heapq.heappop(minHeap)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                newDist = d + w

                if newDist < dist[v]:
                    dist[v] = newDist
                    heapq.heappush(minHeap, (newDist, v))

        return {i: dist[i] if dist[i] != float('inf') else -1 for i in range(n)}