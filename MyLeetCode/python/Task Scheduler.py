 ###
#Time Complexity: O(n) + O(26)  + O(26log26) = O(n)
#Space Complexity: O(26) = O(1)
###
class Task(object):
    def __init__(self, task, cnt):
        self.task = task
        self.cnt = cnt
    def __cmp__(self, other):
        if self.cnt > other.cnt:
            return -1
        elif self.cnt < other.cnt:
            return 1     
        else:
            return 0
    
        
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        from Queue import PriorityQueue
        if not tasks:
            return 0
        if not n:
            return len(tasks)
        d = Counter(tasks)
        q = PriorityQueue()
        for k, v in d.iteritems():
            q.put(Task(k, v))
        it = 0
        
        while not q.empty():
            tmp = []
            for i in xrange(n+1):
                if q.empty():
                    if tmp:
                        it += n + 1 - i
                    break
                cur = q.get()
                cur.cnt -= 1
                if cur.cnt > 0:
                    tmp.append(cur)
                it += 1
            if tmp:
                for t in tmp:
                    q.put(t)
        return it
                
            
                
            
class Task(object):
    def __init__(self, task, cnt):
        self.task = task
        self.cnt = cnt
    def __cmp__(self, other):
        if self.cnt > other.cnt:
            return -1
        elif self.cnt < other.cnt:
            return 1     
        else:
            return 0
    
        
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        from Queue import PriorityQueue
        if not tasks:
            return 0
        d = Counter(tasks)
        q = PriorityQueue()
        for k, v in d.iteritems():
            q.put(Task(k, v))
        it = 0
        
        while not q.empty():
            k = n + 1
            tmp = []
            while k and not q.empty():
                cur = q.get()
                cur.cnt -= 1
                if cur.cnt > 0:
                    tmp.append(cur)
                k -= 1
                it += 1
            if tmp:
                for t in tmp:
                    q.put(t)
                it += k
        return it
                
            

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from heapq import heappush, heappop
        d = collections.defaultdict(int)
        for t in tasks:
            d[t] += 1
        q = []
        for t, cnt in d.iteritems():
            heappush(q, (-cnt, t))
        stage = 0
        while q:
            k = n+1
            tmp_list = []
            while k and q:
                cnt, t = heappop(q)
                cnt = -cnt
                
                if cnt > 1:
                    tmp_list.append((-(cnt-1), t))
                k -= 1
                stage += 1
            if tmp_list:
                for e in tmp_list:
                    heappush(q, e)        
                stage += k
                    
        return stage
        