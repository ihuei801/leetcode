###
# Hash Table
# Time Complexity: O(nl) l:len of word and licensePlate
# Space Complexity: O(1)
###
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        target = self.cnt(licensePlate)
        re = None
        for word in words:
            if (not re or len(word) < len(re)) and self.dominate(self.cnt(word), target):
                re = word
        return re
        
    def cnt(self, s):
        re = collections.defaultdict(int)
        for c in s:
            if c.isalpha():
                re[c.lower()] += 1
        
        return re
    
    def dominate(self, src, tgt):
        return all(src[c] >= n for c, n in tgt.iteritems())
            
        
                                        
                            
                    