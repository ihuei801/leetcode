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
        if not digits:
            return []
        re = []
        self.dfs(digits, 0, "", re)
        return re
    
    def dfs(self, digits, idx, one_sol,  re):
        d = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if idx == len(digits):
            re.append(one_sol)
            return
        for c in d[int(digits[idx])]:
            self.dfs(digits, idx + 1, one_sol + c, re)

        
        
        