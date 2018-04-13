###
# DFS
# Time Complexity: O(2^n)
# Space Complexity: O(n)
###
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        l_rm = r_rm = 0
        for c in s:
            if c == '(':
                l_rm += 1
            elif c == ')':
                if l_rm:
                    l_rm -= 1
                else:
                    r_rm += 1
        
        re = set()
        self.dfs(s, 0, 0, l_rm, r_rm, "", re)
        return list(re)
    
    def dfs(self, s, idx, pair, l_rm, r_rm, one_sol, re):
        if idx == len(s):
            if not pair and not l_rm and not r_rm:
                re.add(one_sol)
            return
        c = s[idx]
        if c == '(':
            self.dfs(s, idx + 1, pair + 1, l_rm, r_rm, one_sol + "(", re)
            if l_rm:
                self.dfs(s, idx + 1, pair, l_rm - 1, r_rm, one_sol, re)
        elif c == ')':
            if pair:
                self.dfs(s, idx + 1, pair - 1, l_rm, r_rm, one_sol + ")", re)
            if r_rm:
                self.dfs(s, idx + 1, pair, l_rm, r_rm - 1, one_sol, re)
        else:
            self.dfs(s, idx + 1, pair, l_rm, r_rm, one_sol + c, re)
            
            