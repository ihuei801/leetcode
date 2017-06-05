###
# DP
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return self.check(s[0])
        fn_1 = self.check(s[0])
        fn_2 = 1
        fn = 0
        for i in xrange(1, len(s)):
            fn = 0
            if self.check(s[i]):
                fn += fn_1
            if self.check(s[i-1:i+1]):
                fn += fn_2
            if not fn:
                break
            fn_2 = fn_1
            fn_1 = fn
        return fn
        
    def check(self, s):
        if len(s) == 1:
            return 1 if s != "0" else 0
        else:
            return 1 if s[0] != '0' and int(s) >= 1 and int(s) <= 26 else 0
            