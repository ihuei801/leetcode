###
# 2D array
# Time Complexity: O(mn)
# Space Complexity: O(min(m,n))
###
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        m = len(picture)
        n = len(picture[0])
        if not m or not n:
            return 0
        res = 0
        colcnt = [0] * n
        for i, row in enumerate(picture): #count col
            for j, c in enumerate(row):
                if c == 'B': 
                    colcnt[j] += 1
            
        for i, row in enumerate(picture): 
            rowcnt = 0
            pos = -1
            for j, c in enumerate(row):
                if c == 'B':
                    rowcnt += 1
                    pos = j
            if rowcnt == 1 and colcnt[pos] == 1: #filter row and col
                res += 1
        return res                  
                            
                    