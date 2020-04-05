###
# Back Tracking
# Time Complexity: O(n*l) build a trie/hash table  + O(n^l) (use pruning, hard to analyze)
###
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.startwith = []
        
class Trie(object):
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur.startwith.append(word)
                cur = cur.children[c]
                
    def find_by_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        return cur.startwith
    
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words:
            return []
        size = len(words[0])
        trie = Trie(words)
        square = []
        squares = []
        self.bt(trie, 0, size, square, squares)
        return squares
    
    def bt(self, trie, cur, target, square, squares):
        if len(square) == target:
            squares.append(square)
            return
        prefix = ''
        if cur:
            prefix = ''.join(zip(*square)[cur])
        for word in trie.find_by_prefix(prefix):          
            self.bt(trie, cur + 1, target, square + [word], squares)
            

class Solution(object):
    
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        if not words:
            return []
        size = len(words[0])
        table = defaultdict(list)
        for word in words:
            for i in xrange(size):
                table[word[0:i]].append(word)
        squares = []
        square = [] 
        self.build(table, size, square, squares)
        return squares
    def build(self, table, size, square, squares):
        if len(square) == size:
            squares.append(square)
            return
        prefix = ''
        if square:
            prefix = ''.join(zip(*square)[len(square)])
        for word in table[prefix]:
            self.build(table, size, square + [word], squares)
        
        