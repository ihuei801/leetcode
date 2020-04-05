###
# Math
# For each set of three adjacent points A, B, C, find the cross product AB x BC. If the sign of
# all the cross products is the same, the angles are all positive or negative (depending on the
# order in which we visit them) so the polygon is convex.
# cross product AB x BC.
# The cross product is a vector perpendicular to AB and BC having length |AB| * |BC| * Sin(theta) and
# with direction given by the right-hand rule. For two vectors in the X-Y plane, the result is a
# vector with X and Y components 0 so the Z component gives the vector's length and direction.
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) < 3:
            return False
        neg, pos = False, False
        for i, A in enumerate(points):
            B = points[(i+1) % len(points)]
            C = points[(i+2) % len(points)]
            cp = self.cross_product(A, B, C)
            if cp < 0:
                neg = True
            if cp > 0:
                pos = True
            if neg and pos:
                return False
        return True
    
    def cross_product(self, A, B, C):
        BAx = A[0] - B[0]
        BAy = A[1] - B[1]
        BCx = C[0] - B[0]
        BCy = C[1] - B[1]
        return BAx * BCy - BCx * BAy
                                        
                            
                    