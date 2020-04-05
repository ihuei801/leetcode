###
# Stack
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
###

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        stack = []
        last = intervals[0]
        for i in xrange(1, len(intervals)):
            if intervals[i].start > last.end:
                stack.append(last)
                last = intervals[i]
            else:
                last.start = min(last.start, intervals[i].start)
                last.end = max(last.end, intervals[i].end)
        stack.append(last)
                
        return stack