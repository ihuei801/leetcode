###
# Trie + dfs
# Time Complexity: O(wl) + O(n*m*4*3^(l-1)) 4 direcs, each neighbor has 3 direcs
# Space Complexity: O(wl)
###
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        dct = self.build_dct(words)
        return self.search_word(board, dct)

    def build_dct(self, words):
        dct = Trie()
        for word in words:
            dct.insert(word)
        return dct

    def search_word(self, board, dct):
        results = set()
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                self.dfs(board, i, j, dct.root, "", results)
        return list(results)

    def dfs(self, board, i, j, cur, prefix, results):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return
        c = board[i][j]
        if c is '#' or c not in cur.children:
            return
        board[i][j] = '#'
        if cur.children[c].is_end:
            results.add(prefix + c)
        for nbi, nbj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            self.dfs(board, nbi, nbj, cur.children[c], prefix + c, results)
        board[i][j] = c


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_end = True


class TrieNode(object):
    def __init__(self):
        self.is_end = False
        self.children = collections.defaultdict(TrieNode)

######
# Version 2: dfs checker outside
######
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