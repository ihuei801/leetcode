###
# Binary Search
# search the max distance of two adjacent gas station between 0 and maxdis
# Time Complexity: O(nlogd)
# Space Complexity: O(1)
###
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        l = 0
        r = stations[-1] - stations[0]
        while r - l > 1e-6:
            mid = (l + r) / 2.0
            cnt = 0
            for a, b in zip(stations, stations[1:]):
                cnt += math.ceil((b-a)/mid) - 1
            if cnt > K:
                l = mid
            else:
                r = mid
        return r
                                        
                            
                    