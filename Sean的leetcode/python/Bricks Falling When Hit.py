###
# Design Deque
# Time Complexity: hasNext:  O(1) next O(1)
# Space Complexity: O(n)
###
class DSU(object):
    def __init__(self, size):
        self.root = range(size)
        self.cnt = [1] * size
    def find(self, e):
        if self.root[e] != e:
            self.root[e] = self.find(self.root[e])
        return self.root[e]
    def union(self, e1, e2):
        r1 = self.find(e1)
        r2 = self.find(e2)
        if r1 != r2:
            self.root[r1] = r2
            self.cnt[r2] += self.cnt[r1]
        
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        
        m = len(grid)
        n = len(grid[0])
        dsu = DSU(m*n+1)
        #O(hits)
        for hitr, hitc in hits:
            if grid[hitr][hitc] == 1:
                grid[hitr][hitc] = 2
        
        #O(mn)
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == 1:
                    self.union_around(i, j, grid, dsu)
        cnt = dsu.cnt[dsu.find(m*n)]
        re = []
        #O(hits)
        for i, j in reversed(hits):
            if grid[i][j] == 2:
                self.union_around(i, j, grid, dsu)
                grid[i][j] = 1
            newcnt = dsu.cnt[dsu.find(m*n)]
            drop = max(newcnt - cnt - 1, 0)
            re.append(drop)
            cnt = newcnt
        return re[::-1]
    def union_around(self, i, j, grid, dsu):
        m = len(grid)
        n = len(grid[0])
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for di, dj in direc:
            nbi = i + di
            nbj = j + dj
            if nbi >= 0 and nbj >= 0 and nbi < m and nbj < n and grid[nbi][nbj] == 1:
                dsu.union(i*n+j, nbi*n+nbj)
            if i == 0:
                dsu.union(i*n+j, m*n)
                            
                    