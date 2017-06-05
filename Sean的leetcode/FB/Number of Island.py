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
        if not grid:
            return 0
        num = 0
        for r in xrange(len(grid)):
            for c in xrange(len(grid[0])):
                if grid[r][c] == '1':
                    num += 1
                    self.dfs(grid, r, c)
        return num
        
    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return
        
        grid[r][c] = '0' 
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
            