###
# Stack 
# remove previous element if we can make the number smaller
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        re = [''] * (len(num))
        l = len(num) - k
        for c in num:
            while re and k and re[-1] > c:
                re.pop()
                k -= 1   
            re.append(c)
        re = ''.join(re)[:l].lstrip('0')
        return '0' if not re else re
        
        