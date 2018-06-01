###
# Design, Bucket
# hit: O(1)
# getHit: O(1)
# The solution is easy to scale if number os hits per second is large
###
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.q = [(0, 0)] * 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        k = timestamp % 300
        time, cnt = self.q[k]
        if timestamp == time:
            self.q[k] = (timestamp, cnt + 1)
        else:
            self.q[k] = (timestamp, 1)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        cnt = 0
        for time, hit in self.q:
            if timestamp - time < 300:
                cnt += hit           
        return cnt


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
        
        