###
# String
# Time Complexity: O(n)
# Space Complexity: O(n^2)
###
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 1:
            return []
        re = []
        for i in xrange(len(s) - 1):
            if s[i] == "+" and s[i+1] == "+":
                re.append(s[:i] + "--" + s[i+2:])       
        return re
        
        