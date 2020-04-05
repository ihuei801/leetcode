###
# 2D Array
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dx = 0
        dy = 0
        for m in moves:
            if m == "U":
                dy += 1
            elif m == "D":
                dy -= 1
            elif m == "R":
                dx += 1
            else:
                dx -= 1       
        return dx == 0 and dy == 0
                                        
                            
                    