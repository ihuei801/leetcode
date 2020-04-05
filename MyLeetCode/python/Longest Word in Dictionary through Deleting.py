###
# Design Deque
# Time Complexity: O(nl)
# Space Complexity: O(1)
###
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        self.maxsub = ""
        for word in d:
            if self.is_subseq(s, word):
                if len(word) > len(self.maxsub) or (len(word) == len(self.maxsub) and word[0] < self.maxsub):
                    self.maxsub = word
        return self.maxsub
                                                
                                                    
    def is_subseq(self, s, word):
        if len(word) > len(s):
            return False
        i = 0
        j = 0
        while j < len(word):
            while i < len(s) and s[i] != word[j]:
                i += 1
            if i == len(s):
                return False
            i += 1
            j += 1
        return True
            
                                        
                            
                    