###
# Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        d = defaultdict(set)
        max_v = -float('inf')
        min_v = float('inf')
        for x, y in points:
            d[y].add(x)
            max_v = max(max_v, x)
            min_v = min(min_v, x)
        for x, y in points:
            if (max_v + min_v - x) not in d[y]:
                return False
        return True
        