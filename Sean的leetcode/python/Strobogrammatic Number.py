###
# Two pointers
# Time Complexity: O(n) 
# Space Complexity: O(1)
###
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return False
        d = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in d or d[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True
        
        