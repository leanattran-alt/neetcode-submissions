from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0

        for i in range(len(cost) -1, -1, -1):
            one, two = cost[i] + min(one, two), one

        return min(one, two)