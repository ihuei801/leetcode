###
# Graph DFS/BFS
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
###
#DFS
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not maze[0] or not start or not destination:
            return False
        return self.dfs(maze, start, destination, set())
    
    def dfs(self, maze, start, destination, visit):
        if start == destination:
            return True
        visit.add(tuple(start))
        m = len(maze)
        n = len(maze[0])
        drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for di, dj in drc:
            i, j = start
            while i + di >= 0 and i + di < m and j + dj >= 0 and j + dj < n and maze[i+di][j+dj] == 0:
                i += di
                j += dj  
            if (i, j) not in visit and self.dfs(maze, [i, j], destination, visit):
                return True
        return False
            
            
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not maze[0] or not start or not destination:
            return False
        return self.dfs(maze, start, destination, set())
    
    def dfs(self, maze, start, destination, visit):
        if start == destination:
            return True
        if tuple(start) in visit:
            return False
        visit.add(tuple(start))
        m = len(maze)
        n = len(maze[0])
        drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for di, dj in drc:
            i, j = start
            while i + di >= 0 and i + di < m and j + dj >= 0 and j + dj < n and maze[i+di][j+dj] == 0:
                i += di
                j += dj  
            if self.dfs(maze, [i, j], destination, visit):
                return True
        return False
        
#BFS
class Solution(object):
    def hasPath(self, maze, start, destination):
        q = collections.deque()
        q.append(start)
        visit = set()
        direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            si, sj = q.popleft()
            if [si, sj] == destination:
                return True
            if (si, sj) in visit:
                continue
            visit.add((si, sj))
            for di, dj in direc:
                i, j = si, sj
                while i + di >= 0 and i + di < len(maze) and j + dj >= 0 and j + dj < len(maze[0]) and maze[i + di][j + dj] != 1:
                    i += di
                    j += dj            
                q.append([i,j])
            
        return False


            
            


