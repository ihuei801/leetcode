###
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'{': '}', '[': ']', '(':')'}
        stack = []
        for e in s:
            if e == '}' or e == ']' or e == ')':
                if not stack or d[stack.pop()] != e:
                    return False
            else:
                stack.append(e)
        return not stack