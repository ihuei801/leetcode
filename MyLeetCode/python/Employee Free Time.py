###
# Time Complexity: O(nlogk) k: number of employees, n: number of intervals
# Space Complexity: O(k)
###
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class EmployInterval:
    def __init__(self, interval, employ_idx, interval_idx):
        self.interval = interval
        self.employ_idx = employ_idx
        self.interval_idx = interval_idx

    def __lt__(self, other):
        return self.interval.start < other.interval.start


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        pq = []
        import heapq
        for i, intervals in enumerate(schedule):
            heapq.heappush(pq, EmployInterval(intervals[0], i, 0))
        prev = None
        result = []
        while pq:
            cur = heapq.heappop(pq)
            if prev and prev.end < cur.interval.start:
                result.append(Interval(prev.end, cur.interval.start))
            if not prev or prev.end < cur.interval.end:
                prev = cur.interval
            if cur.interval_idx + 1 < len(schedule[cur.employ_idx]):
                heapq.heappush(pq, EmployInterval(schedule[cur.employ_idx][cur.interval_idx + 1], cur.employ_idx,
                                                  cur.interval_idx + 1))
        return result
        
        