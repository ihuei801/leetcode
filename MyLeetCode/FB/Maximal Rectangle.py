###
# DP
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
                    
                