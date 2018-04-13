###
# Heap
# addNum: O(logn)
# findMedian: O(1)
# Space: O(n)
###
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        from Queue import PriorityQueue
        self.st = PriorityQueue()
        self.bt =  PriorityQueue()
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.st.put(-num)
        self.bt.put(-self.st.get())
        if self.bt.qsize() > self.st.qsize():
            self.st.put(-self.bt.get())
        

    def findMedian(self):
        """
        :rtype: float
        """
        if self.st.qsize() > self.bt.qsize():
            return -self.st.queue[0]
        else:
            return (-self.st.queue[0] + self.bt.queue[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        
        