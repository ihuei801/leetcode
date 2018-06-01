###
# Trie
# Time Complexity: O(n*l) n:number of words, l: average len of words
# Space Complexity: O(n*l)
###
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = None
class Trie(object):
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.word = word
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie(words)
        self.re = ""
        self.dfs(trie.root)
        return self.re
    
    def dfs(self, node):
        if node.word and (len(node.word) > len(self.re) or (len(node.word) == len(self.re) and node.word < self.re)):
            self.re = node.word
        for c, child in node.children.iteritems():
            if child.word:
                self.dfs(child)
                                        
                            
                    