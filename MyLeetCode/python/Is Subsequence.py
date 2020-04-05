###
# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        m = len(s)
        n = len(t)
        i = 0
        for j, c in enumerate(t):
            if c == s[i]:
                i += 1
                if i == m:
                    return True
        return False
                                        
                            
                    