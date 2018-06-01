###
# String
# We can split S to two parts for two coordinates.
# Then we use sub function f to find all possible strings for each coordinate.

# In sub functon f(S)
# if S == "": return []
# if S == "0": return [S]
# if S == "0XXX0": return []
# if S == "0XXX": return ["0.XXX"]
# if S == "XXX0": return [S]
# return [S, "X.XXX", "XX.XX", "XXX.X"...]

# Then we add the product of two lists to result.
# Time Complexity: sigma k*(n-k) = O(n^3)
# Space Complexity: O(n^3)
###
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def make(s):
            if len(s) > 1 and s[0] == s[-1] == '0':
                return []
            if s[-1] == '0':
                return [s]
            if s[0] == '0':
                return [s[0] + '.' + s[1:]]
            return [s] + [s[:i] + '.' + s[i:] for i in xrange(1, len(s))]
        S = S[1:-1]
        return ["({}, {})".format(a, b) for i in xrange(1, len(S)) for a, b in itertools.product(make(S[:i]), make(S[i:]))]
                                        
                            
                    