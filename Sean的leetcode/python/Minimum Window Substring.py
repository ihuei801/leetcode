#######################################################################
# Sliding Window
# Time Complexity: O(t+s)
# Space Complexity: O(t)
# Use Distinct Chars to check match
#######################################################################
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        d = collections.Counter(t)
        l = 0
        match = 0
        minlen = float('inf')
        minl = None
        for r, rc in enumerate(s):
            if rc in d:
                d[rc] -= 1
                if d[rc] == 0:
                    match += 1
            while match == len(d): # Use distinct chars
                if r-l+1 < minlen:
                    minlen = r-l+1
                    minl = l
                lc = s[l]
                if lc in d:
                    if d[lc] == 0:
                        match -= 1
                    d[lc] += 1
                l += 1
        return s[minl:minl + minlen] if minlen != float('inf') else ''

#######################################################################
# Sliding Window
# Time Complexity: O(t+s)
# Space Complexity: O(t)
# Use All Chars to check match
#######################################################################
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        d = collections.Counter(t)
        l = 0
        match = 0
        minlen = float('inf')
        minl = None
        for r, rc in enumerate(s):
            if rc in d:
                d[rc] -= 1
                if d[rc] >= 0:
                    match += 1
            while match == len(t):
                if r-l+1 < minlen:
                    minlen = r-l+1
                    minl = l
                lc = s[l]
                if lc in d:
                    if d[lc] >= 0:
                        match -= 1
                    d[lc] += 1
                l += 1
        return s[minl:minl + minlen] if minlen != float('inf') else ''