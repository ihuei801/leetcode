###
# Trie: 
# Every node consists of multiple branches. Each branch represents a possible character of keys. 
# We need to mark the last node of every key as leaf node
# Time Complexity: Add: O(n) Search: O(26^n) n: average len of a word
# Space Complexity: Add: O(26*n) Search: O(26^n) 
###
class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(word, 0, self.root)
    def find(self, word, idx, node):
        if idx == len(word):
            return node.end
        c = word[idx]
        if c in node.children:
            return self.find(word, idx + 1, node.children[c])
        elif c == '.':
            for ch in node.children:
                if self.find(word, idx + 1, node.children[ch]):
                    return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)