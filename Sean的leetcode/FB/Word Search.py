###
# DFS
# Time Complexity: O(n*m*4^(k)) n:row m:col k:len of word
# Space Complexity: O(k)
###

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False
        
    def dfs(self, board, i, j, word, idx):
        if len(word) == idx:
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[idx] != board[i][j]:
            return False
        board[i][j] = '#'
        exist = self.dfs(board, i+1, j, word, idx+1) or self.dfs(board, i-1, j, word, idx+1) or self.dfs(board, i, j-1, word, idx+1) or self.dfs(board, i, j+1, word, idx+1)
        board[i][j] = word[idx]
        return exist