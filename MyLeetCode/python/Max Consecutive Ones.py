###
# Array
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxlen = 0
        n = len(nums)
        l, r = 0, 0
        while r < n:
            if nums[r] == 0:
                l = r + 1
            else:          
                maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen
                    
                       
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len = 0
        cur_len = 0
        for i, n in enumerate(nums):
            if n == 1:
                cur_len += 1   
            else:
                cur_len = 0
            max_len = max(max_len, cur_len)
        return max_len
                                        
                            
                    