###
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        ln = len(citations)
        d = [0] * (ln + 1)
        for c in citations:
            if c >= ln:
                d[ln] += 1
            else:
                d[c] += 1
        accu = 0
        for i in xrange(ln, -1, -1):
            accu += d[i]
            if accu >= i:
                return i
        return 0