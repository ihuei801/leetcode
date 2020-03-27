###
# Sliding Window
# Time Complexity: O(l1 + (l2-l1))
# Space Complexity: O(l1) = O(1) only lower case - 26
###
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        if not s1:
            return False
        d = collections.Counter()
        for c in s1:
            d[c] += 1
        l = 0
        match = 0
        for r, rc in enumerate(s2):
            if rc in d:
                d[rc] -= 1
                if d[rc] == 0:
                    match += 1
            if match == len(d):
                return True
            # if current window size hit the limit, shrink window
            if r - l + 1 >= len(s1):
                lc = s2[l]
                if lc in d:
                    if d[lc] == 0:
                        match -= 1
                    d[lc] += 1
                l += 1
        return False

                