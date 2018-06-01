###
# Array 2D
# Time Complexity: O(m*n)
# Space Complexity: O(1)
###
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        for i, row in enumerate(board):
            for j, e in enumerate(row):
                cnt = self.count(board, i, j)
                if cnt == 3 or (cnt == 2 and e == 1):
                    board[i][j] |= 2
                    
        for i, row in enumerate(board):
            for j, e in enumerate(row):
                board[i][j] >>= 1
                
    def count(self, board, i, j):
        row = len(board)
        col = len(board[0])
        cnt = 0
        for r in xrange(i-1, i+2):
            for c in xrange(j-1, j+2):
                if r < 0 or r >= row or c < 0 or c >= col or (r == i and c == j):
                    continue
                cnt += board[r][c] & 1
        return cnt
                
#Follow up: infinite board
#Time Complexity: O(m*n)
#Space Complexity: O(m*n)                               
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        from collections import Counter
        live = {(i, j) for i, row in enumerate(board) for j, c in enumerate(row) if c}
        t = Counter((nbi, nbj) for i, j in live for nbi in xrange(i-1, i+2) for nbj in xrange(j-1, j+2) if nbi != i or nbj != j) 
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                board[i][j] = int(t[(i, j)] == 3 or (t[(i, j)] == 2 and (i, j) in live))
                
                                
                    