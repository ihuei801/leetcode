#######################################################################
# Two Pointers and Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
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
        need = len(t)
        n = len(s) 
        l, r = 0, 0
        minlen = float('inf')
        minst = -1
        while r < n:
            d[s[r]] -= 1
            if d[s[r]] >= 0:
                need -= 1
            while need == 0:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    minst = l
                d[s[l]] += 1
                if d[s[l]] > 0:
                    need += 1
                l += 1
            r += 1
        return s[minst:minst+minlen] if minlen != float('inf') else ""
                    
                    