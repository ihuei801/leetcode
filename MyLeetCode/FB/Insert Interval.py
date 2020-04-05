###
# Time Complexity: O(n)
# Space Complexity: O(n)
###
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        stack = []
        for e in intervals:
            if e.end < newInterval.start:
                stack.append(e)
            elif newInterval.end < e.start:
                stack.append(newInterval)
                newInterval = e
            else:
                newInterval.start = min(newInterval.start, e.start)
                newInterval.end = max(newInterval.end, e.end)
        stack.append(newInterval)
        return stack
                
        
        