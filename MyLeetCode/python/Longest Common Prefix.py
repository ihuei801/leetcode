###
# Vertical Scan
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        end = 0
        for i in xrange(len(strs[0])):
            for j in xrange(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
            
        return strs[0]
                                        
                            
                    