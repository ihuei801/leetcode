###
# DFS
# Time Complexity: O(m^n) m:average unique letters of each digit, n: len of input string
# Space Complexity: O(n*m) space needed for recursive call (the number of branch is fixed)
###
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, "", res)
        return res
    def dfs(self, digits, idx, one_sol, res):
        table = 'N N abc def ghi jkl mno pqrs tuv wxyz'.split()
        if idx == len(digits):
            res.append(one_sol)
            return
        for e in table[int(digits[idx])]:
            self.dfs(digits, idx + 1, one_sol + e, res)
        
        
        