###
# DFS/DP
# memo[i][j]: longest increasing path starts from [i,j]
# 不可能往回走，因為increasing，不需要記visit
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
        m = len(matrix)
        n = len(matrix[0])
        self.max_len = 0
        memo = [[0] * n for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                cur = self.dfs(matrix, i, j, memo)
        return self.max_len
    
    def dfs(self, matrix, i, j, memo):
        m = len(matrix)
        n = len(matrix[0])
        memo[i][j] = 1
        for nbi, nbj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):            
            if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and matrix[nbi][nbj] > matrix[i][j]:  
                if memo[nbi][nbj] != 0:
                    memo[i][j] = max(memo[i][j], 1 + memo[nbi][nbj])
                else:
                    memo[i][j] = max(memo[i][j], 1 + self.dfs(matrix, nbi, nbj, memo))
        self.max_len = max(memo[i][j], self.max_len)
        return memo[i][j]
        
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        self.max_len = 0
        memo = [[0] * n for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                cur = self.dfs(matrix, i, j, memo)
        return self.max_len
    
    def dfs(self, matrix, i, j, memo):
        if memo[i][j] != 0:
            return memo[i][j]
        m = len(matrix)
        n = len(matrix[0])
        memo[i][j] = 1
        for nbi, nbj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):            
            if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and matrix[nbi][nbj] > matrix[i][j]:        
                memo[i][j] = max(memo[i][j], 1 + self.dfs(matrix, nbi, nbj, memo))
        self.max_len = max(memo[i][j], self.max_len)
        return memo[i][j]
        
        