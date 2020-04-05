###
# Two Pointers
# 1. The order of R and L must be the same
# 2. L can only move to left, R can only move to right
# Time Complexity: O(max(m,n))
# Space Complexity: O(1)
###
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(start) or j < len(end):
            
            while i < len(start) and start[i] == 'X':
                i += 1
            while j < len(end) and end[j] == 'X':
                j += 1
            if i == len(start) and j == len(end):
                return True
            elif i == len(start) or j == len(end) or start[i] != end[j]:
                return False
            
            if start[i] == 'L' and i < j:
                return False
            elif start[i] == 'R' and i > j:
                return False
            else:
                i += 1
                j += 1
        return True
                                        
                            
                    