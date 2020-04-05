###
# Array
# Two conditions to help solve this problem:
# (1) In a valid chess board, there are 2 and only 2 kinds of rows and one is inverse to the other.
#     For example if there is a row 01010011 in the board, any other row must be either 01010011 or 10101100.
#     The same for columns
#     A corollary is that, any rectangle inside the board with corners 
#     top left, top right, bottom left, bottom right must be 4 zeros or 2 ones 2 zeros or 4 zeros.
# (2) Every row and column has half ones. Assume the board is N * N:
#     If N = 2*K, every row and every column has K ones and K zeros.
#     If N = 2*K + 1, every row and every column has K ones and K + 1 zeros or K + 1 ones and K zeros.
# Since the swap process does not break this property, for a given board to be valid, this property must hold.
# These two conditions are necessary and sufficient condition for a valid chessboard.
# Once we know it is a valid cheese board, we start to count swaps.
# Basic on the property above, when we arange the first row, we are actually moving all columns.
# I try to arrange one row into 01010 and 10101 and I count the number of swaps.
# In case of N even, I take the minimum swaps, because both are possible.
# In case of N odd, I take the even swaps.
# Because when we make a swap, we move 2 columns or 2 rows at the same time.
# So col swaps and row swaps should be even here
# Time Complexity: O(n*m)
# Space Complexity: O(1)
###
class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        for i in xrange(N):
            for j in xrange(N):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] != 0:
                    return -1
        rowcnt, colcnt = 0, 0 #count number of 1
        rowswap, colswap = 0, 0 #count the row/col that is in 0,1,0,1 order
        for i in xrange(N):
            rowcnt += board[0][i]
            colcnt += board[i][0]
            rowswap += board[0][i] == i & 1
            colswap += board[i][0] == i & 1
        if rowcnt > math.ceil(N/2.0) or colcnt > math.ceil(N/2.0):
            return -1
        if N & 1:
            if rowswap & 1:
                rowswap = N - rowswap
            if colswap & 1:
                colswap = N - colswap
        else:
            rowswap = min(rowswap, N-rowswap)
            colswap = min(colswap, N-colswap)
        return (rowswap + colswap)/2
            
                                        
                            
                    