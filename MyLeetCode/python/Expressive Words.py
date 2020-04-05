###
# Two Pointers
# Time Complexity: O(n*l)
# Space Complexity: O(1)
###
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for word in words:
            if self.can_ext(S, word):
                res += 1
        return res
    def can_ext(self, S, word):
        i = 0
        j = 0
        while i < len(S) or j < len(word):
            if i == len(S) or j == len(word) or S[i] != word[j]:
                return False 
            cnt1 = 1
            while i+1 < len(S) and S[i+1] == S[i]:
                i += 1
                cnt1 += 1
            cnt2 = 1
            while j+1 < len(word) and word[j+1] == word[j]:
                j += 1
                cnt2 += 1
            if (cnt1 < 3 and cnt1 != cnt2) or cnt1 >= 3 and cnt1 < cnt2:
                return False
            i += 1
            j += 1
        return True
                
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for word in words:
            if self.can_ext(S, word):
                res += 1
        return res
    
    def can_ext(self, S, word):
        if len(word) > S:
            return False
        i = 0
        j = 0
        while i < len(S) or j < len(word):
            if i == len(S) or j == len(word) or S[i] != word[j]:
                return False
            while i < len(S) and j < len(word) and S[i] == word[j]:
                i += 1
                j += 1
            if i == len(S) and j == len(word):
                return True
            while i > 0 and i < len(S) and S[i] == S[i-1]:
                i += 1
            if i < 3 or S[i-1] != S[i-2] or S[i-2] != S[i-3]:
                return False
        return True
                
                                        
                            
                    