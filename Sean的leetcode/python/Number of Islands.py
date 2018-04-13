###
# Time Complexity: O(m*n)
# Space Complexity: O(m*n) recursive call
###
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        num = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    num += 1
                    self.dfs(grid, i, j)
        return num
    def dfs(self, grid, i, j):
        rows = len(grid)
        cols = len(grid[0])
        grid[i][j] = '0'
        direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for di, dj in direc:
            nbi = i + di
            nbj = j + dj
            if nbi >= 0 and nbi < rows and nbj >= 0 and nbj < cols and grid[nbi][nbj] == '1':
                self.dfs(grid, nbi, nbj)
        
        
            