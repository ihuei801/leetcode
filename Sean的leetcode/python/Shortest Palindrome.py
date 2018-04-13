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
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        r = s[::-1]
        l = self.lps(s + "#" + r)
        return r[:len(r) - l[-1]] + s
    
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
        
        