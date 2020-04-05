###
# One edit distance:
# 1) Insert/Delete (insert to short one or delete from long one)
# 2) Substitute
# Time Complexity: O(n)
# Space Complexity: O(1)
###

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1 or s == t:
            return False
        for i in xrange(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        return True