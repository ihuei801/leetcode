###
# Hash Table
# Time Complexity: O(n^2)
# Space Complexity: O(n)
###
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        if not words:
            return 0
        d = defaultdict(int)
        max_len = 0
        for word in words:
            key = 0
            for c in word:
                key |= 1 << (ord(c) - ord('a'))
            d[key] = max(d[key], len(word))
            for k, v in d.iteritems():
                if k & key == 0:
                    max_len = max(max_len, d[key] * v)
        return max_len
               
                    