###
# Back Tracking
# Time Complexity: 
# T(n) = 2T(n-1) = 4T(n-2) = 2^(n-1)T(1)
# O(2^2n) n:row m:col k:len of word
# Space Complexity: O(n)(recursive) O(2^2n) (solution)
###
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        re = []
        self.backtrack(n, 0, "", re)
        return re
    def backtrack(self, left, right, one_sol, re):
        if not left and not right:
            re.append(one_sol)
            return
        if left:
            self.backtrack(left - 1, right + 1, one_sol + "(", re)
        if right:
            self.backtrack(left, right - 1, one_sol + ")", re)
        
        