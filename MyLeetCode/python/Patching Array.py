###
# Greedy
# Suppose miss is the smallest missing number, then we know that [1, miss) (left-closed, right-open) is already covered .
# In order to cover miss, we have to add something smaller than or equal to miss. 
# Otherwise, there is no way we can cover it.
# For example, you have any array nums = [1,2,3,8] and n = 16. 
# The numbers already covered is in the ranges [1, 6] and [8, 14]. 
# In other words, 7, 15, 16 are missing. If you add patches larger than 7, then 7 is still missing.
# Suppose the number we added is x. then, the ranges [1, miss) and [x, x + miss) are both covered. 
# And since we know that x <= miss, the two ranges will cover the range [1, x + miss). 
# We want to choose x as large as possible so that the range can cover as large as possible. 
# Therefore, the best option is x = miss.
# After we covered miss, we can recalculate the coverage and see what's the new smallest missing number. 
# We then patch that number. We do this repeatedly until no missing number.
# Time Complexity: O(m + logn) m : len of array 
# In each iteration, we either increase the index i or we double the variable miss. 
# Space Complexity: O(1)
###
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        missing = 1
        cnt = 0
        i = 0
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                cnt += 1
                missing += missing
        return cnt
        
        