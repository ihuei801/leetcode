###
# Array
# Time Complexity: O(m*n)
# Space Complexity: O(1)
###
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        
        for i, word in enumerate(words):
            for j, c in enumerate(word):
                if j >= len(words) or i >= len(words[j]) or c != words[j][i]:
                    return False
        return True
        