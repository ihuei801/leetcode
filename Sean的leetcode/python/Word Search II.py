###
# Trie + dfs
# Time Complexity: O(wl) + O(n*m*l)
# Space Complexity: O(wl)
###
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        
class Trie(object):
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
            
    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie(words)
        re = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c in trie.root.children:
                    self.dfs(board, i, j, trie.root, "", re)
        return re
    
    def dfs(self, board, i, j, root, one_sol, re):
        c = board[i][j]
        cur = root.children[c]
        if cur.is_word:
            re.append(one_sol+c)
            cur.is_word = False
        m = len(board)
        n = len(board[0])        
        board[i][j] = '#'
        for nbi, nbj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if nbi >= 0 and nbi < m and nbj >= 0 and nbj < n and board[nbi][nbj] != "#" and board[nbi][nbj] in cur.children:
                self.dfs(board, nbi, nbj, cur, one_sol + c, re)
        board[i][j] = c
        
                
                
        
        