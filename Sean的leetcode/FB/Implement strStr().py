###
# KMP
# Time Complexity: O(n)
# Space Complexity: O(m)
# Ref: http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
###
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        lps = self.kmp(needle)
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif j:
                j = lps[j-1]
            else:
                j = 0
                i += 1
        return -1
    def kmp(self, needle):
        lps = [0] * len(needle)
        j = 0
        i = 1
        while i < len(needle):
            if needle[j] == needle[i]:
                j += 1
                lps[i] = j
                i += 1
            elif j:
                j = lps[j-1]
            else:
                j = 0
                i += 1
        return lps       
###
# Time Complexity: O(n*m)
###
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        