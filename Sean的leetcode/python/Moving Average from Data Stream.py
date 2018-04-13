###
# Queue/Deque
# Time Complexity: O(1) 
# Space Complexity: O(size)
###
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        from collections import deque
        self.nums = deque()
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        # move left end
        if len(self.nums) == self.size:
            self.sum -= self.nums.popleft()
        # insert element
        self.nums.append(val)
        self.sum += val
        return float(self.sum) / len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
        
        