###
# Time Complexity: O(n*l*logl) n:num of words, l:num of chars in str
# Space Complexity: O(n)
###
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        d = collections.defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            d[k].append(s)
        
        return d.values()