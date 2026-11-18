from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        rooms = 0
        maxRooms = 0
        s = e = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
                maxRooms = max(maxRooms, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1

        return maxRooms