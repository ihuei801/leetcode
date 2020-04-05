###
# PriorityQueue
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
###

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        from heapq import heappop, heappush
        q = []
        n = 0
        for interval in sorted(intervals, key=lambda x: (x.start, x.end)):
            while q and interval.start >= q[0]:
                heappop(q)
            
            heappush(q, interval.end)
            n = max(n, len(q))
        return n