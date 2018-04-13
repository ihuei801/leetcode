###
# Time Complexity: O(n)
###
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join([str(len(s)) + '#' + s for s in strs])

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            idx = s.find('#', i)
            l = int(s[i:idx])
            strs.append(s[idx+1:idx+1+l])
            i = idx + 1 + l
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
        
        