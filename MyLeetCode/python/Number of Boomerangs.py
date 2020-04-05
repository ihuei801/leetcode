###
# Hash Table
# Time Complexity: O(n^2) 
# Space Complexity: O(n)
###
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        if len(points) <= 2:
            return 0
        num = 0
        for i, p1 in enumerate(points):
            d = defaultdict(int)
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                dis = self.distance(p1, p2)
                d[dis] += 1
            for k, v in d.iteritems():
                num += v * (v-1)
        return num
    
    def distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (x1-x2)**2 + (y1-y2)**2
        
        