###
# String
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        re = []
        while i >= 0 or j >= 0 or carry:
            tmp = 0
            if i >= 0:
                tmp += int(num1[i])
                i -= 1
            if j >= 0:
                tmp += int(num2[j])
                j -= 1
            tmp += carry
            re.append(str(tmp % 10))
            carry = tmp / 10
        return ''.join(re[::-1])
        