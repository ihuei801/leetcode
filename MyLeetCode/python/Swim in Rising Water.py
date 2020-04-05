###
# Heap (Priority Queue)
# Time Complexity: O(n^2logn)
# Space Complexity: O(n^2)
###
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        pq = [(grid[0][0], 0, 0)]
        visit = {(0,0)}
        re = 0
        while pq:
            d, i, j = heapq.heappop(pq)
            re = max(re, d)
            if i == j == len(grid)-1:
                return re
            for nbi, nbj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if nbi >= 0 and nbj >= 0 and nbi < len(grid) and nbj < len(grid[0]) and (nbi, nbj) not in visit:
                    visit.add((nbi, nbj))
                    heapq.heappush(pq, (grid[nbi][nbj], nbi, nbj))
                            
                    