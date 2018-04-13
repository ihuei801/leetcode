###
# DFS
# Time Complexity: O(m^n) m:average unique letters of each digit, n: len of input string
# Space Complexity: O(n) space needed for recursive call (the number of branch is fixed)
###
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        t = ["", "", "abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits:
            return []
        re = []
        self.dfs(digits, 0, "", re, t)
        return re
    def dfs(self, digits, i, one_sol, re, t):
        if i == len(digits):
            re.append(one_sol)
            return
        for c in t[int(digits[i])]:
            self.dfs(digits, i+1, one_sol + c, re, t)
        
    

        
        
        