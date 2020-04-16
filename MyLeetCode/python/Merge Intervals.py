###
# Stack
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
###
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda e: e[0])
        result = []
        for e in intervals:
            if not result or result[-1][1] < e[0]:
                result.append(e)
            else:
                result[-1][1] = max(result[-1][1], e[1])
        return result
