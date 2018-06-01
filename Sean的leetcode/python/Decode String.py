###
# Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        num = 0
        cur = ""
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stk.append((cur, num))
                num = 0
                cur = ""
            elif c == ']':
                pre, cnt = stk.pop()
                cur = pre + cur * cnt
                print pre, cnt, re
            else:
                cur += c         
        return cur
   
                
   
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = [["", 1]]
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stk.append(["", num])
                num = 0
            elif c == ']':
                cur, cnt = stk.pop()
                stk[-1][0] += cur * cnt
            else:
                stk[-1][0] += c
        return stk[0][0]
   
                            
                                        
                            
                    