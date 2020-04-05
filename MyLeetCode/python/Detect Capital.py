###
# String
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()
                            
                    