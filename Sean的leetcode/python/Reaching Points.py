###
# Math
# Start from target and go back to start
# If sx,sy occurs in the path of Euclidean method to get GCD (by subtracting lesser value from greater value) of tx,ty, then return true.
# To see why this is true, consider how the tx, ty could have been formed if tx > ty. Let ax, ay be the pair in previous step. It cannot be ax, ax+ay because both ax and ay are greater than 0. 
# So the only other possibility is ax+ay, ay. This means ay = ty and ax = tx-ty. 
# Now we can optimize this subtraction a bit by doing ax = tx % ty since we will keep subtracting ty from tx until tx < ty.
# One special case we need to handle during this optimization is when tx=9,ty=3,sx=6, sy=3 
# which can be covered using the condition if(sy == ty) and (tx - sx) % ty == 0;
# Similar argument applies for tx <= ty
# Time Complexity: O(log(max(tx, ty)))
# Space Complexity: O(1)
###
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx<tx and sy<ty: tx,ty = tx%ty,ty%tx
        return sx==tx and (ty-sy)%sx==0 or sy==ty and (tx-sx)%sy==0
                            
                    