###
# 2D Array
# Time Complexity: O(mn)
# Space Complexity: O(1)
###
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for j in xrange(-(-len(row)//2)):
                row[j], row[~j] = row[~j] ^ 1, row[j] ^ 1
        return A
                                        
                            
                    