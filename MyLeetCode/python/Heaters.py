###
# Binary Search
# Time Complexity: O(nlogn) + O(mlogn) n: number heaters, m: number of houses
# Space Complexity: O(1)
###
cclass Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        rad = -float('inf')
        heaters.sort()
        for h in houses:
            idx = bisect.bisect(heaters, h)
            if idx == 0:
                min_dis = abs(h - heaters[0])
            elif idx == len(heaters):
                min_dis = abs(h - heaters[-1])
            else:
                min_dis = min(abs(h - heaters[idx-1]), abs(h - heaters[idx]))
            rad = max(min_dis, rad)
        return rad
                            
                    