###
# Array
# Time Complexity: O(n*m) n:row m:col k:len of word
# Space Complexity: O(1)
###
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        land = 0
        nb = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == 1:
                    land += 1
                    if j+1 < len(row) and row[j+1] == 1:
                        nb += 1
                    if i+1 < len(grid) and grid[i+1][j] == 1:
                        nb += 1
        return land * 4 - nb * 2
        
        