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

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        if not intervals:
            return 0
        pq = []
        for it in intervals:
            heapq.heappush(pq, (it.start, 's'))
            heapq.heappush(pq, (it.end, 'e'))
        
        cnt = 0
        maxcnt = 0
        while pq:
            time, flag = heapq.heappop(pq)
            if flag == 's':
                cnt += 1
            else:
                cnt -= 1
            maxcnt = max(maxcnt, cnt)
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