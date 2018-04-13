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
        rows = len(grid)
        cols = len(grid[0])
        dis = [[0] * cols for _ in xrange(rows)]
        visit = [[0] * cols for _ in xrange(rows)]
        total_num = 0
        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == 1:
                    self.bfs(grid, i, j, dis, visit)
                    total_num += 1
        min_dis = float('inf')
        for i, row in enumerate(visit):
            for j, e in enumerate(row):
                if e == total_num:
                    min_dis = min(min_dis, dis[i][j])
        return min_dis if min_dis != float('inf') else -1
    
    def bfs(self, grid, r, c, dis, visit):
        rows = len(grid)
        cols = len(grid[0])
        d = [(1,0), (-1,0), (0,1), (0,-1)]
        level = 1
        q = [(r,c)]
        visited = set((r,c))
        while q:
            next_q = []
            for i, j in q:
                for d_i, d_j in d:
                    nb_i = i + d_i
                    nb_j = j + d_j
                    if nb_i >= 0 and nb_i < rows and nb_j >= 0 and nb_j < cols and grid[nb_i][nb_j] == 0 and (nb_i, nb_j) not in visited:
                        dis[nb_i][nb_j] += level
                        visit[nb_i][nb_j] += 1
                        next_q.append((nb_i, nb_j))
                        visited.add((nb_i, nb_j))
            q = next_q
            level += 1
        