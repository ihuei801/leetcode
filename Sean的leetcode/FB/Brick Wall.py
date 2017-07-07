###
# Time Complexity: O(n)
# Space Complexity:O(l)
###

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        boundary = collections.defaultdict(int)
        max_cnt = 0
        for w in wall:
            l = 0
            for i in xrange(len(w)-1):
                l += w[i]
                boundary[l] += 1
                max_cnt = max(max_cnt, boundary[l])
        return len(wall) - max_cnt
        