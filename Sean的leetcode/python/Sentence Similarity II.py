###
# Union Find
# Time Complexity: O(p+n) p: size of pairs, n: len(words1) = len(words2)
# Space Complexity: O(p)
###
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        idx = itertools.count()
        dsu = DSU(len(pairs) * 2)
        word_to_idx = dict()
        for w1, w2 in pairs:
            if w1 not in word_to_idx:
                word_to_idx[w1] = next(idx)
            if w2 not in word_to_idx:
                word_to_idx[w2] = next(idx)
            dsu.union(word_to_idx[w1], word_to_idx[w2])
        for w1, w2 in itertools.izip(words1, words2):
            if w1 != w2:
                if w1 not in word_to_idx or w2 not in word_to_idx or dsu.find(word_to_idx[w1]) != dsu.find(
                        word_to_idx[w2]):
                    return False
        return True


class DSU(object):
    def __init__(self, n):
        self.roots = range(n)

    def find(self, v):
        if self.roots[v] != v:
            self.roots[v] = self.find(self.roots[v])
        return self.roots[v]

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            self.roots[r2] = r1
    
                                        
                            
                    