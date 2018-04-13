###
# Time Complexity: O(m*n)
# Space Complexity: O(m+n)
###
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        re = [0] * (len(num1) + len(num2))
        
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                re[i+j] += int(n1) * int(n2)
                re[i+j+1] += re[i+j] / 10
                re[i+j] %= 10
        
        while re and re[-1] == 0:
            re.pop()
        return ''.join(map(str, re[::-1]))
        
  