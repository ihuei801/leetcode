###
# Time Complexity: O(n)
# Space Complexity: O(1)
###

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pre = None
        cur_sum = 0
        for c in s:
            num = d[c]
            if pre and pre < num:
                cur_sum -= 2 * pre
            cur_sum += num
            pre = num
        return cur_sum