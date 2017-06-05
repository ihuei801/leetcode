##
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
###

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from heapq import heappush, heappop
        i = 0
        q = []
        re = []
        while i < len(buildings) or q:
            if i < len(buildings):
                x = buildings[i][0]
            #non-overlapped with the current top
            if i == len(buildings) or (q and x > q[0][1]):
                x = q[0][1]
                while q and q[0][1] <= x:
                    heappop(q)
                h = -q[0][0] if q else 0
            #overlapped with the current top
            else:
                while i < len(buildings) and buildings[i][0] == x:
                    heappush(q, (-buildings[i][2], buildings[i][1]))
                    i += 1
                h = -q[0][0]
            if not re or re[-1][1] != h:
                re.append([x, h])
        return re