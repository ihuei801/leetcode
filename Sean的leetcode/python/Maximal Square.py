###
# DP
# Time Complexity: O(m*n)
# Space Complexity: O(n)
# P[i][j]:the maximal size of the square that can be achieved at point (i, j)
# i == 0 or j == 0: P[i][j] = matrix[i][j]
# i > 0 and j > 0: if matrix[i][j] = 0 -> P[i][j] = 0
#                 if matrix[i][j] = 1 -> P[i][j] = min(P[i-1][j], P[i][j-1], P[i-1][j-1]) + 1 (three neighbors must be 1)
###    
### Solution 1
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        dp = [0] * len(matrix[0])
        max_side = 0
        for i in xrange(len(matrix)):
            new_dp = [0] * len(matrix[0])
            for j in xrange(len(matrix[0])):
                if j == 0:
                    new_dp[j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        new_dp[j] = min(dp[j-1], dp[j], new_dp[j-1]) + 1
                max_side = max(max_side, new_dp[j])
            dp = new_dp
        return max_side*max_side
                        
### Solution 2
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        max_size = 0
        left = 0
        dp = [0] * len(matrix[0])
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if i == 0 or j == 0:
                    curr = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        curr = min(left, dp[j-1], dp[j]) + 1
                    else:
                        curr = 0
                max_size = max(max_size, curr)
                if j > 0:
                    dp[j-1] = left
                if j == len(matrix[0])-1:
                    dp[j] = curr
                left = curr
        return max_size * max_size