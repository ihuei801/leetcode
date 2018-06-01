###
# Graph: BFS
# Time Complexity: O(mn*max(m,n))
# Space Complexity: O(mn)
###
#BFS: Dijkstra shortest path
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0] or not start or not destination:
            return -1
        m = len(maze)
        n = len(maze[0])
        dis = [[float('inf')] * n for i in xrange(m)]
        q = collections.deque([(0, start)])
        drc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            topdis, [topi, topj] = q.popleft()
            for di, dj in drc:
                i, j = topi, topj
                d = 0
                while i + di >= 0 and i + di < m and j + dj >= 0 and j + dj < n and maze[i+di][j+dj] == 0:
                    i += di
                    j += dj
                    d += 1 
                if topdis + d < dis[i][j]:
                    dis[i][j] = topdis + d
                    q.append((topdis+d, [i, j]))
           
        return dis[destination[0]][destination[1]] if dis[destination[0]][destination[1]] != float('inf') else -1
    
        
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0] or not start or not destination:
            return -1
        m = len(maze)
        n = len(maze[0])
        dis = [[float('inf')] * n for i in xrange(m)]
        q = collections.deque([(0, start)])
        drc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            topdis, [topi, topj] = q.popleft()
            if topdis >= dis[topi][topj]: #必須要取出來是檢查因為可能不同的上一層都走到這個點，無法再加入queue時檢查
                continue
            dis[topi][topj] = topdis
            for di, dj in drc:
                i, j = topi, topj
                d = 0
                while i + di >= 0 and i + di < m and j + dj >= 0 and j + dj < n and maze[i+di][j+dj] == 0:
                    i += di
                    j += dj
                    d += 1 
                q.append((topdis+d, [i, j]))
           
        return dis[destination[0]][destination[1]] if dis[destination[0]][destination[1]] != float('inf') else -1
    
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0] or not start or not destination:
            return -1
        m = len(maze)
        n = len(maze[0])
        dis = [[float('inf')] * n for i in xrange(m)]
        q = [(0, start)]
        drc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            topdis, [topi, topj] = heapq.heappop(q) 
            if topdis >= dis[topi][topj]:
                continue
            if [topi, topj] == destination: #early termination, the only benefit of using priority queue
                return topdis
            dis[topi][topj] = topdis
            for di, dj in drc:
                i, j = topi, topj
                d = 0
                while i + di >= 0 and i + di < m and j + dj >= 0 and j + dj < n and maze[i+di][j+dj] == 0:
                    i += di
                    j += dj
                    d += 1 
                heapq.heappush(q, (topdis+d, [i, j]))
           
        return dis[destination[0]][destination[1]] if dis[destination[0]][destination[1]] != float('inf') else -1
    
        


    
        
       
#DFS TLE
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        dis = [[float('inf')] * len(maze[0]) for i in xrange(len(maze))]
        dis[start[0]][start[1]] = 0
        self.dfs(maze, start, dis)
        return dis[destination[0]][destination[1]] if dis[destination[0]][destination[1]] != float('inf') else -1
    
    def dfs(self, maze, start, dis):
        i, j = start[0], start[1]
        up, down, left, right = i, i, j, j
        while up-1 >= 0 and maze[up-1][j] != 1:
            up -= 1      
        if dis[i][j] + abs(up-i) < dis[up][j]:   
            dis[up][j] = dis[i][j] + abs(up-i)
            self.dfs(maze, [up, j], dis)
        while down+1 < len(maze) and maze[down+1][j] != 1:
            down += 1  
        if dis[i][j] + abs(down-i) < dis[down][j]:
            dis[down][j] = dis[i][j] + abs(down-i)
            self.dfs(maze, [down, j], dis)
        while left-1 >= 0 and maze[i][left-1] != 1:
            left -= 1
        if dis[i][j] + abs(left-j) < dis[i][left]:   
            dis[i][left] = dis[i][j] + abs(left-j)
            self.dfs(maze, [i, left], dis) 
        while right+1 < len(maze[0]) and maze[i][right+1] != 1:
            right += 1
        if dis[i][j] + abs(right-j) < dis[i][right]: 
            dis[i][right] = dis[i][j] + abs(right-j)
            self.dfs(maze, [i, right], dis) 
        
       
                                        
                            
                    