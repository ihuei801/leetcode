###
# Binary Tree
# Find the parent of current by recursive call -(-k)//2
# if parent if 0, current is 0 if k is odd else 1
# if parent is 1, current is 1 if k is odd else 0
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0 
        if self.kthGrammar(N-1, -(-K//2)) == 0:
            return 0 if K & 1 else 1
        else:
            return 1 if K & 1 else 0
             
        
        