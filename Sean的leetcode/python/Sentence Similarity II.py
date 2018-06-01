###
# Union Find
# Time Complexity: O(p+n)
# Space Complexity: O(p)
###
class DSU(object):
    def __init__(self, n):
        self.root = range(n)
    
    def find(self, v):
        if v != self.root[v]:
            self.root[v] = self.find(self.root[v])
        return self.root[v]
    
    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            self.root[r1] = r2
        
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
        d = dict()
        _id = itertools.count()
        n = len(pairs)
        dsu = DSU(2*n)
        
        for pair in pairs:
            for w in pair:
                if w not in d:
                    d[w] = next(_id)
            dsu.union(d[pair[0]], d[pair[1]])
        
        return all(w1 == w2 or (w1 in d and w2 in d and dsu.find(d[w1]) == dsu.find(d[w2])) for w1, w2 in zip(words1, words2))
            
    
    
                                        
                            
                    