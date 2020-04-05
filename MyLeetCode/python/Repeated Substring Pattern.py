###
# KMP
# preprocessing of KMP to find longest proper prefix and suffix
# https://leetcode.com/problems/shortest-palindrome/solution/
# video: https://www.youtube.com/watch?v=GTJr8OvyEVQ
# http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = self.lps(s)
        return l[-1] != 0 and len(s) % (len(s) - l[-1]) == 0 #substring is the one minus longest prefix and subfix
    
    def lps(self, s):
        lps = [0] * len(s)
        idx = 0
        for i in xrange(1, len(s)):
            while idx > 0 and s[idx] != s[i]:
                idx = lps[idx-1]
            if s[i] == s[idx]:
                idx += 1
            lps[i] = idx
        return lps
# s = substr * n n >= 2
# 2s[1:-1] = substr * (2n-2) >= substr * 2    
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s*2)[1:-1]