###
# Sliding Window
# Time Complexity: O(n) 
# Space Complexity: O(1)
###
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        maxlen = 0
        l = 0
        d = collections.OrderedDict()
        for r, e in enumerate(s):
            if e in d:
                del d[e]
            d[e] = r
            if len(d) > 2:
                _, idx = d.popitem(last=False)
                l = max(l, idx + 1)
            maxlen = max(maxlen, r - l + 1)
        return maxlen
###
# Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        maxlen = 0
        l = 0
        d = collections.Counter()
        for r, e in enumerate(s):
            d[e] += 1
            while len(d) > 2:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen
                          
                            
                    