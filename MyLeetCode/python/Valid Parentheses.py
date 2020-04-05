###
# Time Complexity: O(n)
# Space Complexity: O(n)
# Warning: check stack is empty in the end
###
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        d = {'(': ')', '{': '}', '[': ']'}
        stk = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stk.append(c)
            else:
                if not stk or d[stk.pop()] != c:
                    return False
        return not bool(stk) 