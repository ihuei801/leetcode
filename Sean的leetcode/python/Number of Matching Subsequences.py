###
# 
# Since the length of S is large, let's think about ways to iterate through S only once.
# We can put words into buckets by starting character. 
# If for example we have words = ['dog', 'cat', 'cop'], 
# then we can group them 'c' : ('cat', 'cop'), 'd' : ('dog',). 
# This groups words by what letter they are currently waiting for. 
# Then, while iterating through letters of S, we will move our words through different buckets.
# For example, if we have a string like S = 'dcaog':
# heads = 'c' : ('cat', 'cop'), 'd' : ('dog',) at beginning;
# heads = 'c' : ('cat', 'cop'), 'o' : ('og',) after S[0] = 'd';
# heads = 'a' : ('at',), 'o' : ('og', 'op') after S[0] = 'c';
# heads = 'o' : ('og', 'op'), 't': ('t',) after S[0] = 'a';
# heads = 'g' : ('g',), 'p': ('p',), 't': ('t',) after S[0] = 'o';
# heads = 'p': ('p',), 't': ('t',) after S[0] = 'g'
# Time Complexity: O(S)
# Space Complexity: O(w*l)
###
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        d = collections.defaultdict(list)
        for it in map(iter, words):
            d[next(it, None)].append(it)
        for c in S:
            for it in d.pop(c, []):
                d[next(it, None)].append(it)
        return len(d[None])
                                        
                            
                    