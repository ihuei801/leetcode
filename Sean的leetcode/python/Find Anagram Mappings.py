###
# Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for i, e in enumerate(B):
            d[e].append(i)
        return [d[e].pop() for e in A]
                                        
                            
                    