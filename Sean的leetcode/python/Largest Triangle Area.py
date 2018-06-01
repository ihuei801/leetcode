###
# Array
# Time Complexity: hasNext:  O(n^3)
# Space Complexity: O(1)
###
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        if len(points) < 3:
            return 0
        return max(self.area(*triangle) for triangle in itertools.combinations(points, 3))
        
    def area(self, p1, p2, p3):
        return 0.5 * abs(p1[0] * (p2[1]-p3[1]) + p2[0] * (p3[1]-p1[1]) + p3[0] * (p1[1]-p2[1]))
                                        
                            
                    