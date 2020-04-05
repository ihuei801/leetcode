###
# stack
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""
        stack = []
        dir = path.split('/')
        for d in dir: 
            if d == '..':
                if stack:
                    stack.pop()
            elif d == '.' or d == "":
                pass
            else:
                stack.append(d)
        return '/' + '/'.join(stack)