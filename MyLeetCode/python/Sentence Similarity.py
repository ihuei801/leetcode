###
# HashTable
# Time Complexity: O(p+n) p:num of pairs n: num of words
# Space Complexity: O(p)
###
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        edges = collections.defaultdict(set)
        if len(words1) != len(words2):
            return False
        for w1, w2 in pairs:
            edges[w1].add(w2)
            edges[w2].add(w1)
        
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and (w1 not in edges or w2 not in edges or w2 not in edges[w1]):
                return False
            
        return True
                
                                        
                            
                    