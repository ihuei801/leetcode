###
# DP
# The DP solution proceeds row by row, starting from the first row. 
# Let the maximal rectangle area at row i and column j be computed by [right(i,j) - left(i,j)]*height(i,j).
# All the 3 variables left, right, and height can be determined by the information from previous row, and also information from the current row. 
# So it can be regarded as a DP solution. The transition equations are:
# left(i,j) = max(left(i-1,j), cur_left), cur_left can be determined from the current row
# right(i,j) = min(right(i-1,j), cur_right), cur_right can be determined from the current row
# height(i,j) = height(i-1,j) + 1, if matrix[i][j]=='1';
# height(i,j) = 0, if matrix[i][j]=='0'
# Time Complexity: O(row*col)
# Space Complexity: O(col)
###
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        left = [0] * col
        right = [col] * col
        height = [0] * col
        max_area = 0
        for i in xrange(row):
            cur_left = 0
            cur_right = col
            for j in xrange(col):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                    height[j] += 1
                else:
                    left[j] = 0
                    cur_left = j+1
                    height[j] = 0
            for j in xrange(col-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = col
                    cur_right = j
                max_area = max(max_area, (right[j] - left[j]) * height[j])
           
            
        return max_area
                    
                