###
# String
# a=b. If both the strings are identical, it is obvious that no subsequence will be uncommon
# length(a)=length(b) and a != b. Example: abc and abd. Either one can never be a subsequence of the other string
# length(a) != length(b). Example abcd and abc. In this case we can consider bigger string as a required subsequence 
# because bigger string can't be a subsequence of smaller string. Hence, return max(length(a),length(b)).
# Time Complexity: O(min(a, b))
# Space Complexity: O(1)
###
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))
        
                            
                    