###
# Hash Table
# The basic idea is that we iterate through the input array and mark elements we've seen as negative 
# In the second iteration, if a value is not marked as negative, 
# it implies we have never seen that index before, so just add it to the return list.
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        return [i+1 for i, n in enumerate(nums) if n > 0]
            
            
                                        
                            
                    