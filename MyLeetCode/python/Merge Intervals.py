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
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        re = []
        for it in intervals: 
            if not re or re[-1].end < it.start:
                re.append(it)
            else:
                re[-1].end = max(re[-1].end, it.end)
        return re