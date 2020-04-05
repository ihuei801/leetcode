###
# String
# Time Complexity: O(nwl) n:len of S w:num of words l:len of word
# Space Complexity: O(n)
###
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        mask = [False] * len(S)
        for word in words:
            self.mark_word(word, S, mask)
        re = ""
        for i, c in enumerate(S):
            if mask[i] and (i == 0 or not mask[i-1]):
                re += "<b>"
            re += c
            if mask[i] and (i == len(S) - 1 or not mask[i+1]):
                re += "</b>"
        return re
    def mark_word(self, word, S, mask):
        for i in xrange(len(S)-len(word)+1):
            if word == S[i:i+len(word)]:
                for j in xrange(i, i+len(word)):
                    mask[j] = True
           
       
            
                                        
                            
                    