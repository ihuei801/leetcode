###
# Time Complexity: O(rowA * colA * colB)
# Space Complexity: O(rowA * colB)
###
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        cols = len(B[0])
        l = len(B)
        C = [[0 for _ in xrange(cols)] for _ in xrange(rows)]
        for i in xrange(rows):
            for k in xrange(l):
                if A[i][k]:
                    for j in xrange(cols):
                        if B[k][j]:
                            C[i][j] += A[i][k] * B[k][j]
        return C