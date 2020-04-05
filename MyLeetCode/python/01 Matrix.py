###
# BFS: Add to Queue->mark visit vs DFS: in node: mark visit
# Time Complexity: O(mn)
# Space Complexity: O(mn)
###
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        
        q = collections.deque()
        for i, row in enumerate(matrix):
            for j, e in enumerate(row):
                if e == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = float('inf')
       
        dis = 1
        while q:
            size = len(q)
            for _ in xrange(size):
                i, j = q.popleft()
                for nbi, nbj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and matrix[nbi][nbj] == float('inf'):
                        matrix[nbi][nbj] = dis
                        q.append((nbi, nbj))
        
            dis += 1
        return matrix

                                        
                            
                    