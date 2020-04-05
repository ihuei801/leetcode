###
# Bit Manipulation
# For each dictionary word (of correct size), create a diff-number whose bits tell me which of the word's letters differ from the target. 
# Then go through the 2**m possible abbreviations, represented as number from 0 to 2**m-1, 
# the bits representing which letters of target are in the abbreviation. 
# An abbreviation is ok if it doesn't match any dictionary word. 
# To check whether an abbreviation doesn't match a dictionary word, I simply check whether the abbreviation number and the dictionary word's diff-number have a common 1-bit. 
# Which means that the abbreviation contains a letter where the dictionary word differs from the target.
# Then from the ok abbreviations I find one that minimize the len of abbreviation.
# Time Complexity: 
# Space Complexity: 
###
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        m = len(target)
        diff = set()
        for word in dictionary:
            if len(word) != m:
                continue
            bits = 0
            for i, w in enumerate(word):
                if w != target[i]:
                    bits += 2**i
            diff.add(bits)
        if not diff:
            return str(m)
        abbrs = []
        for i in xrange(2**m):
            if all(i & d for d in diff):
                abbrs.append(self.abbr(target, i))
        return min(abbrs, key=lambda x:len(x))
    
    def abbr(self, target, mask):
        re = ""
        cnt = 0
        for w in target:
            if mask & 1:
                if cnt:
                    re += str(cnt)
                    cnt = 0
                re += w
            else:
                cnt += 1
            mask >>= 1
        if cnt:
            re += str(cnt)
        return re
        
                                        
                            
                    