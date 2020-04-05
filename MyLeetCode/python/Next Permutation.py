###
# Array
# (1) For any given sequence that is in descending order, no next larger permutation is possible. 
#     For example, no next permutation is possible for the following array: [9, 5, 4, 3, 1]
#     So, We need to find the first pair of two successive numbers a[i] and a[i-1], from the right, which satisfy a[i] > a[i-1].
# (2) Create the permutation just larger than the current one by replacing the number a[i-1] 
#     with the number which is just larger than itself among the numbers lying to its right section, say a[j]
# (3) We need the smallest permutation that can be formed by using the numbers only to the right of a[i-1]. 
#     Therefore, we need to place those numbers in ascending order to get their smallest permutation. so reverse a[i] to the end
# Time complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        l = i + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        
        
        
    
        
        
        
        
    
        
        
        