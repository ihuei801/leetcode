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
        need = collections.Counter(t)
        missing = len(t)
        i = j = I = 0
        min_len = float('inf')
        while j < len(s):
            need[s[j]] -= 1
            if need[s[j]] >= 0:
                missing -= 1
            while not missing:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    I = i
                need[s[i]] += 1
                if need[s[i]] > 0:
                    missing += 1
                i += 1
            j += 1
                
        return s[I:I+min_len] if min_len != float('inf') else ""
                    
                    