###
# Queue
# Time Complexity: Preprocess: O(n)  hasNext:O(1) next:O(1)
# Space Complexity: O(n)
###
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.q = collections.deque()
        l = 0
        while l < len(compressedString):
            r = l + 1
            while r < len(compressedString) and compressedString[r].isnumeric():
                r += 1
            self.q.append([compressedString[l], int(compressedString[l+1:r])])
            l = r

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.q[0][1] -= 1
            c, num = self.q[0]
            if num == 0:
                self.q.popleft()
            return c
        return " "
            

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
                                        
                            
                    