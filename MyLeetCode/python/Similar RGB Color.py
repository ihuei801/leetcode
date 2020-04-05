###
# Math
# Time Complexity: O(1)
# Space Complexity: O(1)
###
class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        return "#" + self.close(color[1:3]) + self.close(color[3:5]) + self.close(color[5:])
    
    def close(self, s):
        max_sim = -float('inf')
        re = None
        for d in xrange(16):
            num = d * 16 + d
            sim = - (num - int(s, 16))**2
            if sim > max_sim:
                max_sim = sim
                re = num    
        return '{:02x}'.format(re)
            
            
                    
                            
                    