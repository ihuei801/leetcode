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
        if not board or not board[0] or not word:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board, i, j, word, idx):
        if len(word) == idx:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
            return False
        direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        board[i][j] = '#'
        found = False
        for dr, dc in direc:
            if self.dfs(board, i+dr, j+dc, word, idx+1):
                found = True
                break
        board[i][j] = word[idx]
        return found
        
        