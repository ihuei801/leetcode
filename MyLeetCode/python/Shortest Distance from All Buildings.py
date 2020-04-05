###
# BFS
# Time Complexit: O(m^2n^2)
# Space Complexity: O(mn)
###
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        dist = [[0] * n for i in xrange(m)]
        cnt = [[0] * n for i in xrange(m)]
        total = 0
        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == 1:
                    self.bfs(grid, i, j, dist, cnt)
                    total += 1
        mindis = float('inf')
        for i, row in enumerate(dist):
            for j, e in enumerate(row):
                if cnt[i][j] == total:
                    mindis = min(mindis, e)
                    
        return mindis if mindis != float('inf') else -1
    
    def bfs(self, grid, i, j, dist, cnt):
        m = len(grid)
        n = len(grid[0])
        q = collections.deque([(i, j)])
        dis = 1
        visit = [[False] * n for i in xrange(m)]
        while q:
            size = len(q)
            for _ in xrange(size):
                i, j = q.popleft()
                for nbi, nbj in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                    if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and grid[nbi][nbj] == 0 and not visit[nbi][nbj]:
                        visit[nbi][nbj] = True
                        dist[nbi][nbj] += dis
                        cnt[nbi][nbj] += 1
                        q.append((nbi, nbj))
            dis += 1
    
        