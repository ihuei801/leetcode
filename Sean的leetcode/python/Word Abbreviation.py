###
# Hash Table + Trie
# Time Complexity: O(n*l)
# Space Complexity: O(n*l)
###
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.cnt = 0
class Trie(object):
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
    def insert(self, word):
        cur = self.root     
        for c in word:   
            cur = cur.children[c]
            cur.cnt += 1
           
            
class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        groups = collections.defaultdict(list)
        re = [None] * len(words)
        for i, word in enumerate(words):
            groups[(len(word), word[0], word[-1])].append((word, i))
        for _, wlist in groups.iteritems():
            if len(wlist) == 1:
                word, idx = wlist[0]
                if len(word) > 3:
                    re[idx] = word[0] + str(len(word)-2) + word[-1]
                else:
                    re[idx] = word
            else:        
                trie = Trie([w for w, i in wlist])
                for word, idx in wlist:
                    cur = trie.root
                    for i, c in enumerate(word):
                        cur = cur.children[c]
                        if cur.cnt == 1:
                            break
                    if len(word) - 2 - i > 1:
                        re[idx] = word[:i+1] + str(len(word) - 2 - i) + word[-1]
                    else:
                        re[idx] = word
        return re
        
        
        
                            
                    