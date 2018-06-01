###
# Design Array
# Time Complexity: hasNext:  O(1) next O(1)
# Space Complexity: O(1)
###
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
                                        
                            
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.r = 0
        self.c = 0
        self.l = vec2d

    def next(self):
        """
        :rtype: int
        """
        re = self.l[self.r][self.c]
        self.c += 1
        return re

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.r < len(self.l):
            if self.c < len(self.l[self.r]):
                return True
            self.r += 1
            self.c = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())   
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        from collections import deque
        whole = [e for v in vec2d for e in v]
        
        self.it = iter(whole)
        self.len = len(whole)

    def next(self):
        """
        :rtype: int
        """
        self.len -= 1
        
        return next(self.it)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.len != 0

     