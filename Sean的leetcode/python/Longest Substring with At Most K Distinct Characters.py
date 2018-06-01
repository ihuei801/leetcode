###
# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(k)
###
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) <= k:
            return len(s)
        n = len(s)
        l, r = 0, 0
        d = collections.Counter()
        maxlen = 0
        while r < n:
            d[s[r]] += 1
            while len(d) > k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])
                l += 1
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen
        
        