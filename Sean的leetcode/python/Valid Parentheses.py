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
        st = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            else:
                if not st or d[st.pop()] != c:
                    return False
        return not st 