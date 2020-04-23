###
# Time Complexity: O(n)
# Space Complexity: O(n)
###
# Method 1
# Stack
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
            i += 1
        result.append(newInterval)
        while i < len(intervals):
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][0] = min(result[-1][0], intervals[i][0])
                result[-1][1] = max(result[-1][1], intervals[i][1])
            i += 1
        return result


# Method 2
# Use merge
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
        idx = 0
        for i, it in enumerate(intervals):
            if it.start < newInterval.start:
                idx = i + 1
            else:
                break
        intervals.insert(idx, newInterval)
        return self.merge(intervals)
    def merge(self, intervals):
        if not intervals:
            return []
        re = []
        for it in intervals:
            if not re or re[-1].end < it.start:
                re.append(it)
            else:
                re[-1].end = max(re[-1].end, it.end)
        return re


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
                stack.append(newInterval)     # value reference, not the variable itself
                newInterval = e               # ref: https://stackoverflow.com/questions/12080552/python-list-doesnt-reflect-variable-change 
            else:
                newInterval.start = min(newInterval.start, e.start)
                newInterval.end = max(newInterval.end, e.end)
        stack.append(newInterval)
        return stack
                
        
        