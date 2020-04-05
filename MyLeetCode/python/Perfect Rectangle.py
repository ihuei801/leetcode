###
# Math
# The right answer must satisfy two conditions:
# (1) The formed rectangle area should be equal to the sum of all small rectangles
# (2) count of all points except the four corner points of the perfect rectangle should be even, 
#     and the four corner points of the perfect rectangle points should appear once
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        points = set()
        X1 = Y1 = float('inf') 
        X2 = Y2 = -float('inf')
        area = 0
        for x1, y1, x2, y2 in rectangles:
            X1 = min(X1, x1)
            Y1 = min(Y1, y1)
            X2 = max(X2, x2)
            Y2 = max(Y2, y2)
            area += (y2 - y1) * (x2 - x1)
            p1 = complex(x1, y1)
            p2 = complex(x1, y2)
            p3 = complex(x2, y1)
            p4 = complex(x2, y2)
            for p in (p1, p2, p3, p4):
                if p not in points:
                    points.add(p)
                else:
                    points.remove(p)
        return len(points) == 4 and complex(X1, Y1) in points and complex(X1, Y2) in points and complex(X2, Y1) in points and complex(X2, Y2) in points and area == (Y2 - Y1) * (X2 - X1)
                                        
                            
                    