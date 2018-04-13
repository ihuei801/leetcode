##
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
###
class Point(object):
    def __init__(self, pos, height, flag, index):
        self.pos = pos
        self.height = height
        self.flag = flag
        self.index = index
    def __cmp__(self, other):
        if self.pos < other.pos:
            return -1
        elif self.pos > other.pos:
            return 1
        elif self.flag == 's' and other.flag == 'e':
            return -1
        elif self.flag == 'e' and other.flag == 's':
            return 1
        elif self.flag == 's':
            if self.height > other.height:
                return -1
            elif self.height < other.height:
                return 1
            else:
                return 0
        elif self.flag == 'e':
            if self.height < other.height:
                return -1
            elif self.height > other.height:
                return 1
            else:
                return 0
class HashHeap(object):
    def __init__(self):
        self.heap = [0]
        self.hash = {}
        
    def add(self, key, value):
        self.heap.append((key, value))
        self.heap[0] += 1
        self.hash[key] = self.heap[0]
        self._shift_up(self.heap[0])
        
    def remove(self, key):
        index = self.hash[key]
        self._swap(index, self.heap[0])
        self.hash.pop(key)
        self.heap.pop()
        self.heap[0] -= 1
        if index <= self.heap[0]:
            index = self._shift_up(index)
            self._shift_down(index)
            
    def _swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        self.hash[self.heap[a][0]] = a
        self.hash[self.heap[b][0]] = b
        
    def _shift_up(self, index):
        while index > 1:
            if self.heap[index / 2][1] >= self.heap[index][1]:
                break
            self._swap(index, index/2)
            index = index / 2
        return index
    
    def _shift_down(self, index):
        size = self.heap[0]
        while index <= size:
            t = index
            if index * 2 <= size and self.heap[index * 2][1] > self.heap[t][1]:
                t = index * 2
            if index * 2 + 1 <= size and self.heap[index * 2 + 1][1] > self.heap[t][1]:
                t = index * 2 + 1
            if t == index:
                break
            self._swap(index, t)
            index = t
        return index
    
    def top(self):
        return 0 if self.heap[0] == 0 else self.heap[1][1]
    
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        from Queue import PriorityQueue
        points = PriorityQueue()
        for i, b in enumerate(buildings):
            points.put(Point(b[0], b[2], 's', i))
            points.put(Point(b[1], b[2], 'e', i))
        heights = HashHeap()
        re = []
        while not points.empty():
            cur = points.get()
            if cur.flag == 's':
                if not heights or cur.height > heights.top():
                    re.append([cur.pos, cur.height])
                heights.add(cur.index, cur.height)
            else:
                heights.remove(cur.index)
                if not heights or heights.top() < cur.height:
                    if not heights:
                        re.append([cur.pos, 0])
                    else:
                        re.append([cur.pos, heights.top()])
        return re
            
    


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from heapq import heappush, heappop
        i = 0
        q = []
        re = []
        while i < len(buildings) or q:
            if i < len(buildings):
                x = buildings[i][0]
            #non-overlapped with the current top
            if i == len(buildings) or (q and x > q[0][1]):
                x = q[0][1]
                while q and q[0][1] <= x:
                    heappop(q)
                h = -q[0][0] if q else 0
            #overlapped with the current top
            else:
                while i < len(buildings) and buildings[i][0] == x:
                    heappush(q, (-buildings[i][2], buildings[i][1]))
                    i += 1
                h = -q[0][0]
            if not re or re[-1][1] != h:
                re.append([x, h])
        return re