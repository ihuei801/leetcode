###
# DFS
# Time Complexity: O(n*m) n:row m:col k:len of word
# Space Complexity: O(n*m)
###
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        max_len = 0
        dis = [[0] * cols for i in xrange(rows)]
        for i in xrange(rows):
            for j in xrange(cols):
                max_len = max(max_len, self.dfs(matrix, i, j, dis))
        return max_len
    
    def dfs(self, matrix, i, j, dis):
        rows = len(matrix)
        cols = len(matrix[0])
        if dis[i][j] != 0:
            return dis[i][j]
        dis[i][j] = 1
        direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for di, dj in direc:
            nbi = i + di
            nbj = j + dj
            if nbi >= 0 and nbi < rows and nbj >= 0 and nbj < cols and matrix[nbi][nbj] > matrix[i][j]:
                dis[i][j] = max(dis[i][j], self.dfs(matrix, nbi, nbj, dis) + 1)
        return dis[i][j]
        
        