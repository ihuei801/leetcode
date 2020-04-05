###
# Bit Manipulation
# Build the answer bit by bit from left to right. 
# Let’s say we already know the largest first seven bits we can create. 
# How to find the largest first eight bits we can create? 
# Well it’s that maximal seven-bits prefix followed by 0 or 1. 
# Try to create the 1 one from two eight-bits prefixes from nums.
# Time Complexity: O(n)
# Space Complexity: O(n)
###   
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 0
        ans = 0
        for i in xrange(31, -1, -1):
            mask = mask | (1 << i)
            prefix = {n & mask for n in nums}
            tmp = ans | (1 << i)
            for pre in prefix:
                if tmp ^ pre in prefix:
                    ans = tmp
                    break
        return ans
                    
        
                            
   