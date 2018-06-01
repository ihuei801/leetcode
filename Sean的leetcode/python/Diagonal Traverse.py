###
# Design Deque
# Time Complexity: hasNext:  O(1) next O(1)
# Space Complexity: O(n)
###
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        import itertools
        self.it = (v[i] for i in itertools.count() for v in (v1, v2) if i < len(v))
        self.l = len(v1) + len(v2)

    def next(self):
        """
        :rtype: int
        """
        self.l -= 1
        return next(self.it)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.l > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        from collections import deque
        self.q = deque([(len(v), iter(v)) for v in (v1, v2) if v])
        

    def next(self):
        """
        :rtype: int
        """
        l, it = self.q.popleft()
        if l-1 > 0:
            self.q.append((l-1, it))
        return next(it)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q) 

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
                                        
                            
                    