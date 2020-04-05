class TrieNode:
        def __init__(self):
            
            self.children = collections.defaultdict(TrieNode)
            self.is_word = False
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
        curr = self.root
        for e in word:
            curr = curr.children[e]
        curr.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for e in word:
            if e not in curr.children:
                return False
            curr = curr.children[e]
        return curr.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for e in prefix:
            if e not in curr.children:
                return False
            curr = curr.children[e]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)