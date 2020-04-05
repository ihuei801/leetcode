###
# Time Complexity: O(m*n + k) k: num of hits
# Space Complexity: O(m*n)
###
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        if not grid or not hits:
            return []
        # record the bricks that would eventually disappear
        # O(hits)
        for i, j in hits:
            if grid[i][j] == 1:
                grid[i][j] = 2
        m = len(grid)
        n = len(grid[0])
        # Initiate final state
        # O(m*n)
        dsu = DSU(m * n + 1)
        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == 1:
                    self.union_around(i, j, grid, dsu)
        cnt = dsu.cnts[dsu.find(m * n)]
        # Reconstruct the state before this hit
        # O(hits)
        result = []
        for i, j in reversed(hits):
            if grid[i][j] == 2:
                self.union_around(i, j, grid, dsu)
                grid[i][j] = 1  # before this hit, it is a brick
            new_cnt = dsu.cnts[dsu.find(m * n)]
            drop = max(new_cnt - cnt - 1, 0)
            result.append(drop)
            cnt = new_cnt
        return result[::-1]

    def union_around(self, i, j, grid, dsu):
        m = len(grid)
        n = len(grid[0])
        for nbi, nbj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n:
                if grid[nbi][nbj] == 1:
                    dsu.union(i * n + j, nbi * n + nbj)
            if i == 0:
                dsu.union(i * n + j, m * n)


class DSU(object):
    def __init__(self, n):
        self.roots = range(n)
        self.cnts = [1] * n

    def find(self, v):
        if self.roots[v] != v:
            self.roots[v] = self.find(self.roots[v])
        return self.roots[v]

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            self.roots[r2] = r1
            self.cnts[r1] += self.cnts[r2]
            return True
        return False
                    