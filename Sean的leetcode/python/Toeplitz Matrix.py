###
# Array 2D
# Time Complexity: O(mn)
# Space Complexity: O(1)
###
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(i == 0 or j == 0 or matrix[i-1][j-1] == c for i, row in enumerate(matrix) for j, c in enumerate(row))
        
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if i >= 1 and j >= 1:
                    if c != matrix[i-1][j-1]:
                        return False
        return True
                                        
                            
                    