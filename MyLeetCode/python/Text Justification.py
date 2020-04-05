###
# DFS
# Time Complexity: O(n)+O(s*L) n:num of words s:num of space l:num of lines
# Space Complexity: O(n)
###

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, curr, num_of_letters =  [], [], 0
        for word in words:
            if len(word) + len(curr) + num_of_letters > maxWidth:
                for i in xrange(maxWidth - num_of_letters):
                    curr[i%(len(curr)-1 or 1)] += ' ' 
                res.append(''.join(curr))
                curr, num_of_letters = [], 0
            curr.append(word)
            num_of_letters += len(word)
        return res + [' '.join(curr).ljust(maxWidth)]