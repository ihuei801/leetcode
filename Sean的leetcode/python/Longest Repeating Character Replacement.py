###
# Moving Window
# Time Complexity: O(n)
# Space Complexity: O(1) -> 26 lower case chars
###
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        l = 0
        d = collections.Counter()
        maxlen = 0
        maxcnt = 0
        for r, c in enumerate(s):
            d[c] += 1
            maxcnt = max(maxcnt, d[c])
            while r - l + 1 - maxcnt > k:
                d[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen


