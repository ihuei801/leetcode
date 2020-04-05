###
# HashTable
# Time Complexity: O(m * n ^ 2) where m is the length of the list and the n is the length of the word.
# Space Complexity: O(m)
###
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d = {word: i for i, word in enumerate(words)}
        re = []
        for i, w in enumerate(words):
            for j in xrange(len(w)+1):
                str1 = w[:j]
                str2 = w[j:]
                if self.is_palindrome(str1):
                    if str2[::-1] in d and d[str2[::-1]] != i:
                        re.append([d[str2[::-1]], i])
                if str2 and self.is_palindrome(str2):
                    if str1[::-1] in d and d[str1[::-1]] != i:
                        re.append([i, d[str1[::-1]]])
        return re
    def is_palindrome(self, word):
        i = 0
        j = len(word) - 1
        while i <= j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True
                                        
                            
                    