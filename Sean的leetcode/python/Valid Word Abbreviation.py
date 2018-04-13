###
# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                k = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                num = int(abbr[k:j])
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
        
        