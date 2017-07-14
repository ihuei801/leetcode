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
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in direc:
            self.dfs(grid, i + dr, j + dc)
        
            