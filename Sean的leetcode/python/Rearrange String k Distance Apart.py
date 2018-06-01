###
# Priority Queue
# Time Complexity: O(n) + O(26) + O(26log26) = O(n)
# Space Complexity: O(26) = O(1)
###
class Element(object):
    def __init__(self, cnt, c):
        self.cnt = cnt
        self.c = c
    def __cmp__(self, other):
        if self.cnt != other.cnt:
            return self.cnt < other.cnt
        return self.c > other.c
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not k:
            return s
        from collections import Counter, deque
        import heapq
        q = []
        cnt = Counter(s)
        re = []
        q = [Element(n, c) for c, n in cnt.iteritems()]
        heapq.heapify(q)
        while q: 
            tmp = []
            for i in xrange(k):
                if not q:
                    if tmp:
                        return ""
                    break
                top = heapq.heappop(q)
                re.append(top.c)
                top.cnt -= 1
                if top.cnt > 0:
                    tmp.append(top) 
            if tmp:
                for e in tmp:
                    heapq.heappush(q, e)   
        return "".join(re) 
        
        
        