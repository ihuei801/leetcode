###
# Array 2D
# Time Complexity: O(mn)
# Space Complexity: O(n+m)
###
class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        m = len(picture)
        n = len(picture[0])
        if not m or not n:
            return 0
        d = collections.Counter()
        colcnt = [0] * n
        for i, row in enumerate(picture): #filter row & count col
            rowcnt = 0 
            for j, c in enumerate(row):
                if c == 'B':
                    rowcnt += 1
                    colcnt[j] += 1
            if rowcnt == N:
                d[tuple(row)] += 1
        res = 0
        for k, cnt in d.iteritems(): 
            if cnt == N: #filter pattern
                for j, c in enumerate(k):
                    if c == 'B' and colcnt[j] == N: #filter col
                        res += N 
        return res
            
                                        
                            
                    