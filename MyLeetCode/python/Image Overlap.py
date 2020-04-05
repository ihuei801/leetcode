###
# 2D Array
# Time Complexity: O(n^4)
# Space Complexity: O(n^2)
###
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        
        SA = [complex(i, j) for i, row in enumerate(A) for j, c in enumerate(row) if c == 1]
        SB = [complex(i, j) for i, row in enumerate(B) for j, c in enumerate(row) if c == 1]
        d = collections.Counter(a-b for a in SA for b in SB)
        return max(d.values() or [0])
                                        
                            
                    