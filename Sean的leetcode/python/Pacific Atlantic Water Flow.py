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
        rows = len(matrix)
        cols = len(matrix[0])
        p_visit = [[False] * cols for i in xrange(rows)]
        a_visit = [[False] * cols for i in xrange(rows)]  
        for j in xrange(cols): 
            self.dfs(matrix, 0, j, p_visit)   
            self.dfs(matrix, rows - 1, j, a_visit)
        for i in xrange(rows):  
            self.dfs(matrix, i, 0, p_visit)     
            self.dfs(matrix, i, cols - 1, a_visit)
        re = [[i, j] for i in xrange(rows) for j in xrange(cols) if a_visit[i][j] and p_visit[i][j]]
        return re
    
    def dfs(self, matrix, i, j, visit): 
        rows = len(matrix)
        cols = len(matrix[0])
        if visit[i][j]:
            return
        visit[i][j] = True
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for di, dj in direc:
            nbi = i + di
            nbj = j + dj      
            if nbi >= 0 and nbi < rows and nbj >= 0 and nbj < cols and matrix[nbi][nbj] >= matrix[i][j]: 
                self.dfs(matrix, nbi, nbj, visit)
                
                
        