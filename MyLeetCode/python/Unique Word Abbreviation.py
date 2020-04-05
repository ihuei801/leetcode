###
# Hash Table
# Time Complexity: 
# init: O(n*l)
# isUnique: O(l) 
###
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        from collections import defaultdict
        self.d = defaultdict(set)
        for word in dictionary:
            if len(word) <= 2:
                key = word
            else:
                key = word[0] + str(len(word) - 2) + word[-1]
            self.d[key].add(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 2:
            key = word
        else:
            key = word[0] + str(len(word) - 2) + word[-1]
        return key not in self.d or word in self.d[key] and len(self.d[key]) == 1
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
        
        