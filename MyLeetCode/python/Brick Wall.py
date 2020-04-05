###
# Time Complexity: O(n*m)
# Space Complexity:O(l)
###
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not wall or not wall[0]:
            return 0
        d = collections.defaultdict(int)
        max_cnt = 0
        for w in wall:
            accu = 0
            for i in xrange(len(w)-1):
                accu += w[i]
                d[accu] += 1
                max_cnt = max(max_cnt, d[accu])
        return len(wall) - max_cnt
        