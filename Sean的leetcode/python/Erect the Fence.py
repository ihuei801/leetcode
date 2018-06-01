###
# Monotone Chain
# https://leetcode.com/problems/erect-the-fence/solution/
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
###
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        if len(points) <= 2:
            return points
        points.sort(key=lambda p: (p.x, p.y))
        L = []
        for p in points:
            while len(L) >= 2 and self.cross(L[-2], L[-1], p) < 0:
                L.pop()
            L.append(p)
        U = []
        for p in reversed(points):
            while len(U) >= 2 and self.cross(U[-2], U[-1], p) < 0:
                U.pop()
            U.append(p)
        return list(set(L + U))
    def cross(self, o, a, b):
        return (a.x-o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
                                        
                            
                    