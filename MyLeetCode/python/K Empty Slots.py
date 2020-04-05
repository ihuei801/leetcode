###
# Two Pointers, window
# (1) turn days to position into position to day
# (2) create a window with k flowers inside
# (3) check the k slots is not blooming
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        
            
        days = [0] * len(flowers)
        for day, pos in enumerate(flowers, 1):
            days[pos-1] = day
        l = 0
        r = l + k + 1
        pos = float('inf')
        while r < len(days):
            for i in xrange(l+1, r):
                if days[i] < days[l] or days[i] < days[r]:
                    l = i
                    r = i + k + 1
                    break               
            else:
                pos = min(pos, max(days[l], days[r]))
                l = r
                r = l + k + 1
        return -1 if pos == float('inf') else pos
        
                                        
                            
                    