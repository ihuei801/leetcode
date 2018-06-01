###
# Heap
# Time: O(klogk)
# Space: O(k)
###
class Value(object):
    def __init__(self, v, i, j):
        self.v = v
        self.i = i
        self.j = j
    def __cmp__(self, other):
        if self.v < other.v:
            return -1
        elif self.v > other.v:
            return 1
        else:
            return 0
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        if not matrix or not matrix[0]:
            return 0
        q = []
        heapq.heappush(q, Value(matrix[0][0], 0, 0))
        cur = None
        while q and k:
            cur = heapq.heappop(q)   
            k -= 1
            if cur.j + 1 < len(matrix[0]):
                heapq.heappush(q, Value(matrix[cur.i][cur.j + 1], cur.i, cur.j + 1))
            if cur.i + 1 < len(matrix) and cur.j == 0:
                heapq.heappush(q, Value(matrix[cur.i + 1][cur.j], cur.i + 1, cur.j))
        return cur.v
class Value(object):
    def __init__(self, v, i, j):
        self.v = v
        self.i = i
        self.j = j
    def __cmp__(self, other):
        if self.v < other.v:
            return -1
        elif self.v > other.v:
            return 1
        else:
            return 0
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from Queue import PriorityQueue
        if not matrix or not matrix[0]:
            return 0
        q = PriorityQueue()
        q.put(Value(matrix[0][0], 0, 0))
        cur = None
        while not q.empty() and k:
            cur = q.get()       
            k -= 1
            if cur.j + 1 < len(matrix[0]):
                q.put(Value(matrix[cur.i][cur.j + 1], cur.i, cur.j + 1))
            if cur.i + 1 < len(matrix) and cur.j == 0:
                q.put(Value(matrix[cur.i + 1][cur.j], cur.i + 1, cur.j))
        return cur.v
        return re
        
        