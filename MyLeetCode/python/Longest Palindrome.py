###
# Hash Table
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        odd = sum(v & 1 for v in Counter(s).values())
        return len(s) - odd + bool(odd)
        
        
        