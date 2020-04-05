#######################################################################
# Back Tracking
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
        if not num:
            return []
        re = []
        self.dfs(num, 0, 0, 0, target, "", re)
        return re
    def dfs(self, num, idx, cur_sum, cur_mult, target, one_sol, re):
        if idx == len(num):
            if cur_sum == target:
                re.append(one_sol)
            return
        for i in xrange(idx, len(num)):
            if i != idx and num[idx] == '0':
                break
            val_str = num[idx:i+1]
            val = int(val_str)
            if idx == 0:
                self.dfs(num, i + 1, val, val, target, one_sol + val_str, re)
            else:
                self.dfs(num, i + 1, cur_sum + val, val, target, one_sol + "+" + val_str, re)
                self.dfs(num, i + 1, cur_sum - val, -val, target, one_sol + "-" + val_str, re)
                self.dfs(num, i + 1, cur_sum - cur_mult + cur_mult * val, cur_mult * val, target, one_sol + "*" + val_str, re)
        

                
        