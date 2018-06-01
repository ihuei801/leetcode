###
# Two Pointers
# Time Complexity: O(n) 
# Space Complexity: O(1)
###
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 2:
            return len(s)
        maxlen = 0
        n = len(s)
        d = collections.Counter()
        l, r = 0, 0
        while r < n:
            d[s[r]] += 1
            while len(d) > 2:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    d.pop(s[l])
                l += 1
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen
            
                          
                            
                    