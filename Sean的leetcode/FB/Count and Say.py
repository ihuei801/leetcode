###
# Time Complexity: O(2^n)  len grows up to double 
# Space Complexity: O(2^n)
###
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        s = "1"
        for i in xrange(1, n):
            cnt = 1
            tmp = ""
            for j in xrange(1, len(s)):
                if s[j] != s[j-1]:
                    tmp += str(cnt) + s[j-1]
                    cnt = 1
                else:
                    cnt += 1
            tmp += str(cnt) + s[-1]
            s = tmp
        return s