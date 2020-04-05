###
# Heap
# Time: O(mnlog(m+n))
# Space: O(mn)
###
class Cell(object):
    def __init__(self, i, j, h):
        self.i = i
        self.j = j
        self.h = h
    def __cmp__(self, other):
        if self.h < other.h:
            return -1
        elif self.h > other.h:
            return 1
        else:
            return 0
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        import heapq
        q = []
        visit = [[False] * len(heightMap[0]) for i in xrange(len(heightMap))]
        for i in xrange(len(heightMap)):
            heapq.heappush(q, Cell(i, 0, heightMap[i][0]))
            heapq.heappush(q, Cell(i, len(heightMap[0]) - 1, heightMap[i][len(heightMap[0]) - 1]))
            visit[i][0] = True
            visit[i][len(heightMap[0]) - 1] = True
        for j in xrange(len(heightMap[0])):
            heapq.heappush(q, Cell(0, j, heightMap[0][j]))
            heapq.heappush(q, Cell(len(heightMap) - 1, j, heightMap[len(heightMap) - 1][j]))
            visit[0][j] = True
            visit[len(heightMap) - 1][j] = True
        re = 0
        direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            top = heapq.heappop(q)
            for di, dj in direc:
                nbi = top.i + di
                nbj = top.j + dj
                if nbi >= 0 and nbj >= 0 and nbi < len(heightMap) and nbj < len(heightMap[0]) and not visit[nbi][nbj]:
                    border = max(top.h, heightMap[nbi][nbj])
                    re += border - heightMap[nbi][nbj]
                    visit[nbi][nbj] = True
                    heapq.heappush(q, Cell(nbi, nbj, border))
        return re
                  
            
class Cell(object):
    def __init__(self, i, j, h):
        self.i = i
        self.j = j
        self.h = h
    def __cmp__(self, other):
        if self.h < other.h:
            return -1
        elif self.h > other.h:
            return 1
        else:
            return 0
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        from Queue import PriorityQueue
        q = PriorityQueue()
        visit = [[False] * len(heightMap[0]) for i in xrange(len(heightMap))]
        for i in xrange(len(heightMap)):
            q.put(Cell(i, 0, heightMap[i][0]))
            q.put(Cell(i, len(heightMap[0]) - 1, heightMap[i][len(heightMap[0]) - 1]))
            visit[i][0] = True
            visit[i][len(heightMap[0]) - 1] = True
        for j in xrange(len(heightMap[0])):
            q.put(Cell(0, j, heightMap[0][j]))
            q.put(Cell(len(heightMap) - 1, j, heightMap[len(heightMap) - 1][j]))
            visit[0][j] = True
            visit[len(heightMap) - 1][j] = True
        re = 0
        direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while not q.empty():
            top = q.get()
            for di, dj in direc:
                nbi = top.i + di
                nbj = top.j + dj
                if nbi >= 0 and nbj >= 0 and nbi < len(heightMap) and nbj < len(heightMap[0]) and not visit[nbi][nbj]:
                    border = max(top.h, heightMap[nbi][nbj])
                    re += border - heightMap[nbi][nbj]
                    visit[nbi][nbj] = True
                    q.put(Cell(nbi, nbj, border))
        return re
                  
            
        
        