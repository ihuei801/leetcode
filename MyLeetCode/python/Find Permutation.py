###
# Two Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        A = range(1, len(s)+2)
        r = 0
        while r < len(s):
            if s[r] == 'D':
                l = r
                while r < len(s) and s[r] == 'D':
                    r += 1
                self.reverse(A, l, r)
            else:
                r += 1
        return A
    
    def reverse(self, A, l, r):
        while l <= r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1
                                        
                            
                    