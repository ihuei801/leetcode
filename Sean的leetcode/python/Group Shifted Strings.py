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
        d = collections.defaultdict(list)
        for s in strings:
            key = []
            for c in s:
                key.append((ord(c) - ord(s[0])) % 26)
            d[tuple(key)].append(s)
        return d.values()
            
            
cclass Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strings:
            key = ""
            for c in s:
                key += chr(ord("a") + (ord(c) - ord(s[0])) % 26)
            d[key].append(s)
        return d.values()
            
        