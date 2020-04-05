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
        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == "1":
                    num += 1
                    self.dfs(grid, i, j) #mark visit
        return num
    
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        grid[i][j] = "#"
        for nbi, nbj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and grid[nbi][nbj] == '1':
                self.dfs(grid, nbi, nbj)
        
        
            