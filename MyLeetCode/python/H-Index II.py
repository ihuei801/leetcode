###
# Binary Search
# Time Complexity: O(logn) 
# Space Complexity: O(1)
###

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        l, r = 0, len(citations) - 1
        while l+1 < r:
            mid = (l + r)/2
            r_num = len(citations) - mid 
            if citations[mid] >= r_num:
                r = mid
            else:
                l = mid
        if citations[l] >= len(citations) - l:
            return len(citations) - l
        elif citations[r] >= len(citations) - r:
            return len(citations) - r
        else:
            return 0