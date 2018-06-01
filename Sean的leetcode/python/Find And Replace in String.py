###
# String
# Time Complexity: O(nlogn+nl) n:num of operations, l:len of S
# Space Complexity: O(l)
###
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True): #from right to left, otherwise, modify the string will change the index
            if S[i:i+len(s)] == s:
                S = S[:i] + t + S[i+len(s):]
        return S
        
                                        
                            
                    