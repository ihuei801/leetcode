###
# Design Hash Table
# Time Complexity: O(n*l)
# Space Complexity: O(n*l)
###
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()

    def buildDict(self, dct):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dct:
            for i in xrange(len(word)):
                key = word[:i] + "*" + word[i+1:]
                if key not in self.d:
                    self.d[key] = word[i]
                else:
                    self.d[key] = '*'
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(word)):
            key = word[:i] + "*" + word[i+1:]
            if key in self.d and self.d[key] != word[i]:
                return True
        return False
            


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
                                        
                            
                    