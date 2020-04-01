###
# Sliding Window
# Time Complexity: O(p + s-p)
# Space Complexity: O(p)
# Use Distinct Chars to check match
###
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        d = collections.Counter(p)
        match = 0
        l = 0
        result = []
        for r, rc in enumerate(s):
            if rc in d:
                d[rc] -= 1
                if d[rc] == 0:
                    match += 1
            if match == len(d): # Check distinct chars
                result.append(l)
            if r - l + 1 >= len(p):
                lc = s[l]
                if lc in d:
                    if d[lc] == 0:
                        match -= 1
                    d[lc] += 1
                l += 1
        return result

###
# Sliding Window
# Time Complexity: O(p + s-p)
# Space Complexity: O(p)
# Use All Chars to check match
###
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        d = collections.Counter(p)
        match = 0
        l = 0
        result = []
        for r, rc in enumerate(s):
            if rc in d:
                d[rc] -= 1
                if d[rc] >= 0:
                    match += 1
            if match == len(p):  # Check all chars
                result.append(l)
            if r - l + 1 >= len(p):
                lc = s[l]
                if lc in d:
                    if d[lc] >= 0:
                        match -= 1
                    d[lc] += 1
                l += 1
        return result


                