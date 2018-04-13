###
# Trie
# Time Complexity: insert - O(n) search - O(n) startswith - O(n)
# Space Complexity: insert - O(n) search - O(1) startswith - O(1)
###
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False
    
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_end = True
        
    def find(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.find(word)
        return cur is not None and cur.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.find(prefix)
        return cur is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)