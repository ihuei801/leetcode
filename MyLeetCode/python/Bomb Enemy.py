###
# DP
# Time Complexity: O(mn*(m+n)) -> O(mn)
# Space Complexity: O(n)
###
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        maxhit = 0
        rowhit = 0
        colhits = [0] * len(grid[0])
        rows = len(grid)
        cols = len(grid[0])
        for i in xrange(rows):
            for j in xrange(cols):
                if not j or grid[i][j-1] == 'W':     
                    rowhit = 0
                    for k in xrange(j, cols):
                        if grid[i][k] == 'W':
                            break
                        rowhit += (grid[i][k] == 'E')
                      
                if not i or grid[i-1][j] == 'W':
                    colhits[j] = 0
                    for k in xrange(i, rows):
                        if grid[k][j] == 'W':
                            break
                        colhits[j] += (grid[k][j] == 'E')
                if grid[i][j] == '0':
                    maxhit = max(maxhit, rowhit + colhits[j])
                    
        return maxhit
                        
                    