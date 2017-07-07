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
        n = len(citations)
        table = [0] * (n + 1)
        for num in citations:
            if num > n:
                table[n] += 1
            else:
                table[num] += 1
        acc = 0
        for i in xrange(n, -1, -1):
            acc += table[i]
            if acc >= i:
                return i
        return 0
        