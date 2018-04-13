###
# DP
# Time Complexity: O(1)
# Space Complexity: O(1)
# State:
# dp[i] number or unique element with len i
# Function
# dp[i] = dp[1] * 9 * 8 * ....
# Initialization:
# dp[1] = 10
# Answer:
# dp[1] + dp[2] + ... + dp[n]
###
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            return 0
        if n == 0:
            return 1
        k = 9
        unique = 9
        num = 10
        for i in xrange(2, n+1):
            unique *= k
            k -= 1
            num += unique
        return num