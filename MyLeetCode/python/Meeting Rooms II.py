###
# PriorityQueue
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
###
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Event:
    def __init__(self, time, flag):
        self.time = time
        self.flag = flag
    def __lt__(self, other):
        if self.time != other.time:
            return self.time < other.time
        else:
            return self.flag == 'e'
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        if not intervals:
            return 0
        pq = []
        for it in intervals:
            heapq.heappush(pq, Event(it[0], 's'))
            heapq.heappush(pq, Event(it[1], 'e'))
        maxcnt = 0
        cnt = 0
        while pq:
            event = heapq.heappop(pq)
            if event.flag == 's':
                cnt += 1
            else:
                cnt -= 1
            maxcnt = max(cnt, maxcnt)
        return maxcnt
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        from Queue import PriorityQueue
        if not intervals:
            return 0
        pq = PriorityQueue()
        for it in intervals:
            pq.put((it.start, 's'))
            pq.put((it.end, 'e'))
        
        cnt = 0
        max_cnt = 0
        while not pq.empty():
            v, flag = pq.get()
            if flag == 's':
                cnt += 1
            else:
                cnt -= 1
            max_cnt = max(max_cnt, cnt)
        return max_cnt



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        from heapq import heappop, heappush
        q = []
        n = 0
        for interval in sorted(intervals, key=lambda x: (x.start, x.end)):
            while q and interval.start >= q[0]:
                heappop(q)
            
            heappush(q, interval.end)
            n = max(n, len(q))
        return n