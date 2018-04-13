###
# Back Tracking
# Time Complexity: O(n!) T(n) = (n-1) * T(n-2) = (n-1) * (n-3) * T(n-4) = ... = O(n!) build a trie/hash table  + O(n^l) (use pruning, hard to analyze)
###
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = dict()
        return self.bt(s, d)
    
    def bt(self, s, d):
        if len(s) <= 1:
            return False
        if s in d:
            return d[s]
        for i in xrange(len(s) - 1):
            if s[i] == '+' and s[i+1] == '+':
                tmp = s[:i] + "--" + s[i+2:]
                if not self.bt(tmp, d):
                    d[tmp] = False
                    d[s] = True
                    return True
        d[s] = False
        return False
        
        