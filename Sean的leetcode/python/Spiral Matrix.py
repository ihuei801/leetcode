###
# Array
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
###
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        u, d = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        re = []
        while u <= d and l <= r:
            for j in xrange(l, r+1):
                re.append(matrix[u][j])
            u += 1
            if u > d:
                break
            for i in xrange(u, d+1):
                re.append(matrix[i][r])
            r -= 1
            if r < l:
                break
            for j in xrange(r, l-1, -1):
                re.append(matrix[d][j])
            d -= 1
            if d < u:
                break
            for i in xrange(d, u-1, -1):
                re.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return re
                                        
                            
                    