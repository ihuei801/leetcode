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
        l_rm = r_rm = 0
        for c in s:
            if c == '(' :
                l_rm += 1
            elif c == ')':
                if l_rm:
                    l_rm -= 1
                else:
                    r_rm += 1
        re = set()
        self.dfs(s, 0, l_rm, r_rm, 0, "", re)
        return list(re)
    def dfs(self, s, idx, l_rm, r_rm, pair, one_sol, re):
        if idx == len(s):
            if not l_rm and not r_rm and not pair:
                re.add(one_sol)
            return
        if s[idx] == '(':
            if l_rm:
                self.dfs(s, idx + 1, l_rm - 1, r_rm, pair, one_sol, re)
            self.dfs(s, idx + 1, l_rm, r_rm, pair + 1, one_sol + s[idx], re)
        elif s[idx] == ')':
            if r_rm:
                self.dfs(s, idx + 1, l_rm, r_rm - 1, pair, one_sol, re)
            if pair:
                self.dfs(s, idx + 1, l_rm, r_rm, pair - 1, one_sol + s[idx], re)
        else:
            self.dfs(s, idx + 1, l_rm, r_rm, pair, one_sol + s[idx], re)