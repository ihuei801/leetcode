###
# Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        cnt = collections.Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1
                                        
                            
                    