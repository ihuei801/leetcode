###
# Sliding Window - memorize index
# Time Complexity: O(n)
# Space Complexity: O(k)
###
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = 0
        d = dict()
        maxlen = 0
        for r, e in enumerate(s):
            if e in d:
                l = max(l, d[e] + 1)
            d[e] = r
            maxlen = max(maxlen, r - l + 1)
        return maxlen
###
# Sliding Window - memorize counter
# Time Complexity: O(n)
# Space Complexity: O(k)
###
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = 0
        d = collections.Counter()
        maxlen = 0
        for r, e in enumerate(s):
            d[e] += 1
            while r - l + 1 > len(d):
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen

            


