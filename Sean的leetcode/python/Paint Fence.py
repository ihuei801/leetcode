###
# DP
# Time Complexity: O(n)
# Space Complexity: O(1)
# State:
# Same[i]: number of ways if the last two have same color
# Diff[i]: number of ways if the last two have diff colors
# Function:
# Same[i] = Diff[i]
# Diff[i] = (Same[i-1] + Diff[i-1]) * (k-1)
# Initialization:
# Same[2] = k
# Diff[2] = k * (k-1)
# Answer: Same[n] + Diff[n]
###
cclass Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        diff = k * (k-1)
        same = k
        for i in xrange(3, n+1):     
            same, diff = diff, (same + diff) * (k-1)     
        return same + diff
        