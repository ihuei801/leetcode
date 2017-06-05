#######################################################################
# DFS
# Time Complexity: O(4^n)
# T(n) = 3 * T(n-1) + 3 * T(n-2) + 3 * T(n-3) + ... + 3 *T(1)
# T(n-1) = 3 * T(n-2) + 3 * T(n-3) + ... 3 * T(1)
# Thus T(n) = 4T(n-1) = 4^2 * T(n-2) = 4^n * T(1)
# Space Complexity: O(4^n)
#######################################################################
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.target = target
        res = []
        self.dfs(num, 0, "", 0, 0, res);
        return res
    def dfs(self, num, cur, one_sol, cur_sum, cur_mult, res):
        if cur == len(num):
            if cur_sum == self.target:
                res.append(one_sol)
                return
        for i in xrange(cur, len(num)):
            if i != cur and num[cur] == '0':
                break
            tmp = num[cur:i+1]
            val = int(tmp)
            if cur == 0:
                self.dfs(num, i + 1, one_sol + tmp, val, val, res)
            else:
                self.dfs(num, i + 1, one_sol + "+" + tmp, cur_sum + val, val, res)
                self.dfs(num, i + 1, one_sol + "-" + tmp, cur_sum - val, -val, res)
                self.dfs(num, i + 1, one_sol + "*" + tmp, cur_sum - cur_mult + cur_mult * val, cur_mult * val, res)
                
                
                
        