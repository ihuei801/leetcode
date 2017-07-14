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
        if not wall or not wall[0]:
            return 0
        d = collections.defaultdict(int)
        max_cnt = 0
        for line in wall:
            b = 0
            for i in xrange(len(line)-1):            
                b += line[i]
                d[b] += 1
                max_cnt = max(max_cnt, d[b])
       
        return len(wall) - max_cnt