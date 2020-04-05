###
# DP
# video: Maximum Sum Rectangular Submatrix in Matrix dynamic programming/2D kadane 
#        https://www.youtube.com/watch?v=yCQN096CwWM
# bisect_left(x) return idx: left side < x right side >= x
# Time Complexity: O(m^2nlogn) 
# Space Complexity: O(n)
###
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        res = -float('inf')
        for l in xrange(cols):
            row_sum = [0] * rows
            for r in xrange(l, cols):
                for i in xrange(rows):
                    row_sum[i] += matrix[i][r]
                accu_sum = 0
                accu_sums = [0]
                for i in xrange(rows):
                    accu_sum += row_sum[i]
                    loc = bisect.bisect_left(accu_sums, accu_sum - k)
                    if loc != len(accu_sums):
                        res = max(res, accu_sum - accu_sums[loc])
                    bisect.insort(accu_sums, accu_sum)
        return res