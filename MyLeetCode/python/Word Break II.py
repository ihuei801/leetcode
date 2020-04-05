###
# Back Tracking
# Time Complexity
###     
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s or not wordDict:
            return []
        t = dict()
        return self.bt(s, wordDict, t)
    def bt(self, s, wordDict, t):
        if s in t:
            return t[s]
        if not s:
            return []
        re = []
        for i in xrange(len(s)):
            prefix = s[:i]
            subfix = s[i:]
            if i == 0:
                if subfix in wordDict:
                    re.append(subfix)
            else:
                if prefix in wordDict:
                    for w in self.bt(subfix, wordDict, t):
                        re.append(prefix + " " + w)
        t[s] = re
        return re    