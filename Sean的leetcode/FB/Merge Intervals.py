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
        stack = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if stack and interval.start <= stack[-1].end:
                stack[-1].end = max(stack[-1].end, interval.end)
            else:
                stack.append(interval)
        return stack