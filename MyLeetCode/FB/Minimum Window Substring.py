#######################################################################
# Two Pointers and Hash Table
# Time Complexity: O(n)
# Space Complexity: O(1)
#
#######################################################################

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = collections.Counter(t)
        missing = len(t)
        l = r = L = 0
        min_len = float('inf')
        while r < len(s):
            d[s[r]] -= 1
            if d[s[r]] >= 0:
                missing -= 1
            while not missing:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    L = l
                d[s[l]] += 1
                if d[s[l]] > 0:
                    missing += 1
                l += 1
            r += 1
        return "" if min_len == float('inf') else s[L:L+min_len]
                    
                    