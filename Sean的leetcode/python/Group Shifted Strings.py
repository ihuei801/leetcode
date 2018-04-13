###
# HashTable
# Time Complexity: O(n*l)
# Space Complexity: O(n)
###
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        if not strings:
            return []
        d = defaultdict(list)
        for s in strings:
            key = ""
            for c in s:
                diff = ord(c) - ord(s[0])
                if diff < 0:
                    diff += 26
                key += chr(ord('a') + diff)
            d[key].append(s)
        return d.values()
        