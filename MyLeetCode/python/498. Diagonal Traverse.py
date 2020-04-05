###
# 2D Array
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
###
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        r, c = 0, 0
        rows = len(matrix)
        cols = len(matrix[0])
        re = []
        d = 1
        for i in xrange(rows * cols):
            re.append(matrix[r][c])
            if (r+c) & 1: #down
                if r == rows-1: #check right/down boundary first
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
            else: #up
                if c == cols-1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
                
        
        return re
                
                
                                        
                            
                    