###
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        re = ""
        c = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or c:
            if i >= 0:
                c += int(a[i]) 
                i -= 1
            if j >= 0:
                c += int(b[j]) 
                j -= 1
            re = str(c % 2) + re
            c /= 2
        return re
        