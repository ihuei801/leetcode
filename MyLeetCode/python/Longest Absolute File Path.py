###
# Hash Table
# Time Complexity: O(n) 
# Space Complexity: O(n)
###
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0
        maxlen = 0
        d = {0:0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            level = len(line) - len(name)
            if '.' not in name:
                d[level+1] = d[level] + len(name) + 1
            else:
                maxlen = max(maxlen, d[level] + len(name))
        return maxlen
        
        