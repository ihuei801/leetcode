###
# Hash Table + Trie
# Time Complexity: O(w*l)
# Space Complexity: O(w*l)
###
class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        groups = self.group_words(words)
        return self.get_abbr(groups, words)

    def group_words(self, words):
        dct = collections.defaultdict(list)
        for i, word in enumerate(words):
            dct[(len(word), word[0], word[-1])].append((word, i))
        return dct

    def get_abbr(self, groups, words):
        result = [None] * len(words)
        for (ln, start, end), word_lst in groups.iteritems():
            if len(word_lst) == 1:
                word, idx = word_lst[0]
                if ln > 3:
                    result[idx] = start + str(ln - 2) + end
                else:
                    result[idx] = word
            else:
                trie = Trie([word for word, idx in word_lst])
                for word, idx in word_lst:
                    prefix = self.get_prefix(trie, word)
                    if ln - len(prefix) > 2:
                        result[idx] = prefix + str(ln - len(prefix) - 1) + end
                    else:
                        result[idx] = word
        return result

    def get_prefix(self, trie, word):
        cur = trie.root
        for i, c in enumerate(word):
            cur = cur.children[c]
            if cur.cnt == 1:
                return word[:i + 1]


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


class TrieNode(object):
    def __init__(self):
        self.cnt = 0
        self.children = collections.defaultdict(TrieNode)
        
        
        
                            
                    