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
        if not words:
            return 0
        d = collections.defaultdict(int)
        maxlen = 0
        for word in words:
            key = 0
            for c in word:
                key |= 1 << (ord(c) - ord('a'))
            for k, l in d.iteritems():
                if key & k == 0:
                    maxlen = max(maxlen, l * len(word))
            d[key] = max(d[key], len(word))
        return maxlen
            
               
                    