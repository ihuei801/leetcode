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
        n = len(citations)
        s = [0] * (n+1)
        for c in citations:
            if c >= n:
                s[n] += 1
            else:
                s[c] += 1
        accu = 0
        for i in xrange(n, -1, -1):
            accu += s[i]
            if accu >= i:
                return i