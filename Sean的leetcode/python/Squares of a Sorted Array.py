###
# Two Pointer
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(A) - 1
        result = [0] * len(A)
        p = len(A) - 1
        while l <= r:
            l_sqr = A[l] * A[l]
            r_sqr = A[r] * A[r]
            if l_sqr > r_sqr:
                result[p] = l_sqr
                l += 1
            else:
                result[p] = r_sqr
                r -= 1
            p -= 1
        return result


        
    
        
                                        
                            
                    