###
# DFS
# Time Complexity: O(n*m) n:row m:col k:len of word
# Space Complexity: O(n*m)
###
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        p_visit = [[False] * n for i in xrange(m)]
        a_visit = [[False] * n for i in xrange(m)]
        
        for j in xrange(n):
            if not p_visit[0][j]:
                self.dfs(matrix, 0, j, p_visit)
            if not a_visit[m-1][j]:
                self.dfs(matrix, m-1, j, a_visit)
        for i in xrange(m):
            if not p_visit[i][0]:
                self.dfs(matrix, i, 0, p_visit)
            if not a_visit[i][n-1]:
                self.dfs(matrix, i, n-1, a_visit)
        return [[i, j] for i in xrange(m) for j in xrange(n) if p_visit[i][j] and a_visit[i][j]]
    
    def dfs(self, matrix, i, j, visit):      
        visit[i][j] = True
        m = len(matrix)
        n = len(matrix[0])
        for nbi, nbj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and matrix[nbi][nbj] >= matrix[i][j] and not visit[nbi][nbj]:
                self.dfs(matrix, nbi, nbj, visit)
                

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        p_visit = [[False] * n for i in xrange(m)]
        a_visit = [[False] * n for i in xrange(m)]
        
        for j in xrange(n):
            self.dfs(matrix, 0, j, p_visit)
            self.dfs(matrix, m-1, j, a_visit)
        for i in xrange(m):
            self.dfs(matrix, i, 0, p_visit)
            self.dfs(matrix, i, n-1, a_visit)
        return [[i, j] for i in xrange(m) for j in xrange(n) if p_visit[i][j] and a_visit[i][j]]
    
    def dfs(self, matrix, i, j, visit):
        if visit[i][j]:
            return
        visit[i][j] = True 
        m = len(matrix)
        n = len(matrix[0])
        for nbi, nbj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and matrix[nbi][nbj] >= matrix[i][j]:
                self.dfs(matrix, nbi, nbj, visit)








                
                
        