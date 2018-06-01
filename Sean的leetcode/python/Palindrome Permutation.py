###
# Hash Table
# Time Complexity: O(n) 
# Space Complexity: O(1)
###
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        if not s:
            return False
        odd = sum(n & 1 for n in Counter(s).values())
        return odd <= 1
        
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import defaultdict
        if not s:
            return False
        d = defaultdict(int)
        odd = 0
        for c in s:
            d[c] += 1
            if d[c] & 1:
                odd += 1
            else:
                odd -= 1
        return odd <= 1
        
        