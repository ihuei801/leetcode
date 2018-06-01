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
        m = len(word)
        n = len(abbr)
        i = 0
        j = 0
        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                s = j
                while j < n and abbr[j].isdigit():
                    j += 1
                i += int(abbr[s:j])
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == m and j == n
        
        
        