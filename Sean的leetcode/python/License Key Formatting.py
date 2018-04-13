###
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not S:
            return ""
        S = S.replace("-", "").upper()[::-1]
        re = []
        for i in xrange(0, len(S), K):
            re.append(S[i:i+K])
        return "-".join(re)[::-1]
        
        