###
# Stack
# Push: O(1)
# Pop: O(1)
# Top: O(1)
# getMin: O(1)
# Space: O(n)
###

#class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_st = []
        self.st = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.st.append(x)
        if not self.min_st or x <= self.min_st[-1]:
            self.min_st.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.st:
            return
        if self.st[-1] == self.min_st[-1]:
            self.min_st.pop()
        self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.st:
            return self.st[-1]
        else:
            return -1

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_st:
            return self.min_st[-1]
        else:
            return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()                
                            
                    