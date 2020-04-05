###
# Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        i = 0
        st = []
        sign = 1
        while i < len(s):
            if s[i].isnumeric():
                l = i
                while i < len(s) and s[i].isnumeric():
                    i += 1
                num = int(s[l:i])
                cur += sign * num
                i -= 1
            elif s[i] == '+' or s[i] == '-':
                sign = 1 if s[i] == '+' else -1         
            elif s[i] == '(':
                st.append(cur)
                st.append(sign)
                cur = 0
                sign = 1
            elif s[i] == ')':
                cur = st.pop() * cur + st.pop()
            i += 1
        return cur
            
        
                                        
                            
                    