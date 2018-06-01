###
# String
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cntA = 0
        for i, c in enumerate(s):
            if c == 'A':
                cntA += 1
                if cntA > 1:
                    return False
            elif c == 'L' and i >= 2 and s[i-2] == 'L' and s[i-1] == 'L':
                return False
            
        return True
                                        
                            
                    