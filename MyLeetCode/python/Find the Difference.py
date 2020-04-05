###
# Bit manipulation 
# xor : a ^ a = 0
# Time Complexity: O(m+n)
# Space Complexity: O(1)
###
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c = 0
        for e in s:
            c ^= ord(e)
        for e in t:
            c ^= ord(e)
        return chr(c)    
                    